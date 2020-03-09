"""
HypothesisTestingExercise_DependentSamples.py
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
from scipy.stats import t, ttest_rel

data = pd.read_excel('data/HypothesisTestingExercise_DependentSamples.xlsx', sheet_name='Weight-loss data, kg', skiprows=list(range(10)), usecols='B:C')
confidence_level_1 = 0.99
confidence_level_2 = 0.95
confidence_level_3 = 0.90
mean_h0 = 0.0

data['Difference'] = np.around(data['After (kg)'] - data['Before (kg)'], 2)
mean = np.mean(data['Difference'])
standard_error = np.std(data['Difference'], ddof=1) / np.sqrt(data.shape[0])
t_score_1 = t.ppf(confidence_level_1, df=(data.shape[0] - 1))
t_score_2 = t.ppf(confidence_level_2, df=(data.shape[0] - 1))
t_score_3 = t.ppf(confidence_level_3, df=(data.shape[0] - 1))
T_score = (mean - mean_h0) / standard_error
t_statistic, p_value = ttest_rel(data['After (kg)'], data['Before (kg)'])

print(data)
print('Mean: {:.2f}'.format(mean))
print('Standard Error: {:.2f}'.format(standard_error))
print('One-tailed test t-score for {}% confidence level with {} degrees of freedom: {:.2f}'.format(int(confidence_level_1 * 100), data.shape[0] - 1, t_score_1))
print('One-tailed test t-score for {}% confidence level with {} degrees of freedom: {:.2f}'.format(int(confidence_level_2 * 100), data.shape[0] - 1, t_score_2))
print('One-tailed test t-score for {}% confidence level with {} degrees of freedom: {:.2f}'.format(int(confidence_level_3 * 100), data.shape[0] - 1, t_score_3))
print('T-score for the null hypothesis: {:.2f}'.format(T_score))

decision = 'accept'
if abs(T_score) > t_score_1:
    decision = 'reject'

print('At 1% significance in a one-tailed test, we ' + decision + ' the null hypothesis that the participants have gained weight.')

decision = 'accept'
if abs(T_score) > t_score_2:
    decision = 'reject'

print('At 5% significance in a one-tailed test, we ' + decision + ' the null hypothesis that the participants have gained weight.')

decision = 'accept'
if abs(T_score) > t_score_2:
    decision = 'reject'

print('At 10% significance in a one-tailed test, we ' + decision + ' the null hypothesis that the participants have gained weight.')

print('T-statistic for one-tailed test: {:.2f}'.format(t_statistic))
print('p-value for one-tailed test: {:.3f}'.format(p_value / 2))
