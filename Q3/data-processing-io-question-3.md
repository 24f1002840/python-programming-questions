---
title: Data Processing I/O Question
tags: ['pandas', 'groupby','aggregation','stdin','stdout']
---

# Problem Statement
## StartDuck Coffee shop Sales Analysis

    StarDuck is a Coffee company and they are trying to expand their base in India.
    The CEO is confident but slightly confused and has some questions. 
    You as IITM BS student who has learnt python can help him answer some questions by uncovering some insights from the data they have shared with you.
    The data has the following attributes
    -- Date
    -- Day
    -- Product
    -- Quantity
    -- Price
    -- Total Sales
    -- Payment Method

    the data is in csv format read the data from stdin

    Answer the following questions by implementing the below functions

        1> What is the most profitable day of the week for StarDuck?
        2> Which product generates the highest revenue?
        3> Which payment method is used very frequently?
        4> What is the average daily revenue?

    Print the answers to the above question to stdout.
# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>
    
    def take_input():
        <sol>
        import pandas as pd
        global data
        data = input()
        data = pd.read_csv(pd.compat.StringIO(data))
        </sol>

    def most_profitable_dotw():
        <sol>
        
        day_sales = data.groupby('Day')['Total Sales'].sum()
        most_profitable_day = day_sales.idxmax()
        most_profitable_day_sales = day_sales.max()
        print(most_profitable_day,most_profitable_day_sales)
        </sol>

    def highest_revenue_product():
        <sol>
        
        product_sales = data.groupby('Product')['Total Sales'].sum()
        highest_revenue_product = product_sales.idxmax()
        highest_revenue = product_sales.max()
        print(highest_revenue_product,highest_revenue)
        </sol>
    
    def average_daily_revenue():
        <sol>
        total_sales = data['Total Sales'].sum()
        unique_days = data['Date'].nunique()
        average = total_sales / unique_days
        print(average)
        </sol>
    def frequent_payment_method():
        <sol>
        payment_method_counts  = data['Payment Method'].value_counts()
        most_frequent = payment_method_counts.idmax()
        print(most_frequent)
        </sol>

    


        
</template>

<suffix>
#driver code
import pandas as pd
take_input()
most_profitable_dotw()
highest_revenue_product()
average_daily_revenue()
frequent_payment_method()
</suffix>

```

# Public Test Cases

## Input 1

```
Date,Day,Product,Quantity,Price,Total Sales,Payment Method
2025-01-01,Monday,Coffee,120,3.50,420.00,Credit Card
2025-01-01,Monday,Tea,50,2.50,125.00,Cash
2025-01-01,Monday,Pastry,80,4.00,320.00,Credit Card
2025-01-02,Tuesday,Coffee,150,3.50,525.00,Debit Card
2025-01-02,Tuesday,Tea,60,2.50,150.00,Cash
2025-01-02,Tuesday,Pastry,90,4.00,360.00,Credit Card
2025-01-03,Wednesday,Coffee,130,3.50,455.00,Cash
2025-01-03,Wednesday,Tea,40,2.50,100.00,Credit Card
2025-01-03,Wednesday,Pastry,70,4.00,280.00,Debit Card
2025-01-04,Thursday,Coffee,160,3.50,560.00,Credit Card
2025-01-04,Thursday,Tea,70,2.50,175.00,Debit Card
2025-01-04,Thursday,Pastry,100,4.00,400.00,Cash
2025-01-05,Friday,Coffee,180,3.50,630.00,Cash
2025-01-05,Friday,Tea,90,2.50,225.00,Credit Card
2025-01-05,Friday,Pastry,110,4.00,440.00,Debit Card
2025-01-06,Saturday,Coffee,200,3.50,700.00,Debit Card
2025-01-06,Saturday,Tea,80,2.50,200.00,Cash
2025-01-06,Saturday,Pastry,120,4.00,480.00,Credit Card
2025-01-07,Sunday,Coffee,170,3.50,595.00,Credit Card
2025-01-07,Sunday,Tea,100,2.50,250.00,Debit Card
2025-01-07,Sunday,Pastry,130,4.00,520.00,Cash


```

## Output 1

```
Saturday 1380.00
Coffee 3885.00
1130.00
Credit Card

```


