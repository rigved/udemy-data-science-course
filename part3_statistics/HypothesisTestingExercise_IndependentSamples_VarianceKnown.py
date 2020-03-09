"""
HypothesisTestingExercise_IndependentSamples_VarianceKnown.py
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

import math
from scipy.stats import norm

n_1 = n_2 = 25
mean_1 = 115
pvar_1 = 625
mean_2 = 100
pvar_2 = 400
confidence_level_1 = 0.90
confidence_level_2 = 0.95
confidence_level_3 = 0.99
mean_h0 = 0.00

pstd_1 = math.sqrt(pvar_1)
pstd_2 = math.sqrt(pvar_2)
standard_deviation = math.sqrt((math.pow(pstd_1, 2) / n_1) + (math.pow(pstd_2, 2) / n_2))
z_score_1 = norm.ppf(confidence_level_1)
z_score_2 = norm.ppf(confidence_level_2)
z_score_3 = norm.ppf(confidence_level_3)
Z_score = (mean_1 - mean_2 - mean_h0) / standard_deviation

print('Mean for Extreme Ajax+: {:.2f}'.format(mean_1))
print('Mean for Ajax: {:.2f}'.format(mean_2))
print('Standard Deviation for Extreme Ajax+: {:.2f}'.format(pstd_1))
print('Standard Deviation for Ajax: {:.2f}'.format(pstd_2))
print('Standard Deviation: {:.5f}'.format(standard_deviation))
print('One-tailed test z-score with {}% confidence level: {:.2f}'.format(int(confidence_level_1 * 100), z_score_1))
print('One-tailed test z-score with {}% confidence level: {:.2f}'.format(int(confidence_level_2 * 100), z_score_2))
print('One-tailed test z-score with {}% confidence level: {:.2f}'.format(int(confidence_level_2 * 100), z_score_3))
print('Z-score for the null hypothesis: {:.2f}'.format(Z_score))

decision = 'accept'
if abs(Z_score) > z_score_1:
    decision = 'reject'

print('At {}% significance, we {} the null hypothesis that Ajax cleans more dishes than Extreme Ajax+.'.format(100 - (confidence_level_1 * 100), decision))

decision = 'accept'
if abs(Z_score) > z_score_2:
    decision = 'reject'

print('At {}% significance, we {} the null hypothesis that Ajax cleans more dishes than Extreme Ajax+.'.format(100 - (confidence_level_2 * 100), decision))

decision = 'accept'
if abs(Z_score) > z_score_3:
    decision = 'reject'

print('At {}% significance, we {} the null hypothesis that the Ajax cleans more dishes than Extreme Ajax+.'.format(100 - (confidence_level_3 * 100), decision))

p_value = 1 - norm.cdf(abs(Z_score))
print('p-value for one-tailed test: {:.2f}'.format(p_value))
