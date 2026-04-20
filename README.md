# Student Attendance Predictor

A simple machine learning project that predicts whether a student will attend the next class based on their attendance history and current status.

## Project Overview

This project uses Logistic Regression to predict student attendance (Yes/No) based on three features:
- **past_attendance**: Student's overall attendance percentage
- **classes_missed**: Number of classes missed in the last week
- **is_sick**: Whether the student is currently sick (0=No, 1=Yes)

## Project Structure

```
student_attendance_prediction/
├── main.py              # Main program - handles user input and runs everything
├── model.py             # Machine learning model training and prediction
├── data.py              # Dataset containing student attendance data
├── requirements.txt     # Required Python packages
├── run_project.bat     # Windows batch file to setup and run the project
└── README.md           # This file
```

## Setup Instructions

### Method 1: Using the Batch File (Recommended for Windows)

1. Double-click `run_project.bat`
2. The script will automatically:
   - Create a virtual environment
   - Install required packages
   - Run the program

### Method 2: Manual Setup

1. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Program:**
   ```bash
   python main.py
   ```

## How It Works

1. **Data Loading**: The program loads a small dataset of 20 student records from `data.py`
2. **Model Training**: Uses Logistic Regression to train on the dataset
3. **Accuracy Calculation**: Splits data (70% train, 30% test) and calculates model accuracy
4. **User Input**: Prompts user for student information
5. **Prediction**: Uses the trained model to predict attendance
6. **Result Display**: Shows "Will Attend" or "Will Not Attend"

## Sample Output

```
Initializing Student Attendance Predictor...
Model trained successfully!
Model Accuracy: 0.83

==================================================
STUDENT ATTENDANCE PREDICTOR
==================================================
Enter attendance percentage (0-100): 85
Enter classes missed last week (0-7): 1
Is student sick? (0=No, 1=Yes): 0

------------------------------
PREDICTION RESULT
------------------------------
Prediction: Will Attend
Confidence: Based on model accuracy of 0.83

Input Summary:
  Attendance: 85.0%
  Classes Missed: 1
  Sick Status: No

==================================================
Thank you for using Student Attendance Predictor!
==================================================
```

## Technical Details

- **Algorithm**: Logistic Regression
- **Features**: 3 (attendance %, classes missed, sick status)
- **Dataset Size**: 20 records
- **Test Split**: 30% for testing, 70% for training
- **Accuracy**: Typically 80-90% on this small dataset

## Requirements

- Python 3.7 or higher
- scikit-learn 1.3.0
- pandas 2.0.3

## Project Features

✅ Simple and clean code structure  
✅ Beginner-friendly with clear comments  
✅ No overcomplicated features  
✅ Professional mini-project appearance  
✅ Easy to explain in presentations/viva  
✅ Works out of the box with single click  

## Limitations

- Small dataset (20 records) for demonstration purposes
- Single model (Logistic Regression only)
- No advanced ML features (scaling, cross-validation, etc.)
- Binary classification only (Yes/No prediction)

## Perfect For

- Machine learning beginners
- Class projects and assignments
- Portfolio demonstration
- Learning basic ML concepts
- Viva presentations
