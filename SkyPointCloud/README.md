# Interview process for skypoint cloud (Data engineer):  
1. **Hackerearth Test**: objective questions on hadoop, spark, python and airflow basics and one coding question added above.  
2. **First round of Interview**:  
   - Questions:  
     - what is the difference between mapreduce and spark?  
     - What is the difference between Spark coalesce and repartition?  
     - How do you handle out of memory error in spark application execution?  
     - How does pyspark work?  
     - Can you explain how you solved the programming question you have solved in the test? (refer [here](https://github.com/absognety/Interview-Process-Coding-Questions/blob/master/SkyPointCloud/modifyString.py))  
3. **Second round of Interview**:  
   - Questions:
     - what are the challenges you encountered in your projects and how did you solve them?
     - **Case Study**:  
       - Let's say there are 3 data sources(RDBMS), First Data source contains (firstname,lastname,email and gender), second one contains (firstname,lastname,order_history) and third contains (email,profile_id). How can you construct a 360 degrees view of a customer that contains all information from 3 data sources containing (firstname,lastname,email,gender,order_history and profile_id) but without traditional way of joining the columns (looking for more of ML based solution)(Hint: the columns may contain special characters, spaces, underscores etc)
     - What are list comprehensions and dictionary comprehensions in python.  
     - Tell me one approach on finding all prime numbers in the given range?  
     - Can you code up a binary search algorithm in array that is sorted in descending order? (refer [here](https://github.com/absognety/Interview-Process-Coding-Questions/blob/master/SkyPointCloud/binarySearch.py))  
     - How do you define/create a class in python?  
