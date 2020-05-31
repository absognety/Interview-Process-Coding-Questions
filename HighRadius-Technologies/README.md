## Interview questions (Personal Experience):  

#### 1. Confusion matrix for any classification algorithm is showed and what are precision and recall values from the matrix?  
  
+ **What is precision**: `Number of True Positives / (Total number of Total Positives and False Positives)`  
+ **What is Recall** : `Number of True Positives / (Total Number of Total Positives and False Negatives)`  

#### 2. How do you deal with overfitting in your machine learning model?  
  
+ Regularization - (LASSO or Ridge Regression) (L1 and L2 regularization).  
+ K-Fold cross validation with variable K.  
+ Resampling of Train and Test splits of a datasets, sometimes involve out-of-time validation dataset.  
+ Dimensionality Reduction in case of many features in a dataset.  
+ Ensemble Learning.  

#### 3. How do you explain p-value to a layman? - Hypothesis testing.  

+ p-value is metric by which we decide statistically significant variables.  
+ It's a measure of how extreme an observed value is under the assumed null hypothesis: the smaller it is, the more extreme the 
observation. We can define p-value as the smallest significance level at which the null hypothesis would be rejected.  
+ As the p-value gets smaller, we start wondering if the null hypothesis really is true and well maybe we should change our minds 
(and reject the null hypothesis).  

#### 4. How do you deal with concurrent predictions from decision Trees in ensemble algorithms like random forest?
+ Do some google research on this, there are multiple techniques to deal with this.
