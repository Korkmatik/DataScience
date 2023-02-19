# Cyber Security Salaries

This is an analysis of Cyber Security Salaries in the U.S. The full article can be found on Medium.

# Project structure
- 01_cyber_security_salaries_us_data_cleanup.ipynb: Basic exploratorative analysis and cleaning data
- 02_us_data_analysis.ipynb: Analysis of U.S. Cyber Security Salaries
- 03_model_development.ipynb: Building and comparing various models
- salaries_cyber_us_cleaned.csv: Cleaned data containing only US salaries
- salaries_cyber_model.csv: Data for training models

# Example ML Pipeline

You can download the model and the scaler from the releases page. After that you can make predictions with the following pipeline:

```python
import pickle

f = open("./models/linear_regression.sav", "rb")
model = pickle.load(f)
f.close()

f = open("./models/standard_scalar.sav", "rb")
standard_scaler = pickle.load(f)
f.close()

# Predicting salary for junior professionals working at a large size company
y_pred = model.predict( [[1, 0, 0, 0, 1, 0, 0]] )
salary = standard_scaler.inverse_transform( y_pred )
print(salary)
```