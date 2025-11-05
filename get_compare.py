''' Contains code for first look examination of how variables relate to the target variable'''

import pandas as pd

df = pd.read_csv('heart_2022.csv')

### seperate categorical and continuous columns
def main():

    num_li, cat_li = sep_data_types(df)

    print(num_li)

def sep_data_types(df):
    '''Takes in a dataframe and returns two lists
       one with the continuous columns and one with the cotegorical columns'''

    num_li =[]
    cat_li = []

    for col in df.columns:

        if df[f'{col}'].dtype == 'float64' :

            num_li.append(col)

        if df[f'{col}'].dtype == 'O':

            cat_li.append(col)

    return num_li, cat_li


### compare to catagory

# get category values










main()