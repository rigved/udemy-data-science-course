"""
NumericalVariablesExercise_StandardDeviation_CoefficientOfVariation.py
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

import statistics
from scipy import stats

data1 = [62000.00, 64000.00, 49000.00, 324000.00, 1264000.00, 54330.00, 64000.00, 51000.00, 55000.00, 48000.00, 53000.00]
data2 = [62000.00, 63000.00, 76000.00, 79000.00, 67000.00, 66000.00, 69000.00, 68000.00, 57000.00, 70000.00, 67000.00]

print('Mean1: {:.2f} and Mean2: {:.2f}'.format(statistics.mean(data1), statistics.mean(data2)))
print('Median1: {:.2f} and Median2: {:.2f}'.format(statistics.median(data1), statistics.median(data2)))
print('Sample Variance1: {:.2f} and Sample Variance2: {:.2f}'.format(statistics.variance(data1), statistics.variance(data2)))
print('Sample Standard Deviation1: {:.2f} and Sample Standard Deviation2: {:.2f}'.format(statistics.stdev(data1), statistics.stdev(data2)))
print('Sample Coefficient of Variation1: {:.2f} and Sample Coefficient of Variation2: {:.2f}'.format(stats.variation(data1), stats.variation(data2)))
