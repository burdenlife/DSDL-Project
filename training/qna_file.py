### This file is used to generate the Q&A questions for Chess.ipynb

### IF YOU ARE A LAB PARTICIPANT DO NOT READ THE CODE

### DON'T BE A FILTHY CHEATER !!!!1!!111!!!!

















S1_QUESTIONS = [
    {
        'question': "[Easy] What does each row represent?",
        'options': [
            "Each row is a unique player",
            "Each row is a unique chess game",
            "Each row is a unique half-move",
            "Each row is a unique move found to be cheated"
        ],
        'explanation': 'Yes! \nYou can see this explicitly mentioned in the article: "In ChessFraud, each physical half-move is stored once".\nYou can also tell by analysing field headers with df.columns',

        'answer': 3,
        'help_txt': "Wrong Answer please try again."
    },
    {
        'question': "[Easy] How many fields are available in the dataset?",
        'explanation': "Yes! \nYou can check by running print(len(df.columns)) or count manually I guess...",
        'answer': 33,
        'help_txt': "How do you obtain columns in pandas? \nHmm is there a way to count number of objects in a list?"
    },
    
    {
    
        'question': "[Intermediate] Find the column with the most number of Null values. How many Null values does this column have?",
        'explanation': "Yes! \nYou can obtain the rows with null values for a column using df[df[<column.].isna()]",
        'answer': 29105,
        'help_txt': "Recall how to find null values in pandas."
    },
    
    {
        'question': "[Easy] How many cheated moves are there in the dataset?",
        'explanation': "Yes! \nYou can find the numner of cheated moves using the df[<column name>].value_counts or len(df[df[<column name>]])",
        'answer': 9405,
        'help_txt': "How can I find count of unqiue values for a field in a pandas df? \nGoogle it!"
    },

    {
        'question': "[Intermediate] Which best describes what maia2_win_prob_2050?",
        'options': [
            "It is the Win Probability of the player making the move according to Maia (a chess grandmaster rated 2050)",
            "It is the Win Probability of the player making the move according to Maia (the strongest chess AI engine)",
            "It is the Probability that someone wins the game according to Maia (the strongest chess AI engine)",
            "It is the Win Probability of the player making the move according to Maia (a chess AI engine rated 2050)"
        ],
        'explanation': "Yes! Maia is a chess engine which simulates human behaviour. Cheaters might use it because it may be harder to detect than the strongest engines!",
        'answer': 4,
        'help_txt': "Just Google it!"
    },

    {
        'question': "[Hard] Hmm maybe the eval_after and eval_before fields are useful.\n Find out how much cheating affects the distribution of eval_before and eval_after.\n If a move was cheated, how much more would the eval be improved than if a move had not been cheated?\n (round off to 2dp, answer is positive)",
        'explanation': "Yes! \nYou can first create a eval_diff field using eval_after - eval_before, then use the .groupby and .agg methods to calculate the mean values and take the difference.",
        'answer': 241,
        'help_txt': "eval improve refers to eval_after - eval_before. \np.s. Try creating a field if its too cumbersome!"
    }
]



S2_QUESTIONS = [
    {
        'question': "[Easy] Which row should we use as our dependent variable?",
        'options': [
            "is_cheating_move",
            "is_accused_by_opponent",
            "is_cheating_player_game",
            "opponent_elo"
        ],
        'explanation': 'Yes! \nSince we are trying to design an anti-cheat engine, we should naturally try to predict if a given move is cheated.',

        'answer': 1,
        'help_txt': 'What are we trying to predict?'
    },

    {
        'question': "[Easy] Should I use player_id as an independent variable (predictor)?",
        'options': [
            "Yes. Player ID has a healthy number of unique values (49). It is a useful field to identify the datapoint reference.",
            "No. Player ID is not a numeric field and cannot be understood by ML models.",
            "Yes. If a cheating player had been caught before, their player_id is a good predictor of a cheating move",
            "No. Player ID identifies the player rather than their behaviour, the model may simply memorise known cheaters instead of learning general behavioural patterns to catch unknown cheaters."
        ],
        'explanation': 'Yes! \nIf player_id is included, the model may learn that certain IDs are associated with cheating rather than learning the behavioural patterns associated with cheating. \nThis can cause the model to perform well on players it has seen before but fail to detect cheating by previously unseen players',

        'answer': 4,
        'help_txt': 'Imagine yourself as the ML engine. Should knowing that Bob the Janitor played the move affect your cheating prediction?'
    },

    {
        'question': "[Easy] Should I use move_stockfish_1 (recommended engine move at depth=1) as an independent variable?",
        'options': [
            "Yes. I am not a very good chess player, so I have to reference the engine move to know if a move is cheated.",
            "No. Depth 1 is too shallow. We should use move_stockfish_15 instead.",
            "No. While the field may be useful, the specific best move does not affect the distribution of cheating moves I would expect.",
            "Yes. Cheaters tend to use chess engines, of course the recommended move will affect the probability of cheating"
        ],
        'explanation': 'Yes! \nAlthough the cheater may use stockfish, the best move on its own is not a useful independent variable.',

        'answer': 3,
        'help_txt': 'Imaging yourself as the ML engine. Will knowing that the best move is Pawn to E4 affect your cheating prediction?'
    },
    {
        
        'question': "[Intermediate] player_hint_shown refers to whether the player had access to an engine at the time. Should it be included as an independent variable?",
        'options': [
            "Yes. Access to an engine makes cheating alot easier. So it will make a strong predictor",
            "No. Just because a player has access to an engine does not mean the player cheated",
            "No. Players can also cheat by phoning a GM or getting their older sibling to play so its not a strong predictor",
            "No. The ML engine will not have access to this information when it is performing its inference and prediction. \nThis will degrade the usefullness of the model"
        ],
        'explanation': 'Yes! \nIt is important to consider the data you are able to provide the model during inference. If only we had a is_attacker=True field available in splunk :(',

        'answer': 4,
        'help_txt': "Wrong Answer please try again."
    },

    {
        'question': "[Intermediate] Centipawn loss refers to how bad the move was compared to the best move.  How should we handle the fields centipawn_loss, normalized_centipawn_loss?",
        'options': [
            "Include BOTH as independent variables",
            "Include ONLY ONE as an independent variable",
            "Include NONE as independent variables",
            "Aggregate them into one independent variable"
        ],
        'explanation': 'Yes! \nSince one of these fields is derived from the other, the model will be skewed if we include both',
        'answer': 2,
        'help_txt': "Wrong Answer please try again."

    }
]
    

