"""
ConfidenceIntervals_TwoMeansIndependentSamples_VarianceKnown.py
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
from scipy.stats import norm

n_1 = 100
n_2 = 70
mean_1 = 58
mean_2 = 65
pstd_1 = 10
pstd_2 = 5
confidence_level = 0.95

mean = mean_1 - mean_2
std = np.sqrt((np.square(pstd_1) / n_1) + (np.square(pstd_2) / n_2))
z_score = norm.ppf(np.around(1 - ((1 - confidence_level) / 2), 3))

print('Mean: {:.2f}'.format(mean))
print('Standard Deviation: {:.2f}'.format(std))
print('z-score for 95% confidence: {:.2f}'.format(z_score))
print('Confidence Interval with 95% confidence: ({:.2f}, {:.2f})'.format((mean_1 - mean_2) - (z_score * std), (mean_1 - mean_2) + (z_score * std)))
