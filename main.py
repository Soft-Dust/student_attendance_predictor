"""
Student Attendance Predictor - Main Program
Handles user input and runs the attendance prediction system
"""

from model import AttendancePredictor

def get_user_input():
    """Get student information from user"""
    print("\n" + "="*50)
    print("STUDENT ATTENDANCE PREDICTOR")
    print("="*50)
    
    try:
        # Get attendance percentage
        past_attendance = float(input("Enter attendance percentage (0-100): "))
        if past_attendance < 0 or past_attendance > 100:
            print("Attendance must be between 0 and 100!")
            return None
        
        # Get classes missed
        classes_missed = int(input("Enter classes missed last week (0-7): "))
        if classes_missed < 0 or classes_missed > 7:
            print("Classes missed must be between 0 and 7!")
            return None
        
        # Get sick status
        is_sick = int(input("Is student sick? (0=No, 1=Yes): "))
        if is_sick not in [0, 1]:
            print("Sick status must be 0 or 1!")
            return None
        
        return past_attendance, classes_missed, is_sick
        
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return None

def main():
    """Main program function"""
    print("Initializing Student Attendance Predictor...")
    
    # Create and train the model
    predictor = AttendancePredictor()
    predictor.train()
    
    # Get user input and make prediction
    user_data = get_user_input()
    
    if user_data:
        past_attendance, classes_missed, is_sick = user_data
        
        print("\n" + "-"*30)
        print("PREDICTION RESULT")
        print("-"*30)
        
        # Make prediction
        prediction, probability = predictor.predict(past_attendance, classes_missed, is_sick)
        result = predictor.get_prediction_label(prediction)
        
        print(f"Prediction: {result}")
        print(f"Probability of Attending: {probability:.2f}")
        print(f"Model Accuracy: {predictor.accuracy:.1%}")
        
        # Show input summary
        print("\nInput Summary:")
        print(f"  Attendance: {past_attendance}%")
        print(f"  Classes Missed: {classes_missed}")
        print(f"  Sick Status: {'Yes' if is_sick == 1 else 'No'}")
    
    print("\n" + "="*50)
    print("Thank you for using Student Attendance Predictor!")
    print("="*50)

if __name__ == "__main__":
    main()
