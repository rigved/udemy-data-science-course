"""
ConfidenceIntervalsExercise_PopulationVarianceKnown.py
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

data = pd.read_excel('data/ConfidenceIntervalsExercise_PopulationVarianceKnown.xlsx', sheet_name='CI', skiprows=list(range(9)), usecols='B')
confidence_level = 0.90

mean = np.mean(data['Dataset'])
std = 15000.00
std_err = std / np.sqrt(data['Dataset'].shape[0])
z_score = norm.ppf(np.around(1 - ((1 - confidence_level) / 2), 3))

print('Mean: {:.2f}'.format(mean))
print('Standard Deviation: {:.2f}'.format(std))
print('Standard Error: {:.2f}'.format(std_err))
print('Z-score for 90% confidence: {:.2f}'.format(z_score))
print('Confidence Interval with 90% confidence: ({:.2f}, {:.2f})'.format(mean - (z_score * std_err), mean + (z_score * std_err)))
