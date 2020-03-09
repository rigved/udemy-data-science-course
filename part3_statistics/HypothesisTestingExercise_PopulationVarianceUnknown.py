"""
HypothesisTestingExercise_PopulationVarianceUnknown.py
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
from scipy.stats import t, ttest_1samp

data = pd.read_excel('data/HypothesisTestingExercise_PopulationVarianceUnknown.xlsx', sheet_name='Open rate dataset', skiprows=list(range(11)), usecols='B', skipfooter=2)
confidence_level_1 = 0.95
confidence_level_2 = 0.99
mean_h0 = 0.4

mean = np.mean(data)
standard_error = np.std(data, ddof=1).values[0] / np.sqrt(data.shape[0])
t_score_1 = t.ppf(np.around(1 - ((1 - confidence_level_1) / 2), 3), df=(data.shape[0] - 1))
t_score_2 = t.ppf(np.around(1 - ((1 - confidence_level_2) / 2), 3), df=(data.shape[0] - 1))
T_score = (mean.values[0] - mean_h0) / standard_error
t_statistic, p_value = ttest_1samp(data, mean_h0)

print(data)
print('Mean: {:.2f}'.format(mean.values[0]))
print('Standard Error: {:.2f}'.format(standard_error))
print('Two-sided test t-score for {}% confidence level with {} degrees of freedom: {:.2f}'.format(int(confidence_level_1 * 100), data.shape[0] - 1, t_score_1))
print('Two-sided test t-score for {}% confidence level with {} degrees of freedom: {:.2f}'.format(int(confidence_level_2 * 100), data.shape[0] - 1, t_score_2))
print('T-score for the null hypothesis: {:.2f}'.format(T_score))

decision = 'accept'
if abs(T_score) > t_score_1:
    decision = 'reject'

print('At 5% significance in a two-sided test, we ' + decision + ' the null hypothesis that the average open rate for our emails is {}%.'.format(mean_h0 * 100))

decision = 'accept'
if abs(T_score) > t_score_2:
    decision = 'reject'

print('At 1% significance in a two-sided test, we ' + decision + ' the null hypothesis that the average open rate for our emails is {}%'.format(mean_h0 * 100))

print('T-statistic for two-sided test: {:.2f}'.format(t_statistic[0]))
print('p-value for two-sided test: {:.3f}'.format(p_value[0]))
