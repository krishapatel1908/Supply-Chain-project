import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\supply_chain_data1.csv")
print(df.head())
print(df.shape)
print(df.info())


# Supply Chain KPI Analysis

total_revenue = df['Revenue generated'].sum()
print("total revenue :",total_revenue)

total_products_sold = df['Number of products sold'].sum()
print("total products sold :",total_products_sold)

avg_order_quantity = df['Order quantities'].mean()
print("avg order quantity:",avg_order_quantity)

avg_lead_time = df['Lead time'].mean()
print("avg lead time:",avg_lead_time)


# EDA 
total_revunue = df.groupby("Product type")["Revenue generated"].sum()
print(total_revunue)

total_product_sold = df.groupby("Product type")["Number of products sold"].sum()
print(total_product_sold)

avg_product_price = df.groupby("Product type")["Price"].mean()
avg_product_price.sort_values(ascending=False)
print(avg_product_price)


low_stock_levels =df.nsmallest(10, 'Stock levels')[['Product type', 'SKU', 'Stock levels']]
print(low_stock_levels)


total_revenue = df.groupby("Product type")["Revenue generated"].sum()
revenue_precentage = (total_revenue/df["Revenue generated"].sum())*100
print(revenue_precentage)


sku_count = df['Product type'].value_counts()
print(sku_count)


supplier_lead_time = df.groupby("Supplier name")["Lead time"].mean()
print(supplier_lead_time.sort_values(ascending=False))


supplier_products = df['Supplier name'].value_counts()
print(supplier_products)


supplier_lead_time = df.groupby("Supplier name")["Lead time"].mean()
high_lead_time = supplier_lead_time[supplier_lead_time>16]
print(high_lead_time)


supplier = df.groupby("Supplier name").agg({
    'Lead times': 'mean',
    'Defect rates': 'mean'
})
high_risk = supplier[
    (supplier['Lead times']>16)&
    (supplier['Defect rates']>2)
]
print(high_risk)

low_stock = df.nsmallest(10,'Stock levels')
print(low_stock[['Product type','SKU','Stock levels']])

stock_sorted = df.sort_values('Stock levels',ascending=False)
print(stock_sorted[['Product type','SKU','Stock levels']].head(10))

high_demand_low_stock = df[
    (df['Stock levels']< 10)&
    (df['Number of products sold']>500)
]
print(high_demand_low_stock[
    ['Product type','SKU','Stock levels','Number of products sold']
])

high_defect = df[df['Defect rates']>3]
print("Number of high defct product",len(high_defect))

high_defct = df[df['Defect rates']>3]
quality_issues = high_defct['Product type'].value_counts()
print(quality_issues)

revenue_by_product = df.groupby('Product type')['Revenue generated'].sum()
revenue_by_product.plot(kind= 'bar')
plt.title('Total Revenue by product type')
plt.xlabel('Product type')
plt.ylabel('Revenue')
plt.xticks(rotation = 0)
plt.show()

Revenue_by_Transportation_Mode = df.groupby('Transportation modes')['Revenue generated'].sum()
Revenue_by_Transportation_Mode.plot(kind='bar')

plt.title('total Revenue by Transportation Mode')

plt.xlabel('Transportation modes')
plt.ylabel('Revenue geverated')
plt.xticks(rotation = 0)
plt.show()



sales_by_product = df.groupby('Product type')['Number of products sold'].sum()

sales_by_product.plot(kind='bar')
plt.title('Total product sold by products type')
plt.xlabel('Product type')
plt.ylabel('Products sold')
plt.xticks(rotation = 0)
plt.show()