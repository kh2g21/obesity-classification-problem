# obesity-classification-problem

## Overview

This project aims to classify obesity levels based on various health and lifestyle features. The objective is to develop a machine learning model that can accurately predict whether an individual is underweight, normal weight, overweight, or obese, using factors derived from their health and lifestyle habits.

## Dataset

The dataset used in this project is the [Obesity Levels Detection Data Set](https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels). It contains information about individuals' eating habits, physical condition, and daily routines. Each record in the dataset includes the following features:

- **Gender**: Male or Female
- **Age**: Age of the individual
- **Height**: Height in meters
- **Weight**: Weight in kilograms
- **Family history with overweight**: Yes or No
- **FAVC (Frequent consumption of high caloric food)**: Yes or No
- **FCVC (Frequency of consumption of vegetables)**: Frequency level
- **NCP (Number of main meals)**: Number of main meals per day
- **CAEC (Consumption of food between meals)**: Yes or No
- **SMOKE**: Whether the individual smokes: Yes or No
- **CH2O (Daily water intake)**: Liters of water consumed per day
- **SCC (Calories consumption monitoring)**: Yes or No
- **FAF (Physical activity frequency)**: Times per week
- **TUE (Time using technology devices)**: Hours per day
- **CALC (Consumption of alcohol)**: Frequency level
- **MTRANS (Transportation used)**: Type of transportation used
- **NObeyesdad (Obesity level)** Category of obesity based on all of the above factors.

The target variable is the obesity level, classified into categories: Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I, Obesity Type II, and Obesity Type III.

## Insights from Data Analysis

### Gender Distribution across Obesity Levels

![Gender Distribution across Obesity Levels](path/to/your/generated/plot.png)

#### Observations:

1. **Normal Weight**:
   - Both females and males have a significant number of individuals in the normal weight category. The counts are relatively balanced between genders.

2. **Overweight Level I and II**:
   - The counts for both genders are similar in Overweight Level I, but slightly higher in males for Overweight Level II. This suggests that overweight issues are prevalent among both genders with a slight tendency towards males in more severe cases.

3. **Obesity Types I, II, and III**:
   - Obesity Type I shows a relatively balanced distribution between females and males.
   - Obesity Type II has a much higher count in males compared to females, indicating a higher prevalence in males.
   - Obesity Type III is notably higher in females, with a significant count compared to males.
   
4. **Insufficient Weight**:
   - More females fall into the insufficient weight category than males, which could indicate different issues related to weight management among genders.
  
### Age Distribution across Obesity Levels

#### Observations:

1. **Normal Weight**:
   - The age range for individuals with normal weight is relatively narrow, mostly concentrated around the early twenties with some outliers extending up to around 60 years.

2. **Overweight Level I**:
   - The age distribution for Overweight Level I individuals is slightly broader but still predominantly in the early twenties to early thirties, with a few outliers in the upper age range.

3. **Overweight Level II**:
   - The age range broadens further in Overweight Level II, extending from late teens to around 40 years, indicating that higher overweight levels start to appear in a wider age range.

4. **Obesity Type I**:
   - The age distribution for Obesity Type I shows a significant increase in the age range, spanning from late teens to around 50 years. The median age appears higher compared to normal weight and overweight levels.

5. **Insufficient Weight**:
   - The age range for individuals with insufficient weight is relatively narrow, mostly concentrated in the late teens to early twenties, with a few outliers in the higher age range.

6. **Obesity Type II and III**:
   - Obesity Type II shows a wide age range from late teens to around 50 years, similar to Obesity Type I but with a slightly higher median age.
   - Obesity Type III has a more concentrated age range, primarily in the early twenties to early thirties, with fewer outliers, indicating that severe obesity is more prevalent in younger individuals.

   

