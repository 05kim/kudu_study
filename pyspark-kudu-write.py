from pyspark.sql import *
from pyspark.sql.types import LongType
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder.appName("KuduInsertExample").getOrCreate()

# Kudu 마스터 주소 설정
kudu_master = "localhost:7051"

# 삽입할 데이터 생성
data = [
    (1, "John Doe", 33),
    (2, "Jane Smith", 25),
    (3, "Mike Johnson", 35),
    (4, "hello hello", 40),
]

# 데이터프레임 생성
df = spark.createDataFrame(data, ["id", "name", "age"])

# Kudu 테이블 이름 설정
kudu_table = "impala::default.my_kudu_table"

# Kudu에 데이터 쓰기
df.write.format("org.apache.kudu.spark.kudu").option("kudu.master", kudu_master).option(
    "kudu.table", kudu_table
).mode("append").save()

# SparkSession 종료
spark.stop()
