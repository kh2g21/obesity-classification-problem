import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

# Display basic information
print(df.head())
print(df.describe())
print(df.info())

# Gender Distribution across Obesity Levels
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Gender', hue='NObeyesdad')
plt.title('Gender Distribution across Obesity Levels')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Obesity Level')
plt.show()

# Age Distribution across Obesity Levels
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='NObeyesdad', y='Age')
plt.title('Age Distribution across Obesity Levels')
plt.xlabel('Obesity Level')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()

# Frequency of alcohol consumption across obesity levels
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='CALC', hue='NObeyesdad')
plt.title('Alcohol Consumption across Obesity Levels')
plt.xlabel('Frequency of Alcohol Consumption')
plt.ylabel('Count')
plt.legend(title='Obesity Level')
plt.show()


# Height vs Weight colored by Obesity Level
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Height', y='Weight', hue='NObeyesdad', alpha=0.7)
plt.title('Height vs Weight colored by Obesity Level')
plt.xlabel('Height (meters)')
plt.ylabel('Weight (kilograms)')
plt.legend(title='Obesity Level')
plt.show()

# Family History with Overweight across Obesity Levels
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='family_history_with_overweight', hue='NObeyesdad')
plt.title('Family History with Overweight across Obesity Levels')
plt.xlabel('Family History with Overweight')
plt.ylabel('Count')
plt.legend(title='Obesity Level')
plt.show()

# Frequent Consumption of High Caloric Food across Obesity Levels
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='FAVC', hue='NObeyesdad')
plt.title('Frequent Consumption of High Caloric Food across Obesity Levels')
plt.xlabel('Frequent Consumption of High Caloric Food')
plt.ylabel('Count')
plt.legend(title='Obesity Level')
plt.show()

# Physical Activity Frequency across Obesity Levels
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='NObeyesdad', y='FAF')
plt.title('Physical Activity Frequency across Obesity Levels')
plt.xlabel('Obesity Level')
plt.ylabel('Physical Activity Frequency')
plt.xticks(rotation=45)
plt.show()


