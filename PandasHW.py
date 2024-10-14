import pandas as pd

# Q5
# From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0)df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

filtered = df[['Manufacturer', 'Model', 'Type']].iloc[::20]
print("Filtered DataFrame:\n", filtered)

#Q6
# Replace missing values in Min.Price and Max.Price columns with their respective mean.
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
print("DataFrame after filling missing values:\n", df[['Min.Price', 'Max.Price']].head())

#Q7
# How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# Get rows with row sum > 100
row_over_100 = df[df.sum(axis=1) > 100]
print("Rows with sum > 100:\n", row_over_100)

