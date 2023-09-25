
# Feature engineering operations
def add_features(df):
    # Feature engineering logic here
    df_with_features = df.withColumn('new_feature', df['some_column'] * 2)
    return df_with_features
