# House-prices-prediction

# Project Title

This project aims at predicting house prices (residential) in Pune in different locations.

## Process of Machine Learning Predictions

Making predictions using Machine Learning isn't just about grabbing the data and feeding it to algorithms. The algorithm might spit out some prediction but that's not what you are aiming for. The process is as follows: 

## 1.Understand the problem: 
Before getting the data, we need to understand the problem we are trying to solve. If you know the domain, think of which factors could play an epic role in solving the problem. If you don't know the domain, read about it.
## 2. Hypothesis Generation: 
This is quite important, yet it is often forgotten. In simple words, hypothesis generation refers to creating a set of features which could influence the target variable given a confidence interval ( taken as 95% all the time). We can do this before looking at the data to avoid biased thoughts. This step often helps in creating new features.
## 3. Get Data: 
Now, we download the data and look at it. Determine which features are available and which aren't, how many features we generated in hypothesis generation hit the mark, and which ones could be created. Answering these questions will set us on the right track. 
## 4. Data Exploration: 
We can't determine everything by just looking at the data. We need to dig deeper. This step helps us understand the nature of variables (skewed, missing, zero variance feature) so that they can be treated properly. It involves creating charts, graphs (univariate and bivariate analysis), and cross-tables to understand the behavior of features. 
## 5.Data Preprocessing: 
 Here, we impute missing values and clean string variables (remove space, irregular tabs, data time format) and anything that shouldn't be there. This step is usually followed along with the data exploration stage. 
 ## 6. Feature Engineering: 
 Now, we create and add new features to the data set. Most of the ideas for these features come during the hypothesis generation stage. 7. Model Training: Using a suitable algorithm, we train the model on the given data set. 
 ## 7. Model Training: 
 Using a suitable algorithm ,multiple linear regression,decision tree,random forest etc. we train the model on the given data set. 
 ## 8. Model Evaluation: 
 Once the model is trained, we evaluate the model's performance using a suitable error metric. Here, we also look for variable importance, i.e., which variables have proved to be significant in determining the target variable. And, accordingly we can shortlist the best variables and train the model again. 
 ## 9. Model Testing: 
 Finally, we test the model on the unseen data (test data) set.

### Prerequisites

Need to install the software

```
Software- Anaconda,jupyter
packages- sklearn,pandas,numpy,flask,matplotlib,seaborn etc.
See requirement.text for further
```





## Deployment
 ```
The web framework used - Flask 
 Use the Heroku platform for deploy the app.
```


