"""
HypothesisTesting_IndependentSamples_VarianceUnknownAssumedEqual.py
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

data = pd.read_excel('data/HypothesisTesting_IndependentSamples_VarianceUnknownAssumedEqual.xlsx', sheet_name='Data', skiprows=list(range(3)), usecols='B:C')

confidence_level_1 = 0.90
confidence_level_2 = 0.95
confidence_level_3 = 0.99
mean_h0 = 0.00

mean_1 = np.mean(data['NY apples'])
std_1 = np.std(data['NY apples'], ddof=1)
mean_2 = np.mean(data['LA apples'])
std_2 = np.std(data['LA apples'], ddof=1)
df = data['NY apples'].shape[0] + data['LA apples'].shape[0] - 2
pooled_variance = (((data['NY apples'].shape[0] - 1) * np.square(std_1)) + ((data['LA apples'].shape[0] - 1) * np.square(std_2))) / df
std_err = np.sqrt((pooled_variance / data['NY apples'].shape[0]) + (pooled_variance / data['LA apples'].shape[0]))
t_score_1 = t.ppf(np.around(1 - ((1 - confidence_level_1) / 2), 3), df=df)
t_score_2 = t.ppf(np.around(1 - ((1 - confidence_level_2) / 2), 3), df=df)
t_score_3 = t.ppf(np.around(1 - ((1 - confidence_level_3) / 2), 3), df=df)
T_score = (mean_1 - mean_2 - mean_h0) / std_err

print('Mean for NY apples: ${:.2f}'.format(mean_1))
print('Mean for LA apples: ${:.2f}'.format(mean_2))
print('Standard Deviation for NY apples: ${:.2f}'.format(std_1))
print('Standard Deviation for LA apples: ${:.2f}'.format(std_2))
print('One-tailed test t-score with {}% confidence level: {:.2f}'.format(int(confidence_level_1 * 100), t_score_1))
print('One-tailed test t-score with {}% confidence level: {:.2f}'.format(int(confidence_level_2 * 100), t_score_2))
print('One-tailed test t-score with {}% confidence level: {:.2f}'.format(int(confidence_level_3 * 100), t_score_3))
print('T-score for the null hypothesis: {:.2f}'.format(T_score))

decision = 'accept'
if abs(T_score) > t_score_1:
    decision = 'reject'

print('At {}% significance, we {} the null hypothesis that the cost of apples in LA is higher than the cost in NY.'.format(100 - (confidence_level_1 * 100), decision, abs(mean_h0) * 100))

decision = 'accept'
if abs(T_score) > t_score_2:
    decision = 'reject'

print('At {}% significance, we {} the null hypothesis that the cost of apples in LA is higher than the cost in NY.'.format(100 - (confidence_level_2 * 100), decision, abs(mean_h0) * 100))

decision = 'accept'
if abs(T_score) > t_score_3:
    decision = 'reject'

print('At {}% significance, we {} the null hypothesis that the cost of apples in LA is higher than the cost in NY.'.format(100 - (confidence_level_3 * 100), decision, abs(mean_h0) * 100))

p_value = 1 - t.cdf(abs(T_score), df=df)
print('p-value for one-tailed test: {:.3f}'.format(p_value))
