# Diwali-Sales-Analysis-using-Python
The Diwali Sales Analysis project aims to analyze and gain insights from a dataset of Diwali sales transactions. The dataset is sourced from Kaggle and contains various details about the customers and their purchase patterns during the Diwali season.

# Importing Libraries:
![Screenshot (21)](https://github.com/UtkarshShukla-Dev/Diwali-Sales-Analysis-using-Python/assets/136150238/6583c983-0603-4121-abbc-6795e6d9e601)

NumPy: Used for numerical operations and handling arrays.
Pandas: Essential for data manipulation and analysis, providing data structures like DataFrames.
Matplotlib: Used for creating static, animated, and interactive visualizations.
Seaborn: Built on top of Matplotlib, Seaborn provides a high-level interface for drawing attractive statistical graphics.
Loading Data:

The dataset is read using pd.read_csv() from a CSV file, with encoding='unicode_escape' to handle special Unicode characters.
Initial Data Inspection:

Shape: The dataset contains 11251 rows and 15 columns.
Columns: Key columns include User_ID, Cust_name, Product_ID, Gender, Age Group, Age, Marital_Status, State, Zone, Occupation, Product_Category, Orders, Amount, Status, and unnamed1.
Missing Values: The Status and unnamed1 columns have all null values and are dropped from the DataFrame.
Data Cleaning:

Dropping unnecessary columns (Status and unnamed1).
Checking for and handling null values.
Converting data types where necessary (e.g., converting Amount to integer).
Descriptive Statistics:

Using df.describe() to get an overview of the dataset's numerical columns, including count, mean, standard deviation, min, max, and percentiles.
# Exploratory Data Analysis (EDA):

# Gender Analysis:
![Screenshot (22)](https://github.com/UtkarshShukla-Dev/Diwali-Sales-Analysis-using-Python/assets/136150238/365309e8-f256-49ed-b947-daa4d3c65fcf)

Creating bar charts to visualize the count and purchasing power of each gender.
Observing that most buyers are females, and they have a higher purchasing power than males.
# Age Group Analysis:
![Screenshot (23)](https://github.com/UtkarshShukla-Dev/Diwali-Sales-Analysis-using-Python/assets/136150238/e1ecb41d-1f9e-4f30-b2b0-55765f4357e8)

Visualizing the distribution of buyers across different age groups and genders.
Finding that the majority of buyers are females aged 26-35.
# State-wise Analysis:
![Screenshot (24)](https://github.com/UtkarshShukla-Dev/Diwali-Sales-Analysis-using-Python/assets/136150238/9faa8238-9d97-4a1e-a9ca-ae24c3b93ab5)

Analyzing orders and sales amounts by state.
Identifying that Uttar Pradesh, Maharashtra, and Karnataka are the top states in terms of orders and sales.
# Marital Status Analysis:
![Screenshot (25)](https://github.com/UtkarshShukla-Dev/Diwali-Sales-Analysis-using-Python/assets/136150238/295deffd-518c-49b1-b131-5ec90dedfba4)

Examining the buying patterns based on marital status and gender.
Noting that married women are the predominant buyers with high purchasing power.
# Occupation Analysis:
![Screenshot (20)](https://github.com/UtkarshShukla-Dev/Diwali-Sales-Analysis-using-Python/assets/136150238/88124c73-408a-4165-a1b5-981a40f8bb14)

Creating visualizations to understand the distribution of buyers across various occupations.

# Conclusions:

The majority of buyers during Diwali are females, particularly in the 26-35 age group.
States like Uttar Pradesh, Maharashtra, and Karnataka are significant contributors to sales.
Married women have a notable purchasing power, making up a large portion of the buyers.
The dataset provides valuable insights into customer demographics and their buying behavior during the Diwali season, which can be leveraged for targeted marketing and sales strategies.
By analyzing these patterns, businesses can better understand their customers and optimize their marketing efforts to increase sales during festive seasons like Diwali.






