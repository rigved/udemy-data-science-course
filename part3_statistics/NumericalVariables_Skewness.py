"""
NumericalVariables_Skewness.py
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
import statistics
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

raw_data1 = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 7]
max_value1 = max(raw_data1)
bin_edges1 = [i for i in range(max_value1 + 1)]
bins1 = [i for i in range(max_value1)]
data1 = pd.DataFrame({'Frequency': pd.cut(raw_data1, bin_edges1).value_counts()})
x1 = np.linspace(min(bins1), max(bins1), 250)
spl1 = make_interp_spline(bins1, data1['Frequency'])
smooth_curve1 = spl1(x1)

print(data1)
print('Mean: {:.2f}'.format(statistics.mean(raw_data1)))
print('Median: {:.2f}'.format(statistics.median(raw_data1)))
print('Mode: {:.2f}'.format(statistics.mode(raw_data1)))

raw_data2 = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7]
max_value2 = max(raw_data2)
bin_edges2 = [i for i in range(max_value2 + 1)]
bins2 = [i for i in range(max_value2)]
data2 = pd.DataFrame({'Frequency': pd.cut(raw_data2, bin_edges2).value_counts()})
x2 = np.linspace(min(bins2), max(bins2), 250)
spl2 = make_interp_spline(bins2, data2['Frequency'])
smooth_curve2 = spl2(x2)

print(data2)
print('Mean: {:.2f}'.format(statistics.mean(raw_data2)))
print('Median: {:.2f}'.format(statistics.median(raw_data2)))
print('Mode: {:.2f}'.format(statistics.mode(raw_data2)))

raw_data3 = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7]
max_value3 = max(raw_data3)
bin_edges3 = [i for i in range(max_value3 + 1)]
bins3 = [i for i in range(max_value3)]
data3 = pd.DataFrame({'Frequency': pd.cut(raw_data3, bin_edges3).value_counts()})
x3 = np.linspace(min(bins3), max(bins3), 250)
spl3 = make_interp_spline(bins3, data3['Frequency'])
smooth_curve3 = spl3(x3)

print(data3)
print('Mean: {:.2f}'.format(statistics.mean(raw_data3)))
print('Median: {:.2f}'.format(statistics.median(raw_data3)))
print('Mode: {:.2f}'.format(statistics.mode(raw_data3)))

plt.figure()

plt.subplot(311)
plt.plot(x1, smooth_curve1)
plt.title('Numerical Variables Positive Skewness')
plt.xlabel('Data')
plt.ylabel('Frequency')

plt.subplot(312)
plt.plot(x2, smooth_curve2)
plt.title('Numerical Variables No Skewness')
plt.xlabel('Data')
plt.ylabel('Frequency')

plt.subplot(313)
plt.plot(x3, smooth_curve3)
plt.title('Numerical Variables Negative Skewness')
plt.xlabel('Data')
plt.ylabel('Frequency')

plt.show()
