"""
NumericalVariablesExercise_Histogram.py
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
from matplotlib import pyplot as plt

raw_data = [13, 68, 165, 193, 216, 228, 361, 470, 500, 529, 544, 602, 647, 692, 696, 699, 809, 892, 899, 936]
num_bins = 10
width = (max(raw_data) - min(raw_data) + 1) / num_bins
x_labels = ['({:.2f}, {:.2f}]'.format(min(raw_data) - 1.0, min(raw_data) + width)]
x_labels.extend(['({:.2f}, {:.2f}]'.format(i, i + width) for i in np.arange(min(raw_data) + width, max(raw_data), width)])
bin_edges = [min(raw_data) - 1.0]
bin_edges.extend([i for i in np.arange(min(raw_data) + width, max(raw_data) + width + 1.0, width)])
data = pd.DataFrame({'Frequency': pd.cut(raw_data, bin_edges).value_counts()})
data['Relative Frequency'] = data['Frequency'] / data['Frequency'].sum()

print(data)

plt.figure()
plt.subplot(111)
plt.bar(x_labels, data['Relative Frequency'].values, width=1.0)
plt.ylim(0.0, max(data['Relative Frequency'].values) + 0.1)
plt.title('Numerical Variables Histogram')
plt.xlabel('Bins')
plt.ylabel('Relative Frequency')

plt.show()
