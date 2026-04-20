"""
Student Attendance Prediction Model
Handles model training and prediction using Logistic Regression
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from data import get_features_and_target
import pandas as pd

class AttendancePredictor:
    def __init__(self):
        self.model = LogisticRegression(random_state=42, max_iter=200)
        self.accuracy = 0
        self.is_trained = False
    
    def train(self):
        """Train the logistic regression model"""
        # Get dataset
        X, y = get_features_and_target()
        
        # Split data for training and testing
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Calculate accuracy
        y_pred = self.model.predict(X_test)
        self.accuracy = accuracy_score(y_test, y_pred)
        self.is_trained = True
        
        print(f"Model trained successfully!")
        print(f"Model Accuracy: {self.accuracy:.2f}")
    
    def predict(self, past_attendance, classes_missed, is_sick):
        """
        Predict if student will attend next class
        
        Args:
            past_attendance (float): Attendance percentage (0-100)
            classes_missed (int): Number of classes missed last week
            is_sick (int): 0 if not sick, 1 if sick
            
        Returns:
            tuple: (prediction, probability) where prediction is 1/0 and probability is float
        """
        if not self.is_trained:
            print("Model is not trained yet!")
            return None, None
        
        # Prepare input data as DataFrame with correct column names
        input_data = pd.DataFrame({
            'past_attendance': [past_attendance],
            'classes_missed': [classes_missed],
            'is_sick': [is_sick]
        })
        
        # Make prediction
        prediction = self.model.predict(input_data)[0]
        
        # Get probability of attending (class 1)
        probability = self.model.predict_proba(input_data)[0][1]
        
        return prediction, probability
    
    def get_prediction_label(self, prediction):
        """Convert prediction to readable label with emoji"""
        if prediction == 1:
            return "Will Attend ✅"
        else:
            return "Will Not Attend ❌"
