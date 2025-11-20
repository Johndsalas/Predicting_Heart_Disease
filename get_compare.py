''' Contains code for first look examination of how variables relate to the target variable'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart_2022.csv')
target_column = "HadHeartAttack"
target_value = "Yes"

### seperate categorical and continuous columns
def main(df, target_column, target_value):
    '''Takes in dataframe and target column and target value in that column as strings 
    Prints preliminary charts comparing the other columns in that data frame to the value in the target column'''
    
    num_li, cat_li, o_li = sep_data_types(df,target_column)

    print(f'continuous columns: {num_li}')
    print()
    print(f'categorical columns: {cat_li}')
    print()
    print(f'other columns: {o_li}')
    print()

    print('******************************************************************************')

    cat_compare(df, target_column, target_value, cat_li)

    num_compare(df, target_column, target_value, num_li)

    
def sep_data_types(df, target_column):
    '''Takes in a dataframe and returns two lists
       one with the continuous columns and one with the cotegorical columns'''

    num_li =[]
    cat_li = []
    o_li = []

    for col in df.columns:

        if col == target_column:

            o_li.append(col)

        elif df[f'{col}'].dtype == 'float64' :

            num_li.append(col)

        elif df[f'{col}'].dtype == 'O':

            cat_li.append(col)

        else:

            o_li.append(col)


    return num_li, cat_li, o_li


def cat_compare(df, target_column, target_value, cat_li):
    '''Print chart showing percent of each category that matches the target value in the target column'''

    # for each column
    for col in cat_li:

        # get values in column
        vals = list(set(df[col].to_list()))
        hights = []

        # get total number of rows where value in target column matches target value
        tot_val = len(df[df[target_column] == target_value])

        # get total number of rows in the dataframe
        tot_rows = len(df)

        # get overall percent of target variable
        overall = round(tot_val/tot_rows,2)*100

        # for each value in the column 
        for val in vals:
        
            # get the number of rows matching the value in the current collumn and the target value in the target column
            num_val_target = len(df[(df[col] == val) & (df[f'{target_column}'] == f'{target_value}')])

            # get number of rows matching the value in the current column
            num_val = len(df[df[col] == val])

            print(col, val, f'Number matching target vale: {num_val_target}', f'Tota: {num_val}')

            # get percent of rows matching value in the current column that also match the target variable in the target column
            percent = round((num_val_target/num_val),2)*100
            
            hights.append(percent)

        # Combine categories and values into a list of tuples
        data = list(zip(vals, hights))

        # Sort the data by values in descending order
        data.sort(key=lambda x: x[1], reverse=True)

        # Unzip the sorted data back into separate lists
        vals, hights = zip(*data)

        vals = list(vals)
        hights = list(hights)

        vals.insert(0,'Overall')
        hights.insert(0, overall)

        plt.figure(figsize=(16,6))
        plt.bar(vals, hights)
        plt.title(f'{target_value} percentage for {col}')
        plt.show()

        print('******************************************************************************')

def num_compare(df, target_column, target_value, num_li):
    '''Prints bar chart with 
       Overall mean for column 
       Mean for rows where the value in the target column matches the target value
       Mean for rows where the value in the target column does not match the target value'''
    
    # for each column
    for col in num_li:

        # mean of all rows
        mean = df[col].mean()

        # mean of all rows matching the target value in the target column 
        target_mean = df[col][df[f'{target_column}'] == target_value].mean()

        # mean of all rows not matching the target value in the target column
        non_target_mean = df[col][df[f'{target_column}'] != target_value].mean()
        
        # get labels and hights of bars for graph
        x = [f'All_Mean {round(mean)}', f'{target_value}_Mean {round(target_mean)}', f'Non-{target_value}_Mean {round(non_target_mean)}']
        hight = [mean, target_mean, non_target_mean]
        
        # print graph
        plt.figure(figsize=(16,6))
        plt.bar(x, hight)
        plt.title(f'avg {col}')
        plt.show()

        print('******************************************************************************')
if __name__ == "__main__":

    main(df, target_column, target_value)


def get_chart(df,col,target_column,target_value,title):
    

     # get values in column
        vals = list(set(df[col].to_list()))
        hights = []

        # get total number of rows where value in target column matches target value
        tot_val = len(df[df[target_column] == target_value])

        # get total number of rows in the dataframe
        tot_rows = len(df)

        # get overall percent of target variable
        overall = round(tot_val/tot_rows,2)*100

        # for each value in the column 
        for val in vals:
        
            # get the number of rows matching the value in the current collumn and the target value in the target column
            num_val_target = len(df[(df[col] == val) & (df[f'{target_column}'] == f'{target_value}')])

            # get number of rows matching the value in the current column
            num_val = len(df[df[col] == val])

            # get percent of rows matching value in the current column that also match the target variable in the target column
            percent = round((num_val_target/num_val),2)*100
            
            hights.append(percent)

        # Combine categories and values into a list of tuples
        data = list(zip(vals, hights))

        # Sort the data by values in descending order
        data.sort(key=lambda x: x[1], reverse=True)

        # Unzip the sorted data back into separate lists
        vals, hights = zip(*data)

        plt.figure(figsize=(16,6))
        plt.bar(vals, hights)
        plt.title(f'{title}')
        plt.show()
