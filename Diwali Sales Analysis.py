#!/usr/bin/env python
# coding: utf-8

# #  Importing libraries 

# In[1]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# NumPy is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and a large collection of mathematical functions to operate on these data structures. It is widely used for scientific computing and data analysis.
# 
# Pandas is an essential library for data manipulation and analysis. It provides data structures like DataFrames (2-dimensional labeled data structure) and Series (1-dimensional labeled data structure), which are very flexible and easy to use for handling data.
# 
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. The pyplot module provides a MATLAB-like interface, making it simple to create plots and charts.
# 
# This is an IPython magic command used in Jupyter notebooks to display plots inline, directly below the code cells that produce them. Without this command, plots may not be rendered properly within the notebook.
# 
# 
# Seaborn is a data visualization library built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn is particularly useful for making complex plots easily.

# In[2]:


# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')


# pd.read_csv() is a function provided by Pandas to read a comma-separated values (CSV) file into a DataFrame. The DataFrame is a two-dimensional labeled data structure with columns of potentially different types, similar to a table in a database or an Excel spreadsheet.
# 
# encoding='unicode_escape' is an optional parameter that specifies the encoding to be used to decode the file. The 'unicode_escape' encoding is used here to handle any special Unicode characters that might be present in the CSV file. This is particularly useful if your CSV contains non-ASCII characters, such as those found in various Indian languages.

# In[3]:


df.shape


# df.shape gives the dimensions of the DataFrame.
# The output is a tuple (number of rows, number of columns).

# In[4]:


df.head()


# head() is a method of the DataFrame object in Pandas.
# By default, it returns the first 5 rows of the DataFrame. However, you can pass an integer to the method to display a different number of rows. For example, df.head(10) will display the first 10 rows.

# In[5]:


df.info()


# When you execute df.info(), it gives you a quick overview of the dataset's structure and can help identify any potential issues with the data, such as missing values or incorrect data types.

# In[4]:


df.isnull().sum()


# The df.isnull().sum() function in pandas is used to count the number of missing (null) values in each column of a DataFrame. This provides a quick overview of how many missing values are present in each column.

# In[5]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# drop() is a method of the DataFrame object in Pandas.
# 
# ['Status', 'unnamed1'] is a list of column names that you want to drop from the DataFrame.
# 
# axis=1 specifies that you want to drop columns. If you wanted to drop rows, you would use axis=0.
# 
# inplace=True modifies the existing DataFrame in place, meaning it will drop the columns from df without needing to create a new DataFrame. If inplace=False (the default), the method would return a new DataFrame with the columns dropped, and df would remain unchanged.

# In[23]:


# drop null values
df.dropna(inplace=True)


# The df.dropna(inplace=True) command is used in pandas to remove rows or columns with any missing values from the DataFrame df and apply this change directly to the original DataFrame (due to inplace=True).

# In[7]:


df['Amount'].dtypes


# The initial datatype of 'Amount' is float . We need to convert this to integer for simplicity in further analysis .

# In[17]:


# change data type

df['Amount'] = df['Amount'].astype('int')


# The astype method in pandas is used to cast a pandas object to a specified dtype. In this case, df['Amount'] = df['Amount'].astype('int') will convert the data type of the 'Amount' column in the DataFrame df to integer. However, this will work only if all values in the 'Amount' column can be converted to integers. If there are any NaN values or non-integer convertible values, it will raise an error.

# In[18]:


df['Amount'].dtypes


# To check the data type of the 'Amount' column in a pandas DataFrame, you can use the dtypes attribute. This attribute returns the data type of each column in the DataFrame. If you want to check the data type of a specific column, you can do so by accessing the column and then using the dtypes attribute.

# In[6]:


df.columns


# The df.columns attribute in pandas returns the column labels of the DataFrame. This can be useful when you want to see all the column names in your DataFrame. 
# 
# 
# 'Status', 'unnamed1' have thus been removed from  DataFrame .

