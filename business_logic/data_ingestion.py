
from pyspark.sql import SparkSession

def load_data(input_path):
    spark = SparkSession.builder.appName('Sanuis Health Assesment').getOrCreate()
    df = spark.read.csv(input_path, header=True)
    df = df.limit(15000)
    return df
