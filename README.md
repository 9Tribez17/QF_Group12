**This is QF5214 project of GROUP 12 Bank Customer Churn Prediction**

***1. Problem Stataement***

In the dynamic landscape of the financial sector, a critical challenge faced by banks
is the retention of their clientele. The ability to accurately predict which customers
are at risk of discontinuing their banking services, referred to as customer churn, can
significantly impact a bank’s sustainability and growth. This report focuses on develop-
ing a predictive model that leverages customer data to forecast the likelihood of clients
either continuing with or terminating their financial services. By identifying potential
churners, banks can implement targeted retention strategies, thus mitigating financial
losses and bolstering customer loyalty.

***2. Dataset***

We select two bank customer churn datasets: [dataset 1](https://www.kaggle.com/competitions/playground-series-s4e1), [dataset 2](https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction), which contains over one hundred and fifty thousand structured and unstructured data of bank customers who either left the bank or continue to be a customer. You can also download the datasets in the **data** file.

***3. Architecture Design***

![image](https://github.com/9Tribez17/QF_Group12/blob/main/arch.png)

This is our design of our architecture. You can find the cleaned dataset through ELT process in **data** file. This image is a good guidence if you want to follow our steo throughout our code.

***3. Demo***

We also provide a demo in **demo** file. In the demo, you can see a csv dataset for testing, a pth trained model, and an ipynb. You can follow the code in the jupyter notebook to predict the bank customer churn.
