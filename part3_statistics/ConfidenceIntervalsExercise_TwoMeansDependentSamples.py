"""
ConfidenceIntervalsExercise_TwoMeansDependentSamples.py
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
from scipy.stats import t

data = pd.read_excel('data/ConfidenceIntervalsExercise_TwoMeansDependentSamples.xlsx', sheet_name='Data in kg', skiprows=list(range(13)), index_col=0, usecols='B:D')
data['Difference'] = data['Weight after (kg)'] - data['Weight before (kg)']
confidence_level_1 = 0.90
confidence_level_2 = 0.95
confidence_level_3 = 0.99

mean = np.mean(data['Difference'])
std = np.std(data['Difference'], ddof=1)
std_err = std / np.sqrt(data['Difference'].shape[0])
t_score_1 = t.ppf(np.around(1 - ((1 - confidence_level_1) / 2), 3), df=(data['Difference'].shape[0] - 1))
t_score_2 = t.ppf(np.around(1 - ((1 - confidence_level_2) / 2), 3), df=(data['Difference'].shape[0] - 1))
t_score_3 = t.ppf(np.around(1 - ((1 - confidence_level_3) / 2), 3), df=(data['Difference'].shape[0] - 1))

print('Mean: {:.2f}'.format(mean))
print('Standard Deviation: {:.2f}'.format(std))
print('Standard Error: {:.2f}'.format(std_err))
print('t-score for 90% confidence and {} degrees of freedom: {:.2f}'.format(data['Difference'].shape[0] - 1, t_score_1))
print('t-score for 95% confidence and {} degrees of freedom: {:.2f}'.format(data['Difference'].shape[0] - 1, t_score_2))
print('t-score for 99% confidence and {} degrees of freedom: {:.2f}'.format(data['Difference'].shape[0] - 1, t_score_3))
print('Confidence Interval with 90% confidence and {} degrees of freedom: ({:.2f}, {:.2f})'.format(data['Difference'].shape[0] - 1, mean - (t_score_1 * std_err), mean + (t_score_1 * std_err)))
print('Confidence Interval with 95% confidence and {} degrees of freedom: ({:.2f}, {:.2f})'.format(data['Difference'].shape[0] - 1, mean - (t_score_2 * std_err), mean + (t_score_2 * std_err)))
print('Confidence Interval with 99% confidence and {} degrees of freedom: ({:.2f}, {:.2f})'.format(data['Difference'].shape[0] - 1, mean - (t_score_3 * std_err), mean + (t_score_3 * std_err)))
