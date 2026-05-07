## Assignment 12 This repository contains my work for Assignment 12.

## Files Included
#- main.py

## What I Practiced
#In this assignment, I practiced data cleaning and preprocessing using Python. I worked with a messy customer dataset and learned how to handle missing values, fix incorrect data types, standardize text formats, remove duplicates, and create new derived features. I also practiced using Pandas for data manipulation and generating business insights from cleaned data.

import pandas as pd
import numpy as np
from datetime import datetime
from io import StringIO
import re

# Welcome message
print("=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING")
print("=" * 60)

# ----- SIMULATED CSV FILE -----
csv_content = """customer_id,first_name,last_name,email,phone,join_date,last_purchase,total_purchases,total_spent,preferred_category,satisfaction_rating,age,city,state,loyalty_status
CS001,John,Smith,johnsmith@email.com,(555) 123-4567,2023-01-15,2023-12-01,12,"1,250.99",Menswear,4.5,35,Tampa,FL,Gold
CS002,Emily,Johnson,emily.j@email.com,555.987.6543,01/25/2023,10/15/2023,8,$875.50,Womenswear,4,28,Miami,FL,Silver
CS003,Michael,Williams,mw@email.com,(555)456-7890,2023-02-10,2023-11-20,15,"2,100.75",Footwear,5,42,Orlando,FL,Gold
CS004,JESSICA,BROWN,jess.brown@email.com,5551234567,2023-03-05,2023-12-10,6,659.25,Womenswear,3.5,31,Tampa,FL,Bronze
CS005,David,jones,djones@email.com,555-789-1234,2023-03-20,2023-09-18,4,350.00,Menswear,,45,Jacksonville,FL,Bronze
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS007,Robert,Davis,robert.davis@email.com,555.444.7777,04/30/2023,11/25/2023,7,$725.80,Footwear,4.5,38,Miami,FL,Silver
CS008,Jennifer,Garcia,jen.garcia@email.com,(555)876-5432,2023-05-15,2023-10-30,3,280.50,ACCESSORIES,3,25,Orlando,FL,Bronze
CS009,Michael,Williams,m.williams@email.com,5558889999,2023-06-01,2023-12-07,9,1100.00,Menswear,4,39,Jacksonville,FL,Silver
CS010,Emily,Johnson,emilyjohnson@email.com,555-321-6547,2023-06-15,2023-12-15,14,"1,875.25",Womenswear,4.5,27,Miami,FL,Gold
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS011,Amanda,,amanda.p@email.com,(555) 741-8529,2023-07-10,,2,180.00,womenswear,3,32,Tampa,FL,Bronze
CS012,Thomas,Wilson,thomas.w@email.com,,2023-07-25,2023-11-02,5,450.75,menswear,4,44,Orlando,FL,Bronze
CS013,Lisa,Anderson,lisa.a@email.com,555.159.7530,08/05/2023,,0,0.00,Womenswear,,30,Miami,FL,
CS014,James,Taylor,jtaylor@email.com,555-951-7530,2023-08-20,2023-10-10,11,"1,520.65",Footwear,4.5,,Jacksonville,FL,Gold
CS015,Karen,Thomas,karen.t@email.com,(555) 357-9512,2023-09-05,2023-12-12,6,685.30,Womenswear,4,36,Tampa,FL,Silver
"""
customer_data_csv = StringIO(csv_content)

# -------------------------------
# TODO 1: Load and Explore the Dataset
# -------------------------------
raw_df = pd.read_csv(customer_data_csv)

# Check missing values and duplicates for final report
initial_missing_counts = raw_df.isna().sum()
initial_duplicate_count = raw_df.duplicated().sum()

# -------------------------------
# TODO 2: Handle Missing Values
# -------------------------------
df_cleaned = raw_df.copy()

# 2.2 Fill missing satisfaction_rating with median
df_cleaned['satisfaction_rating'] = df_cleaned['satisfaction_rating'].fillna(df_cleaned['satisfaction_rating'].median())

# 2.3 Fill missing last_purchase dates using forward fill
# First, convert to datetime to ensure proper fill behavior
df_cleaned['last_purchase'] = pd.to_datetime(df_cleaned['last_purchase'], errors='coerce')
df_cleaned['last_purchase'] = df_cleaned['last_purchase'].ffill()

# 2.4 Handle other missing values
df_cleaned['last_name'] = df_cleaned['last_name'].fillna('Unknown')
df_cleaned['phone'] = df_cleaned['phone'].fillna('Unknown')
df_cleaned['loyalty_status'] = df_cleaned['loyalty_status'].replace('', np.nan).fillna('Bronze')
# Fill missing age with mean (rounded)
df_cleaned['age'] = df_cleaned['age'].fillna(df_cleaned['age'].mean())

