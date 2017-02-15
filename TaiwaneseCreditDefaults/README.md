# Taiwanese Credit Defaults

From the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).

From this research paper:  
Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480.

>This research aimed at the case of customer default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients. Because the real probability of default is unknown, this study presented the novel Sorting Smoothing Method to estimate the real probability of default. With the real probability of default as the response variable (Y), and the predictive probability of default as the independent variable (X), the simple linear regression result (Y = A + BX) shows that the forecasting model produced by artificial neural network has the highest coefficient of determination; its regression intercept (A) is close to zero, and regression coefficient (B) to one. Therefore, among the six data mining techniques, artificial neural network is the only one that can accurately estimate the real probability of default.
****
# Can I build a better model?
****
Data Description:  
X1: Amount of the given credit (TWD); includes individual consumer credit and family (supplementary) credit.  
X2: Gender (1 = male; 2 = female).  
X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others).  
X4: Marital status (1 = married; 2 = single; 3 = others).  
X5: Age (years).  

Past Payment History (April - September 2005):  
* X6 = the repayment status in September 2005  
* X7 = the repayment status in August 2005  
* X8 = the repayment status in July 2005  
* X9 = the repayment status in June 2005  
* X10 = the repayment status in May 2005     
* X11 = the repayment status in April 2005. 
    
The measurement scale for the repayment status is:  
* -1 = paid on time  
* 1 = payment delay for one month  
* 2 = payment delay for two months  
* 3 = payment delay for two months  
* 4 = payment delay for two months  
* 5 = payment delay for two months  
* 6 = payment delay for two months  
* 7 = payment delay for two months  
* 8 = payment delay for eight months  
* 9 = payment delay for nine or more months  
         
X12-X17: Amount of bill statement (TWD). 
* X12 = amount of bill statement in September 2005  
* X13 = amount of bill statement in August 2005  
* X14 = amount of bill statement in July 2005  
* X15 = amount of bill statement in June 2005  
* X16 = amount of bill statement in May 2005  
* X17 = amount of bill statement in April 2005  

X18-X23: Amount of previous payment (TWD). 
* X18 = amount paid in September 2005  
* X19 = amount paid in August 2005  
* X20 = amount paid in July 2005  
* X21 = amount paid in June 2005  
* X22 = amount paid in May 2005  
* X23 = amount paid in April 2005  
****