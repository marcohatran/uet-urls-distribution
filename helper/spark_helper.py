from pyspark.sql import SparkSession

# using SQLContext to read parquet file
from pyspark.sql import SQLContext

from state.SparkState import SparkState


def load_parquet_by_spark(spark, sc, parquet_file_path):
    spark, sc = SparkState.getSparkContext()
    sqlContext = SQLContext(sc)
    # to read parquet file
    df = sqlContext.read.parquet(parquet_file_path)
    # df = spark.read.parquet('swift://' + parquet_file_path)
    return df
