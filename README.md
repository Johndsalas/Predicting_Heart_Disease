# Predicting_Heart_Disease
Analyzing Personal Key Indicators of Heart Disease Using Data from Kaggle

## Project Description and Goal

According to the CDC website Heart disease is the leading cause of death in america in this project I will be examining personal key indicators of Heart disease with the goal of identifying the top drivers of heart disease and creating a predictive algorithm to determine an individual's risk level based on those drivers. This information can be used to help manage ones personal risk by identifying lifestyle choices and other health related indicators of heart disease. 

## Data Dictionary
| Feature | Definition |
|:--------|:-----------|
| has_heart_disease (Target) | Respondent reported having had coronary heart disease or myocardial infarction |
| bmi | Body Mass Index reported by respondent|
| is_smoker | Respondent reported having smoked at least 100 cigarettes in their lifetime |
| heavy_drinker | Respondent reported being an adult man having more than 14 drinks per week or an adult women having more than 7 drinks per week) |
| stroke | Respondent reported having had a stroke |
| poor_physical_health_days | Number of days in the last 30 where respondent reported physical health as not good | 
| poor_mental_health_days | Number of days in the last 30 where respondent reported mental health as not good |
| has_difficulty_walking | Respondent has difficulty walking or climbing stairs |
| sex | Respontent’s sex identified as male or female |
| age_category | Respondent's reported age categorized by 5 year intervals |
| race | race/ethnicity reported by respondent |
| diabetic | Respondent reported having had diabetes |
| physical_activity | Respondent reported doing physical activity in the past 30 days outside of their regular job | 
| general_health | Category of general health reported by respondent|
| sleep_time | The average number of hours the respondent reports sleeping each night |
| asthma | Respondent reported having had asthma |
| kidney_disease | Respondent reported having kidney disease |
| skin_cancer | Respondent reported having skin cancer | 

## Project Planning

### Acquire

* Download csv from Kaggle
* Read csv into pandas dataframe in notebook

### Prepare

* Look for nulls and manage them
* Insure that features are correct data types
* Look for outliers and manage them
* Create dummies of categorical variables 
* Split data into train, validate, amd test
* Create scaled versions of continuous variables

### Explore

* Take an initial look at how each feature relates to heart attack and weed out features that show no relationship with heart disease 

* Formulate questions to ask of the data
* Answer questions using visuals and Statistical testing as needed
* Summarize findings in explore and decide which features I will be modeling on

### Modeling

* Develop a number of models to predict heart disease based on the chosen features.
* Evaluate those models on train and validate, choosing the best model 
* Evaluate the best model on test as indication of how the model will perform on test data

### Conclusion

* Summarize findings in explore and model performance
* Formulate recommendations
* Discuss additional steps that could be added to the project in the future

## Steps to Reproduce

* Clone this repo
* Download the csv containing the dataset from Kaggle
* Put CSV into the repo file
* Run notebook