# In[30]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# The df.describe() function in pandas provides a summary of statistical information for the numerical columns in the DataFrame. This function gives an overview of the central tendency, dispersion, and shape of the dataset's distribution.

# # Exploratory Data Analysis

# In[27]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# This generates a bar chart using Seaborn to visualize the count of each gender category ('Male' and 'Female' or other categories) from the DataFrame df. 
# 
# It then adds labels to each bar to display the exact count associated with each category directly on the chart.
# 
# We can check for total number of people (7842+3409=11251) which is same as seen in df.info()  

# In[6]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
sns.set(rc={'figure.figsize':(1,3)})


# df.groupby(['Gender'], as_index=False)['Amount'].sum() 
# groups the DataFrame df by the 'Gender' column and calculates the sum of the 'Amount' column for each gender. The as_index=False parameter ensures that 'Gender' remains a column and not an index.
# 
# .sort_values(by='Amount', ascending=False) 
# sorts the resulting DataFrame (sales_gen) by the 'Amount' column in descending order, ensuring that the bar chart will display genders with the highest total amount first.
# 
# sns.barplot() from the Seaborn library creates a bar plot.
# 
# x='Gender' specifies that the x-axis represents the 'Gender' column from the sales_gen DataFrame.
# 
# y='Amount' specifies that the y-axis represents the 'Amount' column from the sales_gen DataFrame.
# 
# data=sales_gen specifies the DataFrame containing the data to be plotted, which is sales_gen after grouping and summing.

# # From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men .

# # Age

# In[32]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# Creating the Countplot:
# 
# sns.countplot() is used to create a bar plot showing the count of observations in each category ('Age Group') with bars colored by another categorical variable ('Gender').
# 
# data=df specifies the DataFrame from which the data will be taken.
# 
# x='Age Group' specifies that the x-axis of the plot will represent the 'Age Group' column in df.
# 
# hue='Gender' specifies that the bars will be grouped and colored by the 'Gender' column.
# 
# Adding Labels to Bars:
# This loop iterates over each container (bars) in the plot (ax.containers).
# ax.bar_label(bars) attempts to add labels to each bar in the plot.    

# In[33]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# Grouping and Aggregating Data:
# 
# df.groupby(['Age Group'], as_index=False)['Amount'].sum() groups the DataFrame df by the 'Age Group' column and calculates the sum of the 'Amount' column for each age group. The as_index=False parameter ensures that 'Age Group' remains a column and not an index.
# 
# .sort_values(by='Amount', ascending=False) sorts the resulting DataFrame (sales_age) by the 'Amount' column in descending order, ensuring that the bar chart will display age groups with the highest total amount first.
# 
# Creating the Bar Chart:
# 
# sns.barplot() from the Seaborn library creates a bar plot.
# 
# x='Age Group' specifies that the x-axis represents the 'Age Group' column from the sales_age DataFrame.
# 
# y='Amount' specifies that the y-axis represents the 'Amount' column from the sales_age DataFrame.
# 
# data=sales_age specifies the DataFrame containing the data to be plotted, which is sales_age after grouping and summing.

# # *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*.

# 
# 
# 
# # State:

# In[43]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(17,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# Grouping and Aggregating Data:
# 
# df.groupby(['State'], as_index=False)['Orders'].sum() groups the DataFrame df by the 'State' column and calculates the sum of the 'Orders' column for each state. The as_index=False parameter ensures that 'State' remains a column and not an index.
# 
# .sort_values(by='Orders', ascending=False) sorts the resulting DataFrame (sales_state) by the 'Orders' column in descending order.
# 
# .head(10) selects the top 10 states with the highest total number of orders.
# 
# Setting Plot Size:sns.set() is used to set the default Seaborn plotting parameters. Here, rc={'figure.figsize':(15,5)} sets the figure size to 17 inches in width and 5 inches in height.
# 
# Creating the Bar Chart:
# 
# sns.barplot() from the Seaborn library creates a bar plot.
# 
# data=sales_state specifies the DataFrame containing the data to be plotted, which is sales_state after grouping, summing, and sorting.
# 
# x='State' specifies that the x-axis represents the 'State' column from the sales_state DataFrame.
# 
# y='Orders' specifies that the y-axis represents the 'Orders' column from the sales_state DataFrame

