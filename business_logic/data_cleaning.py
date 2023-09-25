# Code for specific operations
def clean_data(df):
    df_cleaned = df.na.drop()
    return df_cleaned
