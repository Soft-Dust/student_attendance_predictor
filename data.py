"""
Student Attendance Dataset
Contains sample data for training the attendance prediction model
"""

# Dataset: Student attendance information
# Features: past_attendance (%), classes_missed (last week), is_sick (0/1)
# Target: will_attend (0/1)

import pandas as pd

def get_dataset():
    """Returns the student attendance dataset"""
    
    data = {
        'past_attendance': [95, 88, 72, 91, 65, 84, 78, 92, 68, 89, 
                           75, 93, 61, 87, 79, 94, 70, 85, 77, 90,
                           82, 73, 96, 59, 81, 67, 89, 74, 83, 69],
        'classes_missed': [0, 1, 3, 0, 4, 1, 2, 0, 3, 1,
                          2, 0, 5, 1, 2, 0, 3, 1, 2, 0,
                          1, 4, 0, 6, 2, 3, 0, 2, 1, 4],
        'is_sick': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
                   1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
                   0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        'will_attend': [1, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                       0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                       1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    }
    
    return pd.DataFrame(data)

def get_features_and_target():
    """Separates features and target from the dataset"""
    df = get_dataset()
    X = df[['past_attendance', 'classes_missed', 'is_sick']]
    y = df['will_attend']
    return X, y
