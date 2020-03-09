"""
NumericalVariables_StandardDeviation_CoefficientOfVariation.py
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

data1 = [1.00, 2.00, 3.00, 3.00, 5.00, 6.00, 7.00, 8.00, 9.00, 11.00]
data2 = [18.81, 37.62, 56.43, 56.43, 94.05, 112.86, 131.67, 150.48, 169.29, 206.91]

print('Mean1: {:.2f} and Mean2: {:.2f}'.format(statistics.mean(data1), statistics.mean(data2)))
print('Sample Variance1: {:.2f} and Sample Variance2: {:.2f}'.format(statistics.variance(data1), statistics.variance(data2)))
print('Sample Standard Deviation1: {:.2f} and Sample Standard Deviation2: {:.2f}'.format(statistics.stdev(data1), statistics.stdev(data2)))
print('Sample Coefficient of Variation1: {:.2f} and Sample Coefficient of Variation2: {:.2f}'.format(stats.variation(data1), stats.variation(data2)))
