import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Q1: Filter to include weekdays only and plot line graph of pedestrian counts for each day of the week
# Include weekdays only (Monday=0 ... Friday=4)
df['DayOfWeek'] = df['Date'].dt.dayofweek
weekday_data = df[df['DayOfWeek'] < 5]

# Calculate pedestrian counts per weekday (Group by DayOfWeek)
weekday_grouped = weekday_data.groupby('DayOfWeek')['Pedestrians'].sum()

# Plotting
plt.figure(figsize=(10,6))
plt.plot(weekday_grouped.index, weekday_grouped.values, marker='o')
plt.xticks(ticks=range(5), labels=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
plt.title('Pedestrian Counts by Weekday (Monday to Friday)')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Counts')
plt.grid(True)
plt.show()

# Q2. Track pedestrian counts on Brooklyn Bridge in 2019 and analyze weather influence
# Sort the pedestrian count data by weather summary to identify any correlations (with a correlation matrix)
# between weather patterns and pedestrian counts for the selected year.
df_2019 = df[df['Date'].dt.year == 2019]

# Encoding for the 'Weather Summary' column
df_encoded = pd.get_dummies(df_2019['Weather Summary'])

# Add pedestrian count to the encoded weather DataFrame
df_encoded['Pedestrians'] = df_2019['Pedestrians'].values

# Compute correlation matrix 
corr_matrix = df_encoded.corr()
print(corr_matrix)

# Heatmap for better visualization
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation between Pedestrian Counts and Weather Conditions in 2019')
plt.show()

# 3. Categorize time of day by implementing custom function, 
# store categories in new column of DataFrame, 
# and analyze pedestrian activity

# Custom function
def categorized(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Extract hour
df['Hour'] = df['Date'].dt.hour

# New column
df['TimeOfDay'] = df['Hour'].apply(categorized)

# Group by TimeOfDay to analyze pedestrian activity patterns
day_grouped = df.groupby('TimeOfDay')['Pedestrians'].sum()

# Plot pedestrian activity
plt.figure(figsize=(10,6))
day_grouped.plot(kind='bar', color='teal')
plt.title('Pedestrian Activity by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Pedestrian Counts')
plt.xticks(rotation=0)
plt.show()
