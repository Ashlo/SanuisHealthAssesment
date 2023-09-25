from pyspark.sql import functions as F

def heart_rate_kpi(df):
    # Calculate AVG heart_rate
    heart_rate = df.select('heart_rate').agg(F.avg('heart_rate'))
    activity_per_heart_rate = df.groupBy('activityID').agg(F.avg('heart_rate'))
    return activity_per_heart_rate

def temp_variability(df):
    variability_in_temp=df.groupBy('activityID').agg(F.stddev('hand temperature (°C)'), F.stddev('chest temperature (°C)'), F.stddev('ankle temperature (°C)'))
    return variability_in_temp

def act_intensity(df):
    try:
        df = df.withColumn('hand_intensity',F.sqrt(F.col('hand acceleration X ±16g') ** 2 + F.col('hand acceleration Y ±16g') ** 2+ F.col('hand acceleration X ±16g') ** 2))
        df = df.withColumn('chest_intensity',F.sqrt(F.col('chest acceleration X ±16g') ** 2 + F.col('chest acceleration Y ±16g') ** 2+ F.col('chest acceleration X ±16g') ** 2))
        df = df.withColumn('ankle_intensity',F.sqrt(F.col('ankle acceleration X ±16g') ** 2 + F.col('ankle acceleration Y ±16g') ** 2+ F.col('ankle acceleration X ±16g') ** 2))
        avg = df.groupBy('activityID').agg(F.avg('hand_intensity'),F.avg('chest_intensity'),F.avg('ankle_intensity'))
        return avg
    except Exception as e:
        print(e)

