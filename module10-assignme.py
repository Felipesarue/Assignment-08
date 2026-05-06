# Module 11 Assignment: Data Visualization with Matplotlib
# SunCoast Retail Visual Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ---------------- DATA GENERATION (DO NOT MODIFY) ----------------
quarters = pd.date_range(start='2022-01-01', periods=8, freq='Q')
quarter_labels = ['Q1 2022','Q2 2022','Q3 2022','Q4 2022',
                  'Q1 2023','Q2 2023','Q3 2023','Q4 2023']

locations = ['Tampa','Miami','Orlando','Jacksonville']
categories = ['Electronics','Clothing','Home Goods','Sporting Goods','Beauty']

quarterly_data = []

for quarter_idx, quarter in enumerate(quarters):
    for location in locations:
        for category in categories:

            base_sales = np.random.normal(100000, 20000)

            seasonal_factor = 1.3 if quarter.quarter == 4 else 0.8 if quarter.quarter == 1 else 1.0

            location_factor = {'Tampa':1.0,'Miami':1.2,'Orlando':0.9,'Jacksonville':0.8}[location]
            category_factor = {'Electronics':1.5,'Clothing':1.0,'Home Goods':0.8,'Sporting Goods':0.7,'Beauty':0.9}[category]

            growth_factor = (1 + 0.05/4) ** quarter_idx

            sales = base_sales * seasonal_factor * location_factor * category_factor * growth_factor
            sales *= np.random.normal(1.0, 0.1)

            ad_spend = (sales ** 0.7) * 0.05 * np.random.normal(1.0, 0.2)

            quarterly_data.append({
                'Quarter': quarter,
                'QuarterLabel': quarter_labels[quarter_idx],
                'Location': location,
                'Category': category,
                'Sales': sales,
                'AdSpend': ad_spend,
                'Year': quarter.year
            })

sales_df = pd.DataFrame(quarterly_data)
sales_df['Quarter_Num'] = sales_df['Quarter'].dt.quarter
sales_df['SalesPerDollarSpent'] = sales_df['Sales'] / sales_df['AdSpend']

# ---------------- 1. TIME SERIES ----------------

def plot_quarterly_sales_trend():
    df = sales_df.groupby('QuarterLabel')['Sales'].sum().reset_index()

    fig, ax = plt.subplots()
    ax.plot(df['QuarterLabel'], df['Sales'], marker='o')
    ax.set_title("Quarterly Sales Trend")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Sales")
    ax.grid()
    plt.xticks(rotation=45)
    return fig


def plot_location_sales_comparison():
    fig, ax = plt.subplots()

    for loc in locations:
        df = sales_df[sales_df['Location'] == loc].groupby('QuarterLabel')['Sales'].sum()
        ax.plot(df.index, df.values, marker='o', label=loc)

    ax.set_title("Sales by Location")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Sales")
    ax.legend()
    plt.xticks(rotation=45)
    ax.grid()
    return fig

# ---------------- 2. CATEGORICAL ----------------

def plot_category_performance_by_location():
    recent = sales_df[sales_df['QuarterLabel'] == sales_df['QuarterLabel'].max()]
    pivot = recent.pivot_table(values='Sales', index='Location', columns='Category', aggfunc='sum')

    fig, ax = plt.subplots()
    pivot.plot(kind='bar', ax=ax)
    ax.set_title("Category Performance by Location (Latest Quarter)")
    ax.set_ylabel("Sales")
    return fig


def plot_sales_composition_by_location():
    pivot = sales_df.groupby(['Location','Category'])['Sales'].sum().unstack()
    pct = pivot.div(pivot.sum(axis=1), axis=0)

    fig, ax = plt.subplots()
    pct.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title("Sales Composition by Location")
    ax.set_ylabel("Proportion")
    return fig

# ---------------- 3. RELATIONSHIP ----------------

