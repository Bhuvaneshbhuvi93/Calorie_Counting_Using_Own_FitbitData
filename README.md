# Calorie Counting Model

## Introduction

For this project, I have worked on developing a machine learning model that predicts the number of calories burned by a person based on their steps taken, active minutes, and distance traveled. The model has been trained on real-life fitness data, and it has given us impressive results in terms of accuracy. This project has been a great learning experience, and I'm thrilled to share it with my professional network.

I have used Python libraries such as NumPy, Pandas, and scikit-learn to build and train the model. I have also used Streamlit, a web app framework, to create an interactive interface that makes it easy for people to use the model and see their calorie predictions. The final product is a user-friendly and interactive tool that can help people keep track of their fitness goals and make healthier choices.

I hope this project showcases my skills and knowledge in machine learning, data science, and web development. I look forward to connecting with like-minded professionals and exploring new opportunities in these fields.

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

## Demo Video


https://user-images.githubusercontent.com/118096816/216385003-f1bec2a9-2f81-4633-af49-8452dd778308.mp4


## Future Work
- The model can be improved by incorporating additional data such as heart rate, sleep data and etc.
- The model can be trained on a larger dataset to improve its accuracy.
- The model could be deployed as a web app or mobile app to make it more accessible to users.
