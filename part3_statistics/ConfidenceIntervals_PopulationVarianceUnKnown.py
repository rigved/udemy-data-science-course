"""
ConfidenceIntervals_PopulationVarianceUnKnown.py
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

data = pd.read_excel('data/ConfidenceIntervals_PopulationVarianceUnknown.xlsx', sheet_name='Salaries', skiprows=list(range(3)), usecols='B')
confidence_level = 0.95

mean = np.mean(data['Dataset'])
std = np.std(data['Dataset'], ddof=1)
std_err = std / np.sqrt(data['Dataset'].shape[0])
t_score = t.ppf(np.around(1 - ((1 - confidence_level) / 2), 3), df=(data['Dataset'].shape[0] - 1))

print('Mean: {:.2f}'.format(mean))
print('Standard Deviation: {:.2f}'.format(std))
print('Standard Error: {:.2f}'.format(std_err))
print('t-score for 95% confidence and {} degrees of freedom: {:.2f}'.format(data['Dataset'].shape[0] - 1, t_score))
print('Confidence Interval with 95% confidence and {} degrees of freedom: ({:.2f}, {:.2f})'.format(data['Dataset'].shape[0] - 1, mean - (t_score * std_err), mean + (t_score * std_err)))