# # From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively .

# 
# 
# # Marital Status:

# In[44]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# Creating the Countplot:
# sns.countplot() creates a bar plot showing the count of observations in each category ('Marital_Status').
# 
# data=df specifies the DataFrame containing the data (df) to be plotted.
# 
# x='Marital_Status' specifies that the x-axis of the plot represents the 'Marital_Status' column from the DataFrame df.
# 
# Setting Plot Size:
# sns.set() is used to set the default Seaborn plotting parameters. Here, rc={'figure.figsize':(7,5)} sets the figure size to 7 inches in width and 5 inches in height.
# 
# Adding Labels to Bars:
# This loop iterates over each container (bars) in the plot (ax.containers).
# ax.bar_label(bars) adds labels to each bar in the plot.

# In[45]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# Grouping and Aggregating Data:
# df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum() groups the DataFrame df by both 'Marital_Status' and 'Gender' columns and calculates the sum of the 'Amount' column for each combination of marital status and gender.
# 
# .sort_values(by='Amount', ascending=False) sorts the resulting DataFrame (sales_state) by the 'Amount' column in descending order, ensuring the plot displays the highest sales amounts first.
# 
# Setting Plot Size:
# sns.set() sets the default Seaborn plotting parameters. Here, rc={'figure.figsize':(6,5)} sets the figure size to 6 inches in width and 5 inches in height.
# 
# Creating the Grouped Bar Plot:
# sns.barplot() from Seaborn creates a bar plot.
# 
# data=sales_state specifies the DataFrame containing the data (sales_state) to be plotted, which has been grouped and aggregated.
# x='Marital_Status' specifies that the x-axis represents the 'Marital_Status' column from sales_state.
# 
# y='Amount' specifies that the y-axis represents the 'Amount' column from sales_state, showing the total sales amount.
# 
# hue='Gender' specifies that the bars will be grouped and colored by the 'Gender' column, allowing for comparison of sales amounts across genders within each marital status.

# # From above graphs we can see that most of the buyers are married (women) and they have high purchasing power.

# 
# 
# # Occupation:

# In[46]:


#sns.set(rc={'figure.figsize':(20,6)})
plt.figure(figsize=(20,6))
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# Setting Figure Size:
# plt.figure(figsize=(20, 6)) sets the size of the figure for plotting using Matplotlib. Here, figsize=(20, 6) specifies a figure width of 20 inches and a height of 6 inches.
# 
# Creating the Countplot:
# sns.countplot() creates a bar plot showing the count of observations in each category ('Occupation').
# 
# data=df specifies the DataFrame containing the data (df) to be plotted.
# 
# x='Occupation' specifies that the x-axis of the plot represents the 'Occupation' column from the DataFrame df.
# 
# Adding Labels to Bars:
# 
# This loop iterates over each container (bars) in the plot (ax.containers).
# 
# ax.bar_label(bars) adds labels to each bar in the plot. 

# In[4]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# Grouping and Aggregating Data:
# 
# df.groupby(['Occupation'], as_index=False)['Amount'].sum() groups the DataFrame df by the 'Occupation' column and calculates the sum of the 'Amount' column for each occupation. The as_index=False parameter ensures that 'Occupation' remains a column and not an index.
# 
# .sort_values(by='Amount', ascending=False) sorts the resulting DataFrame (sales_state) by the 'Amount' column in descending order, ensuring that the plot displays occupations with the highest total sales amount first.
# 
# Setting Plot Size:
# sns.set() sets the default Seaborn plotting parameters. Here, rc={'figure.figsize':(20,5)} sets the figure size to 20 inches in width and 5 inches in height.
# 
# Creating the Bar Plot:
# sns.barplot() from Seaborn creates a bar plot.
# 
# data=sales_state specifies the DataFrame containing the data (sales_state) to be plotted, which has been grouped, aggregated, and sorted.
# 
# x='Occupation' specifies that the x-axis represents the 'Occupation' column from sales_state.
# 
# y='Amount' specifies that the y-axis represents the 'Amount' column from sales_state, showing the total sales amount for each occupation.
# 

