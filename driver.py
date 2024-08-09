
import pyspark as ps

if __name__ == "__main__":
    print("Hello World!")

    spark = ps.sql.SparkSession.builder.appName("Test").master("local[*]").getOrCreate()

    df = spark.range(1,1000)

    df.show()


