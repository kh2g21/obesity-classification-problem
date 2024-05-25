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
  
## Frequent Consumption of High-Caloric Food across Obesity Levels

### Observations:

1. **Normal Weight**:
   - The majority of individuals with normal weight do not frequently consume high-caloric food, as indicated by a moderate count in the "yes" category and a significant count in the "no" category.

2. **Overweight Level I**:
   - Individuals in Overweight Level I predominantly consume high-caloric food frequently, with a high count in the "yes" category and a very low count in the "no" category.

3. **Overweight Level II**:
   - Similar to Overweight Level I, there is a high count of individuals frequently consuming high-caloric food, though with slightly more individuals in the "no" category compared to Overweight Level I.

4. **Obesity Type I**:
   - The highest count of individuals frequently consuming high-caloric food is observed in Obesity Type I, with very few individuals in the "no" category, indicating a strong correlation between frequent high-caloric food consumption and this obesity level.

5. **Insufficient Weight**:
   - The count of individuals with insufficient weight who frequently consume high-caloric food is low, with a more balanced distribution between "yes" and "no" categories, similar to the normal weight group.

6. **Obesity Type II and III**:
   - Both Obesity Type II and Obesity Type III show high counts in the "yes" category, with very few individuals in the "no" category. This pattern is similar to Obesity Type I but with slightly lower counts, suggesting that frequent high-caloric food consumption is prevalent across all severe obesity types.

## Physical Activity Frequency across Obesity Levels

### Observations:

1. **Normal Weight**:
   - Individuals with normal weight have a relatively high median physical activity frequency, with moderate variability indicated by the interquartile range.

2. **Overweight Level I**:
   - The median physical activity frequency is lower compared to normal weight individuals, with a larger spread indicating greater variability in activity levels.

3. **Overweight Level II**:
   - The median physical activity frequency decreases further, with less variability than Overweight Level I, indicating generally lower activity levels in this group.

4. **Obesity Type I**:
   - The median physical activity frequency is similar to Overweight Level I but with a broader spread, showing a wide range of activity levels among individuals.

5. **Insufficient Weight**:
   - Individuals with insufficient weight show a higher median physical activity frequency, similar to normal weight individuals, with moderate variability.

6. **Obesity Type II and III**:
   - Both Obesity Type II and Obesity Type III have the lowest median physical activity frequencies, with Obesity Type III showing slightly more variability. This indicates that individuals in these categories are generally less active, with some variation in activity levels.


### Alcohol Consumption across Obesity Levels


#### Observations:

1. **No Alcohol Consumption**:
   - Individuals with **Obesity Type I** have the highest count in the "no" alcohol consumption category.
   - **Normal Weight** and **Insufficient Weight** categories also have a significant count of individuals who do not consume alcohol.
   - **Obesity Type II** and **Obesity Type III** have a lower count of non-drinkers compared to Obesity Type I, indicating a different pattern in alcohol consumption.

2. **Sometimes**:
   - The majority of individuals across most obesity levels fall into the "sometimes" category for alcohol consumption.
   - **Obesity Type III** has the highest count in this category, indicating a trend where severely obese individuals tend to consume alcohol occasionally rather than abstaining completely.
   - **Overweight Level I** and **Overweight Level II** also show a high count in the "sometimes" category, reflecting that occasional alcohol consumption is common among overweight individuals.

3. **Frequently**:
   - The count of individuals consuming alcohol frequently is relatively low across all obesity levels.
   - There is a slight increase in frequent consumption among those in the **Obesity Type I** category, but it remains minimal compared to non-drinkers and occasional drinkers.

4. **Always**:
   - The "always" category shows negligible counts for all obesity levels, indicating that continuous alcohol consumption is rare among the population in the dataset.

### Overall Insights:
- **Non-drinkers**: A substantial portion of individuals with normal weight, insufficient weight, and Obesity Type I do not consume alcohol at all.
- **Occasional Drinkers**: The majority of individuals with higher obesity levels (particularly Obesity Type III) tend to drink alcohol sometimes.
- **Frequent and Constant Drinkers**: Frequent and constant alcohol consumption is minimal across all obesity levels.
