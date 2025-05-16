# BMI Calculator Project

## Description
This project is a simple Body Mass Index (BMI) calculator implemented in Python. It allows users to input their gender, weight in kilograms, and height in centimeters, then calculates their BMI and classifies it into one of the standard health categories: Underweight, Normal weight, Overweight, or Obese.

## Features
- Collects user inputs for gender, weight (kg), and height (cm)
- Converts height from centimeters to meters
- Calculates BMI using the formula: `BMI = weight (kg) / (height in meters)^2`
- Classifies BMI into standard health categories
- Provides a clear summary of inputs and results
- User-friendly interface with step-by-step output

## BMI Categories
| Category      | BMI Range            |
| ------------- | -------------------- |
| Underweight   | Less than 18.5       |
| Normal weight | 18.5 to less than 25 |
| Overweight    | 25 to less than 30   |
| Obese         | 30 and above         |

## Usage
1. Run the Jupyter Notebook file `BMI Calculator Project.ipynb`.
2. Enter your gender (Male/Female) when prompted.
3. Enter your weight in kilograms (kg).
4. Enter your height in centimeters (cm).
5. The program will display:
   - A summary of your inputs
   - Your calculated BMI
   - Your BMI classification
   - A thank-you message

## Example Output
```
Enter your gender (Male/Female): Male
Enter your weight in kilograms (kg): 76
Enter your height in centimeters (cm): 173

--- Input Summary ---
Gender: Male
Weight: 76.0 kg
Height: 173.0 cm

--- BMI Calculation ---
Height in meters: 1.73
Your BMI is: 25.393431120318084

--- BMI Result ---
Your BMI is: 25.39
You are classified as: Overweight

Thank you for using the BMI Calculator!
```

## Requirements
- Python 3.x
- Jupyter Notebook (optional, for running the notebook file)

## Author
Motlalepula Lawrence Tshabalala  
Date: 2025/05/09

## Notes
- This calculator uses metric units (kilograms and centimeters).
- For medical advice, please consult a healthcare provider.
- The gender input is collected but not used in BMI calculation as BMI formulas are the same for all adults regardless of gender.
