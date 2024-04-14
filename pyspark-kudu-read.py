from pyspark.sql import *
from pyspark.sql.types import LongType
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder.appName("KuduInsertExample").getOrCreate()

# Kudu 마스터 주소 설정
kudu_master = "localhost:7051"

# Kudu 테이블 이름 설정
kudu_table = "impala::default.my_kudu_table"

# Kudu 데이터 읽기
df = (
    spark.read.format("kudu")
    .option("kudu.master", kudu_master)
    .option("kudu.table", kudu_table)
    .load()
)

df.show()

# SparkSession 종료
spark.stop()
