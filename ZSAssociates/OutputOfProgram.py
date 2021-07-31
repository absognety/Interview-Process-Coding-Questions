import pandas as pd
from pyspark import SparkContext
from pyspark.sql.functions import col,struct,pandas_udf,PandasUDFType
from pyspark.sql import SQLContext
sc = SparkContext("local","test")
x = pd.Series([1,2,3])
pdf = pd.DataFrame([1,2,3],columns = ['x'])
df = SQLContext(sc).createDataFrame(pdf)

@pandas_udf("long",PandasUDFType.SCALAR_ITER)
def plus_one(batch_iter):
    for x in batch_iter:
        yield x + 1
        
@pandas_udf("long",PandasUDFType.SCALAR_ITER)
def multiply_two_cols(batch_iter):
    for a,b in batch_iter:
        yield a * b
        
df.select(multiply_two_cols(col("x"),col("x"))).show()