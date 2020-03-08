"""
ConfidenceIntervals_PopulationVarianceKnown.py
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

import numpy as np
import pandas as pd
from scipy.stats import norm

data = pd.read_excel('data/ConfidenceIntervals_PopulationVarianceKnown.xlsx', sheet_name='CI', skiprows=list(range(4)), usecols='B')
confidence_level_1 = 0.95
confidence_level_2 = 0.99

mean = np.mean(data['Dataset'])
std = 15000.00
std_err = std / np.sqrt(data['Dataset'].shape[0])
z_score_1 = norm.ppf(np.around(1 - ((1 - confidence_level_1) / 2), 3))
z_score_2 = norm.ppf(np.around(1 - ((1 - confidence_level_2) / 2), 3))

print('Mean: {:.2f}'.format(mean))
print('Standard Deviation: {:.2f}'.format(std))
print('Standard Error: {:.2f}'.format(std_err))
print('Z-score for 95% confidence: {:.2f}'.format(z_score_1))
print('Z-score for 99% confidence: {:.2f}'.format(z_score_2))
print('Confidence Interval with 95% confidence: ({:.2f}, {:.2f})'.format(mean - (z_score_1 * std_err), mean + (z_score_1 * std_err)))
print('Confidence Interval with 99% confidence: ({:.2f}, {:.2f})'.format(mean - (z_score_2 * std_err), mean + (z_score_2 * std_err)))
