"""
NumericalVariablesExercise_Variance.py
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

data = [62000.00, 64000.00, 49000.00, 324000.00, 1264000.00, 54330.00, 64000.00, 51000.00, 55000.00, 48000.00, 53000.00]

print('Mean: {:.2f}'.format(statistics.mean(data)))
print('Sample Variance: {:.2f}'.format(statistics.variance(data)))
print('Population variance: {:.2f}'.format(statistics.pvariance(data)))
