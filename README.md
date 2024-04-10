**This is QF5214 project of GROUP 12**

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
We select two bank customer churn datasets: \href{https://www.kaggle.com/competitions/playground-series-s4e1}{\textbf{dataset1}}, \href{https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction}{\textbf{dataset2}}. which contains over one hundred and fifty thousand structured and unstructured data of bank customers who either left the bank or continue to be a customer. The data dictionary is as followed. \\
$$\begin{array}{lcl}
\toprule[1.5pt] \text { \textbf{Field Name} } & \text { \textbf{Description} } & \text { \textbf{Data Type }} \\
\hline \text { Customer ID } & \text { A unique identifier for each customer } & \text { String } \\
\hline \text { Surname } & \text { The customer's surname or last name } & \text { String } \\
\hline \text { Credit Score } & \text { A numerical value representing the customer's credit score } & \text { Integer } \\
\hline \text { Geography } & \text { The country where the customer resides } & \text { String } \\
\hline \text { Gender } & \text { The customer's gender } & \text { String } \\
\hline \text { Age } & \text { The customer's age } & \text { Integer } \\
\hline \text { Tenure } & \text { The number of years the customer has been with the bank } & \text { Integer } \\
\hline \text { Balance } & \text { The customer's account balance } & \text { Float } \\
\hline \text { Num Of Products } & \text { The number of bank products the customer uses } & \text { Integer } \\
\hline \text { Has Cr Card } & \text { Whether the customer has a credit card } & \text { Binary } \\
\hline \text { Is Active Member } & \text { Whether the customer is an active member } & \text { Binary } \\
\hline \text { Estimated Salary } & \text { The estimated salary of the customer } & \text { Float } \\
\bottomrule[1.5pt]
\end{array}$$
