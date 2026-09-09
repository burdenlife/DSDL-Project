#!/usr/bin/env python3

import json
import subprocess
import time
from pathlib import Path
from datetime import datetime, timezone


# ============================================================
# CONFIG
# ============================================================

BASE = Path.home() / "cadets_google_drive"

INPUT_DIRS = [
    BASE / "official",
    BASE / "official_1",
    BASE / "official_2",
]

TEMP_FILE = BASE / "cadets_ingest_temp.ndjson"

SPLUNK = "/opt/splunk/bin/splunk"

INDEX = "cadets"
SOURCETYPE = "cadets:cdm18"

# Give Splunk time to optimize buckets before submitting
# another multi-million-record file.
WAIT_AFTER_INGEST = 60


# ============================================================
# TIMESTAMP CONVERSION
# ============================================================

def ns_to_iso(ns):
    ns = int(ns)

    seconds, nanos = divmod(ns, 1_000_000_000)

    dt = datetime.fromtimestamp(
        seconds,
        tz=timezone.utc
    )

    return (
        dt.strftime("%Y-%m-%dT%H:%M:%S")
        + f".{nanos:09d}Z"
    )


# ============================================================
# CDM PARSING
# ============================================================

def get_record_type_and_body(record):

    datum = record.get("datum")

    if not isinstance(datum, dict) or not datum:
        return None, None

    key = next(iter(datum))

    body = datum[key]

    record_type = key.rsplit(".", 1)[-1]

    return record_type, body


def get_semantic_timestamp(record_type, body):

    if not isinstance(body, dict):
        return None, None

    if record_type == "Event":
        return body.get("timestampNanos"), "event"

    if record_type == "Subject":
        return body.get("startTimestampNanos"), "subject_start"

    return None, "none"


# ============================================================
# TRANSFORMATION
# ============================================================

def transform(record):

    record_type, body = get_record_type_and_body(record)

    if record_type:
        record["record_type"] = record_type

    timestamp_ns, time_type = get_semantic_timestamp(
        record_type,
        body
    )

    record["time_type"] = time_type

    if timestamp_ns is not None:

        try:
            record["event_time"] = ns_to_iso(timestamp_ns)

        except (ValueError, TypeError, OverflowError):
            pass

    return record


# ============================================================
# SPLUNK
# ============================================================

def run_splunk_oneshot(path):

    command = [
        "sudo",
        SPLUNK,
        "add",
        "oneshot",
        str(path),
        "-index",
        INDEX,
        "-sourcetype",
        SOURCETYPE,
    ]

    print("\n[+] Submitting to Splunk...")

    result = subprocess.run(command)

    if result.returncode != 0:
        print("\n!!! SPLUNK ONESHOT FAILED !!!")
        print(f"Temporary file retained at: {path}")
        raise SystemExit(1)

    print("[+] Splunk accepted oneshot input.")


# ============================================================
# MAIN
# ============================================================

grand_total = 0
grand_bad = 0

for directory in INPUT_DIRS:

    print()
    print("=" * 70)
    print(f"DIRECTORY: {directory}")
    print("=" * 70)

    files = sorted(
        p for p in directory.iterdir()
        if ".json" in p.name and p.is_file()
    )

    for source_file in files:

        print()
        print("-" * 70)
        print(f"SOURCE: {source_file.name}")
        print("-" * 70)

        file_total = 0
        file_bad = 0
        file_timed = 0

        # Always overwrite the previous temporary file.
        with (
            source_file.open(
                "r",
                encoding="utf-8"
            ) as fin,
            TEMP_FILE.open(
                "w",
                encoding="utf-8"
            ) as fout
        ):

            for line in fin:

                try:
                    record = json.loads(line)

                except json.JSONDecodeError:
                    file_bad += 1
                    continue

                record = transform(record)

                if "event_time" in record:
                    file_timed += 1

                fout.write(
                    json.dumps(
                        record,
                        separators=(",", ":")
                    )
                    + "\n"
                )

                file_total += 1

                if file_total % 500_000 == 0:
                    print(
                        f"  transformed "
                        f"{file_total:,} records..."
                    )

        print()
        print(f"Transformed records: {file_total:,}")
        print(f"Timestamped records: {file_timed:,}")
        print(f"Bad JSON lines:      {file_bad:,}")

        # ====================================================
        # CRITICAL SANITY CHECK
        # ====================================================

        if file_total == 0:
            print("!!! EMPTY FILE - ABORTING !!!")
            raise SystemExit(1)

        # ====================================================
        # INGEST
        # ====================================================

        run_splunk_oneshot(TEMP_FILE)

        # ====================================================
        # DO NOT DELETE IMMEDIATELY
        # ====================================================

        print()
        print(
            f"[+] Waiting {WAIT_AFTER_INGEST} seconds "
            "for Splunk indexing/optimization..."
        )

        time.sleep(WAIT_AFTER_INGEST)

        print()
        print(
            "[+] Finished wait period."
        )

        # ====================================================
        # DELETE ONLY AFTER WAIT
        # ====================================================

        TEMP_FILE.unlink()

        print(
            "[+] Temporary transformed file deleted."
        )

        grand_total += file_total
        grand_bad += file_bad

        print(
            f"[+] Cumulative records submitted: "
            f"{grand_total:,}"
        )


print()
print("=" * 70)
print("ALL SOURCE FILES SUBMITTED")
print("=" * 70)

print(f"Records submitted: {grand_total:,}")
print(f"Bad JSON lines:    {grand_bad:,}")

print()
print("Expected canonical total: 44,404,329")
