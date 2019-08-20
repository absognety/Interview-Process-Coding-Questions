## Questions on SQL:  

1. Let's say there is a table called Completed_Trips. The fields present in the table are `rider_id`,`trip_id` and `trip_date`.Assume there are `X` riders in week 1 and Y riders in immediate following week 2. Retention is defined as ratio of common riders between `X` and `Y` who took atleast 1 trip and number of riders in week 1 who took atleast 1 trip i.e `X`

**Output:** Plot the retentions for last n weeks -> n is an input here.  
**Solution:**  
```
#n = number of weeks

n = int(input()) #n = 4 or 5 or .....

i = 0

j = 1

#Assume df is the parent data frame which is completed_trips

retentions = []

#we can use datetime module to compare dates.

while (i <= n-1 and j <= n):

    df1 = df[df['trip_date'] < curr_date - 7*i and df['trip_date'] > curr_date - 7*j]

    df2 = df[df['trip_date'] < curr_date - 7*(i+1) and df['trip_date'] > curr_date - 7*(j+1)]

    df1 = df1[df1['trip_id'].notnull()]

    df2 = df2[df2['trip_id'].notnull()]

    count_df1 = set(df1['rider_id'].values) #set gives distinct values

    count_df2 = set(df2['rider_id'].values)
    
    numerator = len(count_df1 & count_df2) #gives the common riders among all riders

    denominator = len(count_df2)

    retentions.append(numerator/denominator)

    i += 1

    j += 1

   
#If n = 4
#0<=3 and 1<=4

#1<=3 and 2<=4

#2<=3 and 3<=4

#3<=3 and 4<=4 ----------> total 4 times the loop will repeat so we get 4 retentions.

weeks_var = ["week" + "-" + str(i) for i in range(1,5)]

final_data = pd.DataFrame({"Week":weeks_var,"Retention":retentions},
                          columns = ['Week','Retention'])
                          
#final_data is ready - we can do line charts, trend charts etc in it.

```

## Logical Question:  
  
2. What are the 3 important metrics that you consider to be important to evaluate people who are reporting to you and why?  
   + Correctness of Solution Deivered'
   + Quality of Solution Delivered
   + Adaptability of Solutions Delivered.  
You can form your own answers here.  


## Process Flow Question:  
  
3. What are the steps involved in the process doing the FTP for file of any format and putting it in hive location.  
   + Step-1: Check the location and access  
   + Step-2: Check the format of file as hive only supports csv/delimited files.  
   + Step-3: if it is not csv or delimited then try to convert it into structured data set.  
   + Step-4: Transfer the file using scp protocol binding in python (pysftp) or linux shell.  
   + Step-5: Once the file is in respective folder, create a hive table with location inserted in table definition with csv serializer.  


