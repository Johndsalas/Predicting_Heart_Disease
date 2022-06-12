'''This is a utility file for holding high use functions used for getting to an MVP during the data science process'''

#*******************These are functions used for cleaning outliers from data using the inner quartile rule*************************

def get_outlier_cutoffs(df, col_list, k=3):
    ''' Input a dataframe, list of columns for that dataframe, and k value 
        Prints the median, upper bound, and lower bound cut off values for each column in the column list using the inner-quartile rule
    '''
    for col in col_list:

        q1, q2, q3 = df[f'{col}'].quantile([.25, .5, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # print each col and upper and lower bound for each column
        print(f"{col}: Median = {q2} upper_bound = {upper_bound} lower_bound = {lower_bound}")


def get_upper_and_lower_bound(df, col_list, k=3):
    '''Input a dataframe, list of columns for that dataframe, and k value 
       Returns the lower bound, and upper bound cut off values for each column in the column list using the inner-quartile rule'''

    for col in col_list:

        q1, q2, q3 = df[f'{col}'].quantile([.25, .5, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound
        
    return upper_bound, lower_bound


def remove_outliers(df, col_list, k=3):
    '''Input a dataframe, list of columns for that dataframe, and k value
       Returns a dataframe with outliers removed using the inner quartile rule
       Dependant function: get_upper_and_lower_bound '''

    # itterate through cols in col_list
    for col in col_list:

        # get upper and lower bound using inner quartile rule
        upper_bound, lower_bound = get_upper_and_lower_bound(df, col_list)

        # add is_outlier column to df
        df[f'{col}_is_outlier'] = (df[{col}] > upper_bound) | (df[{col}] < lower_bound)

    # itterate through cols 
    for col in col_list:

        # drop outliers
        df = df[df[f'{col}_is_outlier'] == False] 

        # drop is_outlier column
        df = df.drop(columns = f'{col}_is_outlier') 
        
    return df