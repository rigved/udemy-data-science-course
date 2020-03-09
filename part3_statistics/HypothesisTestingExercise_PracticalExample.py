"""
HypothesisTestingExercise_PracticalExample.py
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
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 512)

data_1 = pd.read_excel('data/HypothesisTestingExercise_PracticalExample.xlsx', sheet_name='Nonwhite', skiprows=list(range(3)), usecols='B:K', parse_dates=[7], index_col=[1, 0], dayfirst=True)
data_1['Ethnicity'] = 'Non-white'
data_2 = pd.read_excel('data/HypothesisTestingExercise_PracticalExample.xlsx', sheet_name='White', skiprows=list(range(3)), usecols='B:K', parse_dates=[7], index_col=[1, 0], dayfirst=True, skipfooter=62)
data_2['Ethnicity'] = 'White'
data = pd.concat([data_1[['Ethnicity', 'Salary']], data_2[['Ethnicity', 'Salary']]])

print(data)

print('H0: White employees and non-white employees are paid the same.\nH0: Salary[White] - Salary[Non-white] = 0')
mean_h0 = 0.00

n_1 = data.loc[data['Ethnicity'] == 'Non-white'].shape[0]
n_2 = data.loc[data['Ethnicity'] == 'White'].shape[0]
mean_1 = np.mean(data.loc[data['Ethnicity'] == 'Non-white']['Salary'])
mean_2 = np.mean(data.loc[data['Ethnicity'] == 'White']['Salary'])
std_1 = np.std(data.loc[data['Ethnicity'] == 'Non-white']['Salary'], ddof=1)
std_2 = np.std(data.loc[data['Ethnicity'] == 'White']['Salary'], ddof=1)
df = n_1 + n_2 - 2
pooled_variance = ((n_1 - 1) * np.square(std_1) + (n_2 - 1) * np.square(std_2)) / df
standard_error = np.sqrt((pooled_variance / n_1) + (pooled_variance / n_2))
T_score = (mean_1 - mean_2 - mean_h0) / standard_error
p_value = 2 * (1 - t.cdf(abs(T_score), df=df))

print('Mean for non-white employees: ${:.2f}'.format(mean_1))
print('Mean for white employees: ${:.2f}'.format(mean_2))
print('Sample standard deviation for non-white employees: ${:.2f}'.format(std_1))
print('Sample standard deviation for white employees: ${:.2f}'.format(std_2))
print('Pooled variance: {:.2f}'.format(pooled_variance))
print('Standard Error: {:.2f}'.format(standard_error))
print('T-score for null hypothesis: {:.2f}'.format(T_score))
print('p-value for null hypothesis: {:.3f}'.format(p_value))

decision = 'accept'
if p_value < 0.01:
    decision = 'reject'

print('At 1% significance level, we {} the null hypothesis that white employees and non-white employees are paid the same.'.format(decision))

decision = 'accept'
if p_value < 0.05:
    decision = 'reject'

print('At 5% significance level, we {} the null hypothesis that white employees and non-white employees are paid the same.'.format(decision))

decision = 'accept'
if p_value < 0.1:
    decision = 'reject'

print('At 10% significance level, we {} the null hypothesis that white employees and non-white employees are paid the same.'.format(decision))
