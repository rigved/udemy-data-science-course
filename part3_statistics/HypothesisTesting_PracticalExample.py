"""
HypothesisTesting_PracticalExample.py
Copyright (C) 2020 Rigved Rakshit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pandas as pd
import numpy as np
from scipy.stats import t

pd.set_option('display.max_column', 25)
pd.set_option('display.width', 512)

data = pd.read_excel('data/HypothesisTesting_PracticalExample.xlsx', sheet_name='Dataset', skiprows=list(range(3)), usecols='B:K', parse_dates=[7], index_col=[1, 0], dayfirst=True)

print(data)

mean_h0 = 0.00

n_1 = data.loc[data['Gender'] == 'Male'].shape[0]
n_2 = data.loc[data['Gender'] == 'Female'].shape[0]
mean_1 = np.mean(data.loc[data['Gender'] == 'Male']['Salary'])
mean_2 = np.mean(data.loc[data['Gender'] == 'Female']['Salary'])
std_1 = np.std(data.loc[data['Gender'] == 'Male']['Salary'], ddof=1)
std_2 = np.std(data.loc[data['Gender'] == 'Female']['Salary'], ddof=1)
df = n_1 + n_2 - 2
pooled_variance = ((n_1 - 1) * np.square(std_1) + (n_2 - 1) * np.square(std_2)) / df
standard_error = np.sqrt((pooled_variance / n_1) + (pooled_variance / n_2))
T_score = (mean_1 - mean_2 - mean_h0) / standard_error
p_value = 1 - t.cdf(abs(T_score), df=df)

print('Mean for Males: ${:.2f}'.format(mean_1))
print('Mean for Females: ${:.2f}'.format(mean_2))
print('Sample standard deviation for Males: ${:.2f}'.format(std_1))
print('Sample standard deviation for Females: ${:.2f}'.format(std_2))
print('Pooled variance: {:.2f}'.format(pooled_variance))
print('Standard Error: {:.2f}'.format(standard_error))
print('T-score for null hypothesis: {:.2f}'.format(T_score))
print('p-value for null hypothesis: {:.3f}'.format(p_value))

decision = 'accept'
if p_value < 0.01:
    decision = 'reject'

print('At 1% significance level, we {} the null hypothesis that the male employees are paid less than the female employees at the Spark Fortress company.'.format(decision))

decision = 'accept'
if p_value < 0.05:
    decision = 'reject'

print('At 5% significance level, we {} the null hypothesis that the male employees are paid less than the female employees at the Spark Fortress company.'.format(decision))

decision = 'accept'
if p_value < 0.1:
    decision = 'reject'

print('At 10% significance level, we {} the null hypothesis that the male employees are paid less than the female employees at the Spark Fortress company.'.format(decision))

data_2 = pd.read_excel('data/HypothesisTesting_PracticalExample.xlsx', sheet_name='Employees below 35', skiprows=list(range(3)), usecols='B:K', parse_dates=[7], index_col=[1, 0], dayfirst=True)

print(data_2)

n_3 = data_2.loc[data_2['Gender'] == 'Male'].shape[0]
n_4 = data_2.loc[data_2['Gender'] == 'Female'].shape[0]
mean_3 = np.mean(data_2.loc[data_2['Gender'] == 'Male']['Salary'])
mean_4 = np.mean(data_2.loc[data_2['Gender'] == 'Female']['Salary'])
std_3 = np.std(data_2.loc[data_2['Gender'] == 'Male']['Salary'], ddof=1)
std_4 = np.std(data_2.loc[data_2['Gender'] == 'Female']['Salary'], ddof=1)
df_2 = n_3 + n_4 - 2
pooled_variance_2 = ((n_3 - 1) * np.square(std_3) + (n_4 - 1) * np.square(std_4)) / df_2
standard_error_2 = np.sqrt((pooled_variance_2 / n_3) + (pooled_variance_2 / n_4))
T_score_2 = (mean_3 - mean_4 - mean_h0) / standard_error_2
p_value_2 = 1 - t.cdf(abs(T_score_2), df=df_2)

print(n_3)
print(n_4)

print('Mean for Males under 35 years of age: ${:.2f}'.format(mean_3))
print('Mean for Females under 35 years of age: ${:.2f}'.format(mean_4))
print('Sample standard deviation for Males under 35 years of age: ${:.2f}'.format(std_3))
print('Sample standard deviation for Females under 35 years of age: ${:.2f}'.format(std_4))
print('Pooled variance for employees under 35 years of age: {:.2f}'.format(pooled_variance_2))
print('Standard Error for employees under 35 years of age: {:.2f}'.format(standard_error_2))
print('T-score for null hypothesis: {:.2f}'.format(T_score_2))
print('p-value for null hypothesis: {:.3f}'.format(p_value_2))

decision = 'accept'
if p_value_2 < 0.01:
    decision = 'reject'

print('At 1% significance level, we {} the null hypothesis that the male employees under 35 years of age are paid less than the female employees at the Spark Fortress company.'.format(decision))

decision = 'accept'
if p_value_2 < 0.05:
    decision = 'reject'

print('At 5% significance level, we {} the null hypothesis that the male employees under 35 years of age are paid less than the female employees at the Spark Fortress company.'.format(decision))

decision = 'accept'
if p_value_2 < 0.1:
    decision = 'reject'

print('At 10% significance level, we {} the null hypothesis that the male employees under 35 years of age are paid less than the female employees at the Spark Fortress company.'.format(decision))

data_3 = pd.read_excel('data/HypothesisTesting_PracticalExample.xlsx', sheet_name='Employees over 35', skiprows=list(range(3)), usecols='B:K', parse_dates=[7], index_col=[1, 0], dayfirst=True)

print(data_3)

n_5 = data_3.loc[data_3['Gender'] == 'Male'].shape[0]
n_6 = data_3.loc[data_3['Gender'] == 'Female'].shape[0]
mean_5 = np.mean(data_3.loc[data_3['Gender'] == 'Male']['Salary'])
mean_6 = np.mean(data_3.loc[data_3['Gender'] == 'Female']['Salary'])
std_5 = np.std(data_3.loc[data_3['Gender'] == 'Male']['Salary'], ddof=1)
std_6 = np.std(data_3.loc[data_3['Gender'] == 'Female']['Salary'], ddof=1)
df_3 = n_5 + n_6 - 2
pooled_variance_3 = ((n_5 - 1) * np.square(std_5) + (n_6 - 1) * np.square(std_6)) / df_3
standard_error_3 = np.sqrt((pooled_variance_3 / n_5) + (pooled_variance_3 / n_6))
T_score_3 = (mean_5 - mean_6 - mean_h0) / standard_error_3
p_value_3 = 1 - t.cdf(abs(T_score_3), df=df_3)

print('Mean for Males over 35 years of age: ${:.2f}'.format(mean_5))
print('Mean for Females over 35 years of age: ${:.2f}'.format(mean_6))
print('Sample standard deviation for Males over 35 years of age: ${:.2f}'.format(std_5))
print('Sample standard deviation for Females over 35 years of age: ${:.2f}'.format(std_6))
print('Pooled variance for employees over 35 years of age: {:.2f}'.format(pooled_variance_3))
print('Standard Error for employees over 35 years of age: {:.2f}'.format(standard_error_3))
print('T-score for null hypothesis: {:.2f}'.format(T_score_3))
print('p-value for null hypothesis: {:.3f}'.format(p_value_3))

decision = 'accept'
if p_value_3 < 0.01:
    decision = 'reject'

print('At 1% significance level, we {} the null hypothesis that the male employees over 35 years of age are paid less than the female employees at the Spark Fortress company.'.format(decision))

decision = 'accept'
if p_value_3 < 0.05:
    decision = 'reject'

print('At 5% significance level, we {} the null hypothesis that the male employees over 35 years of age are paid less than the female employees at the Spark Fortress company.'.format(decision))

decision = 'accept'
if p_value_3 < 0.1:
    decision = 'reject'

print('At 10% significance level, we {} the null hypothesis that the male employees over 35 years of age are paid less than the female employees at the Spark Fortress company.'.format(decision))