# -------------------------------
# TODO 3: Correct Data Types
# -------------------------------
# 3.1 Convert dates
df_cleaned['join_date'] = pd.to_datetime(df_cleaned['join_date'], errors='coerce')

# 3.2 Convert total_spent to numeric (remove $ and ,)
df_cleaned['total_spent'] = df_cleaned['total_spent'].replace(r'[\$,]', '', regex=True).astype(float)

# 3.3 Ensure numeric fields are correct types
df_cleaned['total_purchases'] = df_cleaned['total_purchases'].astype(int)
df_cleaned['age'] = df_cleaned['age'].astype(int)

# -------------------------------
# TODO 4: Clean and Standardize Text Data
# -------------------------------
# Names and Categories to Proper Case
df_cleaned['first_name'] = df_cleaned['first_name'].str.title()
df_cleaned['last_name'] = df_cleaned['last_name'].str.title()
df_cleaned['preferred_category'] = df_cleaned['preferred_category'].str.title()

# Standardize phone numbers: format "(XXX) XXX-XXXX"
def standardize_phone(p):
    digits = re.sub(r'\D', '', str(p))
    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    return "Unknown" if p == "Unknown" else p

df_cleaned['phone'] = df_cleaned['phone'].apply(standardize_phone)

# -------------------------------
# TODO 5: Remove Duplicates
# -------------------------------
# Keeping the first occurrence based on customer_id
df_cleaned = df_cleaned.drop_duplicates(subset=['customer_id'], keep='first')

# -------------------------------
# TODO 6: Add Derived Features
# -------------------------------
analysis_date = pd.Timestamp('2023-12-31')
df_cleaned['days_since_last_purchase'] = (analysis_date - df_cleaned['last_purchase']).dt.days
df_cleaned['average_purchase_value'] = (df_cleaned['total_spent'] / df_cleaned['total_purchases']).fillna(0)

def get_frequency_cat(count):
    if count >= 10: return 'High'
    elif count >= 5: return 'Medium'
    else: return 'Low'

df_cleaned['purchase_frequency_category'] = df_cleaned['total_purchases'].apply(get_frequency_cat)

# -------------------------------
# TODO 7: Clean Up and Sort
# -------------------------------
df_final = df_cleaned.rename(columns={
    'customer_id':'CustomerID', 'first_name':'FirstName', 'last_name':'LastName',
    'email':'Email', 'phone':'Phone', 'join_date':'JoinDate',
    'last_purchase':'LastPurchase', 'total_purchases':'TotalPurchases',
    'total_spent':'TotalSpent', 'preferred_category':'PreferredCategory',
    'satisfaction_rating':'SatisfactionRating', 'age':'Age',
    'city':'City', 'state':'State', 'loyalty_status':'LoyaltyStatus'
}).sort_values(by='TotalSpent', ascending=False)

# -------------------------------
# TODO 8 & 9: Insights and Final Report
# -------------------------------
avg_spent_by_loyalty = df_final.groupby('LoyaltyStatus')['TotalSpent'].mean()
category_revenue = df_final.groupby('PreferredCategory')['TotalSpent'].sum()
satisfaction_spend_corr = df_final['SatisfactionRating'].corr(df_final['TotalSpent'])

print("\n" + "="*60)
print("DATA QUALITY ISSUES")
print("="*60)
print(f"Missing Values: {initial_missing_counts.sum()} total missing entries")
print(f"Duplicates: {initial_duplicate_count} duplicate records removed")
print(f"Data Type Conversions: Dates (to datetime), TotalSpent (to float), Age (to int)")

print("\n" + "="*60)
print("STANDARDIZATION CHANGES")
print("="*60)
print("- Names & Categories: Standardized to Title Case")
print("- Phone Numbers: Standardized to (XXX) XXX-XXXX")
print("- Loyalty Status: Missing values defaulted to 'Bronze'")

print("\n" + "="*60)
print("KEY BUSINESS INSIGHTS")
print("="*60)
print(f"Total Customer Count: {len(df_final)}")
print("\nAverage Spend by Loyalty Level:")
print(avg_spent_by_loyalty.round(2))
print(f"\nTop Performing Category: {category_revenue.idxmax()} (${category_revenue.max():,.2f})")
print(f"Satisfaction vs. Spending Correlation: {satisfaction_spend_corr:.2f}")

print("\n" + "="*60)
print("CLEANED DATASET PREVIEW (TOP 5 SPENDERS)")
print("="*60)
print(df_final.head())
