"""
NumericalVariablesExercise_Skewness.py
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
import numpy as np
import pandas as pd
import statistics
from scipy.stats import skew
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

raw_data1 = [212, 869, 220, 654, 11, 624, 420, 121, 428, 865, 799, 405, 230, 670, 870, 366, 99, 55, 489, 312, 493, 163, 221, 84, 144, 48, 375, 86, 168, 100]
min_value1 = min(raw_data1)
max_value1 = max(raw_data1)
step1 = math.ceil((max_value1 - min_value1) / 10)
bin_edges1 = [i for i in range(min_value1 - 1, max_value1 + 1, step1)]
bins1 = [i for i in range(min_value1, max_value1 + 1, step1)]
if max(bin_edges1) < max_value1:
    bin_edges1.append(max(bin_edges1) + step1)
data1 = pd.DataFrame({'Frequency': pd.cut(raw_data1, bin_edges1).value_counts()})
x1 = np.linspace(min(bins1), max(bins1), 250)
spl1 = make_interp_spline(bins1, data1['Frequency'].values)
smooth_curve1 = spl1(x1)

print(data1)
mean1 = statistics.mean(raw_data1)
median1 = statistics.median(raw_data1)
print('Mean: {:.2f}'.format(mean1))
print('Median: {:.2f}'.format(median1))
try:
    print('Mode: {:.2f}'.format(statistics.mode(raw_data1)))
except Exception as e:
    print(e)
skewness1 = skew(raw_data1)
if mean1 > median1:
    print('Positive Skewness: ' + str(skewness1))
elif mean1 < median1:
    print('Negative Skewness: ' + str(skewness1))
else:
    print('No skewness: ' + str(skewness1))

raw_data2 = [586, 760, 495, 678, 559, 415, 370, 659, 119, 288, 241, 787, 522, 207, 160, 526, 656, 848, 720, 676, 581, 929, 653, 661, 770, 800, 529, 975, 995, 947]
min_value2 = min(raw_data2)
max_value2 = max(raw_data2)
step2 = math.ceil((max_value2 - min_value2) / 10)
bin_edges2 = [i for i in range(min_value2 - 1, max_value2 + 1, step2)]
bins2 = [i for i in range(min_value2, max_value2 + 1, step2)]
if max(bin_edges2) < max_value2:
    bin_edges2.append(max(bin_edges2) + step2)
data2 = pd.DataFrame({'Frequency': pd.cut(raw_data2, bin_edges2).value_counts()})
x2 = np.linspace(min(bins2), max(bins2), 1000)
spl2 = make_interp_spline(bins2, data2['Frequency'].values)
smooth_curve2 = spl2(x2)

print(data2)
mean2 = statistics.mean(raw_data2)
median2 = statistics.median(raw_data2)
print('Mean: {:.2f}'.format(mean2))
print('Median: {:.2f}'.format(median2))
try:
    print('Mode: {:.2f}'.format(statistics.mode(raw_data2)))
except Exception as e:
    print(e)
skewness2 = skew(raw_data2)
if mean2 > median2:
    print('Positive Skewness: ' + str(skewness2))
elif mean2 < median2:
    print('Negative Skewness: ' + str(skewness2))
else:
    print('No skewness: ' + str(skewness2))

plt.figure()

plt.subplot(211)
plt.plot(x1, smooth_curve1)
plt.title('Numerical Variables Exercise Skewness')
plt.xlabel('Data')
plt.ylabel('Frequency')

plt.subplot(212)
plt.plot(x2, smooth_curve2)
plt.title('Numerical Variables Exercise Skewness')
plt.xlabel('Data')
plt.ylabel('Frequency')

plt.show()
