#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator Project

# In[ ]:


# Author: Motlalepula Lawrence Tshabalala
# Date: 2025/05/09
# Description: A simple Body Mass Index (BMI) calculator using metric units.


# In[1]:


# Complete BMI Calculator (All Steps in One Cell) 

# STEP 1: COLLECT USER INFORMATION

# Ask the user to enter their gender/sex
gender = input("Enter your gender (Male/Female): ")

# Ask the user to enter their weight in kilograms
weight = float(input("Enter your weight in kilograms (kg): "))

# Ask the user to enter their height in centimeters
height_cm = float(input("Enter your height in centimeters (cm): "))

# Confirm the inputs
print("\n--- Input Summary ---")
print(f"Gender: {gender}")
print(f"Weight: {weight} kg")
print(f"Height: {height_cm} cm")


# STEP 2: CALCULATE BMI

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate BMI using the formula
bmi = weight / (height_m ** 2)

# Print the raw BMI value
print("\n--- BMI Calculation ---")
print(f"Height in meters: {height_m}")
print(f"Your BMI is: {bmi}")


# STEP 3: DISPLAY RESULTS

# Round the BMI to 2 decimal places
bmi_rounded = round(bmi, 2)

# Print the rounded BMI
print("\n--- BMI Result ---")
print(f"Your BMI is: {bmi_rounded}")

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print the category result
print(f"You are classified as: {category}")


# STEP 4: FINISH THE PROGRAM

# Final message
print("\nThank you for using the BMI Calculator!")

# Optional disclaimer
# print("Note: For medical advice, please consult a healthcare provider.")



# # BMI Calculator step by step!

# In[ ]:


"""
# -------------------------------
# STEP 1: COLLECT USER INFORMATION
# -------------------------------

# Ask the user to enter their gender/sex.
# This input is just stored for now (not used in BMI calculation).
gender = input("Enter your gender (Male/Female): ")

# Ask the user to enter their weight.
# The input is taken as text, so we convert it to a number using float().
# The unit is kilograms (kg).
weight = float(input("Enter your weight in kilograms (kg): "))

# Ask the user to enter their height.
# Again, we convert it to a float.
# The unit is centimeters (cm), not meters.
height_cm = float(input("Enter your height in centimeters (cm): "))

# Print the inputs back to the user to confirm what they entered.
# This is helpful for checking if inputs are correct before calculation.
print("\n--- Input Summary ---")
print(f"Gender: {gender}")
print(f"Weight: {weight} kg")
print(f"Height: {height_cm} cm") 
"""


# BMI Formula:
# BMI =weight(kg)/(height (m))^2 
# So we have to convert height(cm) to height(m) by dividing by 100.

# In[ ]:


"""
# -------------------------------
# STEP 2: CALCULATE BMI
# -------------------------------

# Convert height from centimeters to meters
# We divide by 100 because 1 meter = 100 centimeters
height_m = height_cm / 100

# Now calculate BMI using the formula:
# BMI = weight (kg) / (height in meters)^2
bmi = weight / (height_m ** 2)

# Print the raw BMI value (we’ll round it and interpret it later)
print("\n--- BMI Calculation ---")
print(f"Height in meters: {height_m}")
print(f"Your BMI is: {bmi}")  
"""


#  BMI Categories:
# | Category      | BMI Range            |
# | ------------- | -------------------- |
# | Underweight   | Less than 18.5       |
# | Normal weight | 18.5 to less than 25 |
# | Overweight    | 25 to less than 30   |
# | Obese         | 30 and above         |
# 

# In[ ]:


"""
# -------------------------------
# STEP 3: DISPLAY RESULTS
# -------------------------------

# Round the BMI to 2 decimal places for display
# This makes the number easier to read
bmi_rounded = round(bmi, 2)

# Print the rounded BMI
#print("\n--- BMI Result ---")
#print(f"Your BMI is: {bmi_rounded}")

# Use if-elif-else to determine the BMI category
# Based on standard health ranges
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print the category result
#print(f"You are classified as: {category}") 

# The f lets you insert that variable right into the sentence/string.
"""


# In[ ]:


"""
# -------------------------------
# STEP 4: FINISH THE PROGRAM
# -------------------------------

# Print the inputs back to the user to confirm what they entered.
print("\n--- Input Summary ---")
print(f"Gender: {gender}")
print(f"Weight: {weight} kg")
print(f"Height: {height_cm} cm") 

# Print the rounded BMI
print("\n--- BMI Result ---")
print(f"Your BMI is: {bmi_rounded}") 

# Print the category result
print(f"You are classified as: {category}") 

# Print a thank-you message to the user
print("\nThank you for using the BMI Calculator!")
"""


# In[ ]:




