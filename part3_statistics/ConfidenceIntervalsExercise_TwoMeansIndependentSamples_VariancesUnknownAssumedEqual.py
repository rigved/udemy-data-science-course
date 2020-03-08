"""
ConfidenceIntervalsExercise_TwoMeansIndependentSamples_VariancesUnknownAssumedEqual.py
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

data = pd.read_excel('data/ConfidenceIntervalsExercise_TwoMeansIndependentSamples_VariancesUnknownAssumedEqual.xlsx', sheet_name='CI, indep, var unkwn', skiprows=list(range(8)), usecols='B:C')
confidence_level = 0.90

mean_1 = np.mean(data['NY apples'])
mean_2 = np.mean(data['LA apples'])
std_1 = np.std(data['NY apples'], ddof=1)
std_2 = np.std(data['LA apples'], ddof=1)
df = data['NY apples'].shape[0] + data['LA apples'].shape[0] - 2
pooled_variance = (((data['NY apples'].shape[0] - 1) * np.square(std_1)) + ((data['LA apples'].shape[0] - 1) * np.square(std_2))) / df
pooled_std = np.sqrt(pooled_variance)
t_score = t.ppf(np.around(1 - ((1 - confidence_level) / 2), 3), df=df)
std_err = np.sqrt((pooled_variance / data['NY apples'].shape[0]) + (pooled_variance / data['LA apples'].shape[0]))

print('Mean of NY apples: ${:.2f}'.format(mean_1))
print('Mean of LA apples: ${:.2f}'.format(mean_2))
print('Pooled variance: {:.2f}'.format(pooled_variance))
print('Standard Deviation of NY apples: ${:.2f}'.format(std_1))
print('Standard Deviation of LA apples: ${:.2f}'.format(std_2))
print('Pooled standard deviation: ${:.2f}'.format(pooled_std))
print('Standard Error: {:.2f}'.format(std_err))
print('t-score for 90% confidence and {} degrees of freedom: {:.2f}'.format(df, t_score))
print('Confidence Interval with 90% confidence and {} degrees of freedom: ({:.2f}, {:.2f})'.format(df, (mean_1 - mean_2) - (t_score * std_err), (mean_1 - mean_2) + (t_score * std_err)))
