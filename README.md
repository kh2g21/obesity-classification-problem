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

## Installation

To run this project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/kh2g21/obesity-classification-problem.git
   cd obesity-classification-problem

2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`



   

