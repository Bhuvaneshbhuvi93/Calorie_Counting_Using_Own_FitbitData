# Calorie Counting Model

## Introduction

This project aims to create a calorie detection model using data from a Fitbit device. The model uses linear regression to predict the number of calories burned based on the number of steps taken, the active minutes, and the distance traveled.

## Data

The data used in this project is personal Fitbit data. The data includes the following columns:

- Steps
- Active Minutes
- Distance
- Calories Burned

## Analysis

To find the relationship between the variables, the following analyses were performed:

- Relationship between Total Activity & Total Calories Burnt
- Relationship between Steps & Total Calories Burnt
- Relationship between Distance & Total Calories Burnt

The results of the analysis showed that there is a strong positive correlation between the number of steps taken, active minutes, and distance traveled with the number of calories burned.

## Model

The calorie detection model was created using the scikit-learn library's LinearRegression class. The model was trained on 80% of the data, and the remaining 20% was used for testing. The model achieved a score of 0.9654 on the test set.

## Usage

To use the model, simply run the following code:

```
print("Calorie Prediction")
a=int(input("Steps Taken: "))
b=int(input("Active Minutes: "))
c=float(input("Distacne: "))

features = np.array([[a, b,c]])
print("Calorie Burned = ",model.predict(features))
```
## Methods
The data is preprocessed to clean and prepare it for analysis. The relationships between the different features and the target variable (calories burnt) are then analyzed. Three different models were trained using linear regression and the model with the highest R-squared value was selected as the final model.

## Results
The final model had an R-squared value of 0.9654, indicating a strong correlation between the features and the target variable. The model was able to accurately predict the number of calories burnt based on the user's activity data.

## Usage
The model can be used to predict the number of calories burnt by inputting the user's activity data (steps taken, active minutes, and distance traveled). The user can then use this information to make informed decisions about their physical activity and calorie intake.

## Future Work
- The model can be improved by incorporating additional data such as heart rate, sleep data and etc.
- The model can be trained on a larger dataset to improve its accuracy.
- The model could be deployed as a web app or mobile app to make it more accessible to users.
