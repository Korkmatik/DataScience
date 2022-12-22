#!/usr/bin/env python
# coding: utf-8

# # E-Commerce data
# **This data is fake**

# **Import pandas and read the Ecommerce Purchases csv file and set it to a DataFrame called ecom**
import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases')


# **Check the head of the DataFrame**
ecom.head()


# **How many rows and columns are there?**
ecom.info()
ecom.count()

# **What is the average purchase price?**
ecom['Purchase Price'].mean()


# **What were the highest and lowest purchase prices?**
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()


# **How many people have English as their language of choice on the website?**
sum(ecom['Language'] == 'en')


# **How many people have the job title of "Lawyer"?**
sum(ecom['Job'] == 'Lawyer')


# **How many people made a purchase during AM and PM?**
ecom.groupby(by='AM or PM')['Address'].count()


# **What are the 5 most common Job Titles?**
ecom.groupby('Job')['Job'].count().sort_values(ascending=False).head(5)


# **Someone made a purchase that came from Lot: "90 WT", what was the Purchase Price for this transaction?**
ecom[ecom[['Lot', 'Purchase Price']]['Lot'] == '90 WT']['Purchase Price']


# **What is the email of the person with the following Credit Card Number: 4926535242672853 (This data is fake)**
ecom[ecom['Credit Card'] == 4926535242672853]['Email']


# **How many people have American Express as their Credit Card Provider and made a purchase above $95?**
sum((ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95))


# **How many people have a credit card that expires in 2025?**    
sum(ecom['CC Exp Date'].apply(lambda exp_data: int(exp_data.split('/')[1]) == 25))


# **What are the top 5 most popular email providers/hosts?**
ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)
