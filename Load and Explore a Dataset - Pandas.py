sales_data = [
    {'Product': 'Laptop', 'Brand': 'Dell', 'Month': 'Jan' , 'Region': 'North'},
    {'Product': 'Laptop', 'Brand': 'HP', 'Month': 'Feb', 'Sales': 1300, 'Region': 'South'},
    {'Product': 'Phone', 'Brand': 'Samsung', 'Month': 'Jan', 'Sales': 800, 'Region': 'West'},
    {'Product': 'Tablet', 'Brand': 'Apple', 'Month': 'Feb', 'Sales': 900, 'Region': 'East'},
    {'Product': 'Laptop', 'Brand': 'Dell', 'Month': 'Feb', 'Sales': 1700, 'Region': 'North'},
    {'Product': 'Phone', 'Brand': 'Nokia', 'Month': 'Feb', 'Sales': 400, 'Region': 'South'},
    {'Product': 'Laptop', 'Brand': 'HP', 'Month': 'Jan', 'Sales': 1200, 'Region': 'East'},
    {'Product': 'Tablet', 'Brand': 'Apple', 'Month': 'Jan', 'Sales': 950, 'Region': 'North'},
]


import pandas as pd
df = pd.DataFrame(sales_data)

# View first few rows
print(df.head(20))

# Quick stats
print(df.describe())

# Summary info
print(df.info())

#select a column # Series (1D)
print(df['Product'])

#select mul column # DataFrame (2D)
print(df[['Product','Brand']])


# Select rows by index #first row
print(df.iloc[1])

# Select rows by index #first five row #iloc is position based index
print(df.iloc[0:5])

# Select rows by condition
print(df[df['Sales']>1000])

# Check for missing values (check how many missing (NaN) values are in each column)
print(df.isnull().sum())

# Fill missing with default
df['Sales'] = df['Sales'].fillna(0)
print(df)
df.fillna({'Sales': 0}, inplace=True)
# fillna(0) Replaces all NaN (missing values) in that column with the value 0.
# inplace=True Makes the change directly to the existing DataFrame (no need to assign back).



# Drop rows with nulls
#df.dropna(inplace=True)
print(df)

# Group by Department and find average salary
print(df.groupby('Region')['Sales'].sum())

# Count rows per group
print(df.groupby('Region').size())

# Sort by salary
print(df.sort_values(by='Sales', ascending=False))

# Add rank
df['Rank'] = df['Sales'].rank(ascending=False)
print(df)


# Add new column
df['Tax'] = df['Sales'] * 0.1
print(df)


# Modify existing column
df['Sales'] = df['Sales'] + 1000
print(df)


#create data frame df1 
df1 = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

print(df1)

#create data frame df1 
df2 = pd.DataFrame({
    'EmployeeID': [102, 103, 104, 105],
    'Salary': [50000, 60000, 55000, 45000]
})

print(df2)

#Merge using pd.merge
df_final=pd.merge(df1, df2, on='EmployeeID', how='inner')
print(df_final)