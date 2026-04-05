import pandas as pd

df = pd.read_csv("data/ecommerce_sales.csv")
print(df.head())
#aik new column "Total" which is the product of "Price" and "Quantity"  

df["Total"] = df["Price"] * df["Quantity"]
#convert string date to proper date time fpramt 

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

#her month ma kitne sales hui hai 

print(df.groupby("Month")["Total"].sum())

#graph banaye monthly sales ka
import matplotlib.pyplot as plt

monthly_sales = df.groupby("Month")["Total"].sum()

monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

#kon sa category sabse zyada sale hua hai

category_sales = df.groupby("Category")["Total"].sum()

category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Category")
plt.show()
#top 5 products jo sabse zyada sale hua hai
top_products = df.groupby("Product")["Total"].sum().sort_values(ascending=False)

print(top_products)
#city wise sales ka graph banaye barchaert
city_sales = df.groupby("City")["Total"].sum()

city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.show()
#remove null boxes from the data
print(df.isnull().sum())

#remove dulicate rows from the data
print(df.duplicated().sum())
df=df.drop_duplicates()
print(df.dtypes)

#wrong values ko remove krna 
print(df.describe())
#checked clean data

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)

#correlation between numerical columns

import seaborn as sns
import matplotlib.pyplot as plt

corr = df.select_dtypes(include='number').corr()

sns.heatmap(corr, annot=True, cmap="YlGnBu")
plt.title("Correlation ")
plt.show()

#distribution of total sales ziada order
sns.histplot(df["Total"], bins=5, kde=True)
plt.title("Total Sales Distribution")
plt.show()
#boxplot of total sales agr koi values ziada kam hai ya ziada

sns.boxplot(x=df["Total"])
plt.title("Boxplot of Total")
plt.show()

#scatter plot of price vs total sales
sns.scatterplot(x="Price", y="Total", data=df)
plt.title("Price vs Total")
plt.show()

plt.savefig("images/monthly_sales.png")

print("E-commerce Sales Analysis Completed")