def plot_ad_spend_vs_sales():
    fig, ax = plt.subplots()

    ax.scatter(sales_df['AdSpend'], sales_df['Sales'], alpha=0.5)

    # best fit line
    m, b = np.polyfit(sales_df['AdSpend'], sales_df['Sales'], 1)
    ax.plot(sales_df['AdSpend'], m*sales_df['AdSpend'] + b, color='red')

    ax.set_title("Ad Spend vs Sales")
    ax.set_xlabel("Ad Spend")
    ax.set_ylabel("Sales")
    return fig


def plot_ad_efficiency_over_time():
    df = sales_df.groupby('QuarterLabel')['SalesPerDollarSpent'].mean()

    fig, ax = plt.subplots()
    ax.plot(df.index, df.values, marker='o')
    ax.set_title("Ad Efficiency Over Time")
    ax.set_ylabel("Sales per $ Ad Spend")
    plt.xticks(rotation=45)
    ax.grid()
    return fig

# ---------------- 4. DISTRIBUTION ----------------

def plot_customer_age_distribution():
    ages = np.random.normal(40, 15, 1000)

    fig, ax = plt.subplots()
    ax.hist(ages, bins=20)
    ax.set_title("Customer Age Distribution")
    ax.axvline(np.mean(ages), color='red')
    ax.axvline(np.median(ages), color='green')
    return fig


def plot_purchase_by_age_group():
    age_groups = pd.cut(np.random.randint(18,80,1000),
                        bins=[18,30,45,60,80],
                        labels=['18-30','31-45','46-60','61+'])

    purchases = np.random.gamma(5,20,1000)

    df = pd.DataFrame({'AgeGroup':age_groups,'Purchase':purchases})

    fig, ax = plt.subplots()
    df.boxplot(column='Purchase', by='AgeGroup', ax=ax)
    plt.suptitle("")
    return fig

# ---------------- 5. DISTRIBUTION ----------------

def plot_purchase_amount_distribution():
    fig, ax = plt.subplots()
    ax.hist(np.random.gamma(5,20,1000), bins=30)
    ax.set_title("Purchase Distribution")
    return fig


def plot_sales_by_price_tier():
    tiers = sales_df['Sales'].sample(1000, replace=True)
    labels = ['Budget','Mid-range','Premium']
    values = [30,50,20]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', explode=[0,0,0.1])
    ax.set_title("Sales by Price Tier")
    return fig

# ---------------- 6. MARKET SHARE ----------------

def plot_category_market_share():
    data = sales_df.groupby('Category')['Sales'].sum()

    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', explode=[0.1]+[0]*4)
    ax.set_title("Category Market Share")
    return fig


def plot_location_sales_distribution():
    data = sales_df.groupby('Location')['Sales'].sum()

    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct='%1.1f%%')
    ax.set_title("Location Sales Share")
    return fig

# ---------------- 7. DASHBOARD ----------------

def create_business_dashboard():
    fig, axs = plt.subplots(2,2, figsize=(10,8))

    df = sales_df.groupby('QuarterLabel')['Sales'].sum()

    axs[0,0].plot(df.values)
    axs[0,0].set_title("Sales Trend")

    axs[0,1].scatter(sales_df['AdSpend'], sales_df['Sales'])
    axs[0,1].set_title("Ad vs Sales")

    axs[1,0].bar(locations,
                 sales_df.groupby('Location')['Sales'].sum())

    axs[1,1].pie(sales_df.groupby('Category')['Sales'].sum(),
                 labels=categories, autopct='%1.1f%%')

    fig.tight_layout()
    return fig

# ---------------- MAIN ----------------

def main():
    print("SUNCOAST RETAIL VISUAL ANALYSIS")

    figs = [
        plot_quarterly_sales_trend(),
        plot_location_sales_comparison(),
        plot_category_performance_by_location(),
        plot_sales_composition_by_location(),
        plot_ad_spend_vs_sales(),
        plot_ad_efficiency_over_time(),
        plot_customer_age_distribution(),
        plot_purchase_by_age_group(),
        plot_purchase_amount_distribution(),
        plot_sales_by_price_tier(),
        plot_category_market_share(),
        plot_location_sales_distribution(),
        create_business_dashboard()
    ]

    print("\nAnalysis Complete")
    plt.show()

if __name__ == "__main__":
    main()