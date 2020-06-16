# Personal Experience (Interview Process for AI/Machine Learning Engineer - 2020):  
### First screening round:  
+ Interview with the Director of AI teams:  

Case study: Dataset is as below:  
  
| itemId | item_name | item_description      | manufacturer_name | supplier_name | target_variable(home/workplace) |
|--------|-----------|-----------------------|-------------------|---------------|---------------------------------|
| 1000   | monitor   | ram: 32gb,2.8 GHZ,HDD | HP                | senty pvt ltd | workstation                     |
| 1001   |           |                       |                   |               |                                 |
| 1003   |           |                       |                   |               |                                 |  

Given only sample size of 10 of above schema (with target variable assigned), training dataset(without target_variable assigned) size is 100, how would you avoid the effort of manual tagging  of target variable to training data?  
#### Follow up questions:  
+ How would you select the variables?
+ How would u use the opentext column `item_description`?

The round is for just 10 minutes, and I didn't get selected.

#### My solution:  
+ k-NN/decision tree algorithm for dependent variable tagging (even associaton rule mining algorithms that include apriori and eclat).  
+ initial selection of variables is based on domain knowledge as number of variables is very less here.
+ preprocess the text column `item_description` maybe do text summarization of the full text and extract keywords using bi-grams and collocations and use that tag in further processing.  


## Use https://www.tablesgenerator.com/markdown_tables# for quick tables generation in markdown, It's elegant and simple.  