SELECTED_FEATURES = [
    'player_color',
    'player_elo', 
    'move_player',
    'opponent_elo', 
    'half_move', 
    'move_thinking_time', 
    'clock_remaining_time', 
    'move_stockfish_1', 
    'move_stockfish_9', 
    'move_stockfish_15',
    'move_maia2_2050', 
    'move_allie_2500',
    'normalized_centipawn_loss',
    'is_cheating_move'
]


S3_QUESTIONS = [

    {
        'question': "[Intermediate] Lets first remove all rows with null values. How many rows are left?",
        'explanation': 'Yes! \nYou can use df_new = df[df[<column>].isna() == False] or other equivalent commands to create a filtered df',
        'answer': 28410,
        'help_txt': 'Google `remove rows with null values pandas.`'
    },
    {
        'question': "[Intermediate] Knowing that a player's move matches an engine recommendation is useful to include in our model. How should we do this?",
        'options': [
            "Create a new field matches_engine_move which is True when player move matches an engine move and False otherwise. Include this new field and EXCLUDE all other moves.",
            "Include ALL fields (engine moves and player moves) in the ML model",
            "Include ONLY the player move in the ML model.",
            "Create a new field matches_engine_move which is 1 when player move matches an engine move and 0 otherwise. Include ALL fields.",
            "Include ONLY one engine move AND the player move in the ML model"
            
        ],
        'explanation': 'Yes! \nThe useful information we need to pass the ML model is whether the move matches an engine move. Including the moves themselves should not improve model performance.',
        'answer': 1,
        'help_txt': 'What information are we passing to the model?'
    },

    {
        'question': "[Hard] Create the field matches_engine_move. How many rows have matches_engine_move == True? Engine moves are: [ 'move_stockfish_1', 'move_stockfish_9', 'move_stockfish_15', 'move_maia2_2050', 'maia2_win_prob_2050', 'move_allie_2500',]",
        'explanation': 'Yes! \nHere is the solution I found: \nfiltered_df["matches_engine_move"] = filtered_df[bot_moves].eq(filtered_df["move_player"], axis=0).any(axis=1)\nBut there are many other solutions',
        'answer': 22210,
        'help_txt': 'Just Google or ChatGPT it bro...'
    },
    {
        'question': "[Very Hard] For us to use categorical variables such as player_colour, we will need to encode it. Create new columns with the encoded values of both player_colour (white=1, black=0) and matches_engine_move (True=1, False=0). The headers should be named player_color_encoded and matches_engine_move_encoded"
    }
    
]


def check_df(df):
    import numpy as np
    try:
        invalid_rows = df[(df['matches_engine_move_encoded'] == 0) & (df['matches_engine_move'] != False)]
        assert len(invalid_rows) == 0

        invalid_rows = df[(df['matches_engine_move_encoded'] == 1) & (df['matches_engine_move'] != True)]
        assert len(invalid_rows) == 0
    except KeyError:
        print("Ensure that columns matches_engine_move_encoded and matches_engine_move exist!")
        return
    except AssertionError:
        print("Wrong dataframe format detected. Ensure that column matches_engine_move_encoded is set to 1 when matches_engine_move is True and 0 otherwise.")
        return
    

    try:
        invalid_rows = df[(df['player_color_encoded'] == 0) & (df['player_color'] != 'black')]
        assert len(invalid_rows) == 0

        invalid_rows = df[(df['player_color_encoded'] == 1) & (df['player_color'] != 'white')]
        assert len(invalid_rows) == 0
    except KeyError:
        print("Ensure that columns player_color_encoded and player_color exist!")
        return
    except AssertionError:
        print("Wrong dataframe format detected. Ensure that column player_color_encoded is set to 1 when player_color is white and 0 otherwise.")
        return

    print("Yup! Now all the fields we want to pass the model are numeric and can be understood!")