# # From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector .

# 
# 
# # Product Category:

# In[13]:


sns.set(rc={'figure.figsize':(24,10)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# Setting Plot Size:
# sns.set(rc={'figure.figsize':(24,10)}) sets the default size of the figure for Seaborn plots. Here, the figure size is set to 24 inches in width and 10 inches in height.
# 
# Creating the Countplot:
# sns.countplot() creates a bar plot showing the count of observations in each category ('Product_Category').
# data=df specifies the DataFrame containing the data (df) to be plotted.
# x='Product_Category' specifies that the x-axis of the plot represents the 'Product_Category' column from the DataFrame df.
# 
# Adding Labels to Bars:
# This loop iterates over each container (bars) in the plot (ax.containers).
# ax.bar_label(bars) adds labels to each bar in the plot

# In[14]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# Grouping, Aggregating, and Sorting Data:
# 
# df.groupby(['Product_Category'], as_index=False)['Amount'].sum() groups the DataFrame df by the 'Product_Category' column and calculates the sum of the 'Amount' column for each product category. The as_index=False parameter ensures that
# 
# 'Product_Category' remains a column and not an index.
# 
# .sort_values(by='Amount', ascending=False) sorts the resulting DataFrame (sales_state) by the 'Amount' column in descending order.
# 
# .head(10) selects the top 10 product categories based on the total sales amount.
# 
# Creating the Bar Plot:
# 
# sns.barplot() from Seaborn creates a bar plot.
# 
# data=sales_state specifies the DataFrame containing the data (sales_state) to be plotted, which has been grouped, aggregated, sorted, and limited to the top 10 product categories.
# 
# x='Product_Category' specifies that the x-axis represents the 'Product_Category' column from sales_state.
# 
# y='Amount' specifies that the y-axis represents the 'Amount' column from sales_state, showing the total sales amount for each product category.
# 
# 
# 
# 
# 

# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category
# 

# In[15]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# Grouping, Aggregating, and Sorting Data:
#  df.groupby(['Product_ID'], as_index=False)['Orders'].sum(): This groups the DataFrame df by the 'Product_ID' column and calculates the sum of the 'Orders' column for each product ID. Setting as_index=False ensures that 'Product_ID' remains a column in the resulting DataFrame.
#  
# .sort_values(by='Orders', ascending=False): This sorts the resulting DataFrame (sales_state) by the 'Orders' column in descending order.
# 
# .head(10): This selects the top 10 product IDs based on the total number of orders.
# 
# Creating the Bar Plot:
# 
# sns.barplot(data=sales_state, x='Product_ID', y='Orders'): This creates a bar plot using Seaborn. The data parameter specifies the DataFrame to use, x specifies the column to use for the x-axis, and y specifies the column to use for the y-axis.
#    

# In[16]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# Creating a Figure and Axes:
# fig1, ax1 = plt.subplots(figsize=(12,7)) creates a new figure (fig1) and a set of subplots (ax1). The figsize parameter sets the size of the figure to 12 inches in width and 7 inches in height.    
# 
# Grouping, Aggregating, and Plotting Data:
# df.groupby('Product_ID')['Orders'].sum() groups the DataFrame df by the 'Product_ID' column and calculates the sum of the 'Orders' column for each product ID.
# 
# .nlargest(10) selects the top 10 product IDs based on the total number of orders.
# 
# .sort_values(ascending=False) ensures that the data is sorted in descending order.
# 
# .plot(kind='bar', ax=ax1) creates a bar plot using the aggregated and sorted data. The kind='bar' parameter specifies that a bar plot should be created, and ax=ax1 specifies that the plot should be drawn on the previously created axes (ax1).

# # Conclusion:

# # *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*.
