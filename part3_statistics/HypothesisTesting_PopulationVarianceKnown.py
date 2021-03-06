"""
HypothesisTesting_PopulationVarianceKnown.py
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
from scipy.stats import norm

data = pd.read_excel('data/HypothesisTesting_PopulationVarianceKnown.xlsx', sheet_name='Data', skiprows=[0, 1, 2], usecols='B')
confidence_level_1 = 0.95
confidence_level_2 = 0.99
population_std = 15000
mean_h0 = 113000

mean = np.mean(data)
standard_error = population_std / np.sqrt(data.shape[0])
z_score_1 = norm.ppf(np.around(1 - ((1 - confidence_level_1) / 2), 3))
z_score_2 = norm.ppf(np.around(1 - ((1 - confidence_level_2) / 2), 3))
Z_score = (mean.values[0] - mean_h0) / standard_error

print(data)
print('Mean: {:.2f}'.format(mean.values[0]))
print('Standard Error: {:.2f}'.format(standard_error))
print('z-score for {}% confidence level: {:.2f}'.format(int(confidence_level_1 * 100), z_score_1))
print('z-score for {}% confidence level: {:.2f}'.format(int(confidence_level_2 * 100), z_score_2))
print('Z-score: {:.2f}'.format(Z_score))

decision = 'accept'
if abs(Z_score) > z_score_1:
    decision = 'reject'

print('At 5% significance, we ' + decision + ' the null hypothesis that the average salary of a Data Scientist is $113,000.')

decision = 'accept'
if abs(Z_score) > z_score_2:
    decision = 'reject'

print('At 1% significance, we ' + decision + ' the null hypothesis that the average salary of a Data Scientist is $113,000.')
