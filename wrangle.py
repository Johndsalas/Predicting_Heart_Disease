'''Code for wrangling heart disease data'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler


def get_my_data():

    # readin data
    df = pd.read_csv('heart_disease_2020.csv')

    # rename columns
    df = df.rename(columns={'HeartDisease':'heart_disease', 
                            'BMI':'bmi', 
                            'Smoking':'smoker', 
                            'AlcoholDrinking':'heavy_drinker',
                            'Stroke':'stroke',
                            'PhysicalHealth':'poor_physical_health_days', 
                            'MentalHealth':'poor_mental_health_days', 
                            'DiffWalking': 'difficulty_walking', 
                            'Sex':'sex', 
                            'AgeCategory':'age_category',
                            'Race':'race', 
                            'Diabetic':'diabetic', 
                            'PhysicalActivity':'physical_activity', 
                            'GenHealth':'general_health', 
                            'SleepTime':'sleep_hours',
                            'Asthma':'asthma', 
                            'KidneyDisease':'kidney_disease', 
                            'SkinCancer':'skin_cancer'})

    # get dummie variables for actegorical columns
    df = get_my_dummies(df)

    # split data into train, validate, and test
    train, validate, test = split_my_data(df)

    # scale numeric columns
    train, validate, test = scale_my_data(train, validate, test)

    return train, validate, test


def get_my_dummies(df):

    cat_cols = ['heart_disease',
                'smoker',
                'heavy_drinker',
                'difficulty_walking',
                'diabetic',
                'physical_activity',
                'kidney_disease',
                'skin_cancer',
                'age_category',
                'general_health']

    dummies = pd.get_dummies(df[cat_cols])

    return df.join(dummies)


def split_my_data(df):

    '''Splits data and returns a train, validate, and test dataframe'''

    # split df into train_validate and test
    train_validate, test = train_test_split(df, 
                                            test_size=.2, 
                                            random_state=123, 
                                            stratify=df.heart_disease)

    # split train_validate into train and validate
    train, validate =  train_test_split(train_validate, 
                                        test_size=.2, 
                                        random_state=123, 
                                        stratify=train_validate.heart_disease)

    # reset index for train validate and test
    train.reset_index(drop=True, inplace=True)
    validate.reset_index(drop=True, inplace=True)
    test.reset_index(drop=True, inplace=True)

    return train, validate, test


def scale_my_data(train, validate, test):
    "Adds scaled columns to split data"

    # Scaling continuous variables
    cols_to_scale = ['bmi',
                     'sleep_hours',
                     'poor_physical_health_days',
                     'poor_mental_health_days']

    # create df's for train validate and test with only columns that need to be scaled
    train_to_be_scaled = train[cols_to_scale]
    validate_to_be_scaled = validate[cols_to_scale]
    test_to_be_scaled = test[cols_to_scale]

    # create scaler object and fit that object on the train data
    scaler = RobustScaler().fit(train_to_be_scaled)

    # transform data into an array using the scaler object 
    train_scaled = scaler.transform(train_to_be_scaled)
    validate_scaled = scaler.transform(validate_to_be_scaled)
    test_scaled = scaler.transform(test_to_be_scaled)

    # transform data into a dataframe
    train_scaled = pd.DataFrame(train_scaled, columns = cols_to_scale)
    validate_scaled = pd.DataFrame(validate_scaled, columns = cols_to_scale)
    test_scaled = pd.DataFrame(test_scaled, columns = cols_to_scale)

    # add _scaled to each column name in the scaled data
    for col in cols_to_scale:

        train_scaled = train_scaled.rename(columns={col: col + "_scaled"})
        validate_scaled = validate_scaled.rename(columns={col: col + "_scaled"})
        test_scaled = test_scaled.rename(columns={col: col + "_scaled"})

    # add scaled columns to their original dataframes
    train = train.join(train_scaled)
    validate = validate.join(validate_scaled)
    test = test.join(test_scaled)

    return train, validate, test