def check_train_test(X_train, X_test, y_train, y_test):
    try:
        assert list(X_train.columns) == list(X_test.columns) == ['player_color_encoded', 'player_elo', 'opponent_elo', 'half_move', 'move_thinking_time', 'clock_remaining_time', 'normalized_centipawn_loss', 'matches_engine_move_encoded']
        assert len(X_train) == len(y_train) > len(X_test) == len(y_test)
    except Exception  as e:
        print(e)
        print("Invalid input. Are you using the right dependent(Y) and independent(X) variables?")
        return
    print("Well done!")



S4_QUESTIONS = [

    {
        'question': "[Intermediate] Oh no! Your code ran with an error! Based on the error message (and a Google search if you need it), \nwhich of the following best describes what is happening?",
        'options': [
            "The model stpped iterating before it was able to construct the perfect model",
            "The model we chose is incompatable with the data we provided",
            "The model is not able to identify which fields should be used for prediction",
            "The model stopped iterating because we forgot to add an end condition.",
            "Logistics Regression is not a good ML model"
            
        ],
        'explanation': 'Yes! \nOur model ran too few iterations to converge to the ideal model',
        'answer': 1,
        'help_txt': 'Google/ChatGPT the error message'
    },
        
]



S5_QUESTIONS = [

    {
        'question': "[Intermediate] Lets try to understand our metrics. What does the `support` collumn in the report refer to?",
        'options': [
            "Confidence score",
            "Weighted Average",
            "Number of rows matching the category",
            "Model Accuracy."
            
        ],
        'explanation': 'Yes! \nSupport refers to number of events which supports the metric.',
        'answer': 3,
        'help_txt': 'What do we have thousands of?'
    },

    {
        'question': "[Intermediate] If we were concerned only with False Positives(FP), which metric should we look at?",
        'options': [
            "F1 score",
            "Calculate percentage of All Positives (prediction=True) that are FPs",
            "Accuracy",
            "Calculate percentage of All Records that are FPs."
        ],
        'explanation': 'Yes! \nFalse Positives occur when a move was not cheated but wrongly detected as cheated by the model.\nAs such it is concerning how much can we trust that a move detected as cheated by the model was actually cheated.\nSo it makes sense to only consider moves which the model detects as cheated.',
        'answer': 2,
        'help_txt': 'What are we worried about when we calculate FPs?'
    },
    {
        'question': "[Intermediate] Our model has a True recall rate of 0.09. What does this mean?",
        'options': [
            "The model predicted is_cheated_move correctly 9% of the time",
            "The model was able to correctly predict 9% of the cheated moves as cheated",
            "The model only predicted 9% of the datapoints as cheated",
            "The model was able to correctly predict 9% of the NOT cheated moves as NOT cheated."
        ],
        'explanation': 'Yes! \nRecall is concerned with `How many of the correct answer was preserved?`\nSince this is the recall rate of `True` values, the answer is 2.',
        'answer': 2,
        'help_txt': 'What are we worried about when we calculate FPs?'
    },

    {
        'question': "[VERY EASY] The model is only able to detect 9% of the cheated moves. Is this satisfactory?",
        'options': [
            "Its satisfactory",
            "It is NOT AT ALL satisfactory",
            "Aiya wgt optimise the model? ORD loh...",
            "Its too late to give up on this model! Lets try more test sets and give it another chance!"
        ],
        'explanation': 'Yes! \n9% recall rate is f*cking trash!',
        'answer': 2,
        'help_txt': "DON'T BE LAZY!"
    },

    {
        'question': "[Intermediate] Yay! Our True recall has shot up to 67%. But we also see that our overall accuracy has fallen from 75% to 64%. Is this model better than our previous model? Why?",
        'options': [
            "It is better. Since we did more work in transforming the model, the results have to be better!",
            "It is better. A lazy model is functionally useless, since it is almost equivalent to blindly guessing False for all values.",
            "It is worse. Recall is a subset of accuracy. Therefore, a drop in accuracy is more telling than the increase in recall.",
            "It is better. The increase in recall is bigger than an increase in accuracy. Bigger number better therefore recall is better."
        ],
        'explanation': 'Yes! \nWhile 4 is true most of the time, 2 is more indicative of an improvement in the model performance.',
        'answer': 2,
        'help_txt': "Which is more useful? A model which meta-games telling you False all the time or a model that actively tries to predict but gets it wrong more?"
    },
    
        
]
