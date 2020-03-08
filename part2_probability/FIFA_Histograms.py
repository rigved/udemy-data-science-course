"""
FIFA_Histograms.py
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

csv_data = pd.read_csv('data/FIFA.csv')
csv_data_small = csv_data.iloc[:30].copy()
overall = csv_data['Overall'].values
overall_small = csv_data_small['Overall'].values
shot_power = csv_data['ShotPower'].values
gk_diving = csv_data['GKDiving'].values
age = csv_data['Age'].values

plt.figure()
plt.subplot(721)
plt.xlim([min(overall) - 5, max(overall) + 5])
plt.hist(overall, bins=range(min(overall), max(overall) + 1, 1), rwidth=0.9)
plt.title('Overall')
plt.xlabel('Overall')
plt.ylabel('Count')

plt.subplot(725)
plt.xlim([min(overall_small) - 5, max(overall_small) + 5])
plt.hist(overall_small, bins=range(min(overall_small), max(overall_small) + 1, 1), rwidth=0.9)
plt.title('Sample Overall')
plt.xlabel('Sample Overall')
plt.ylabel('Sample Count')

plt.subplot(726)
plt.xlim([min(overall_small) - 5, max(overall_small) + 5])
plt.hist(overall_small, bins=range(min(overall_small), max(overall_small) + 3, 3), rwidth=0.9)
plt.title('Sample Overall with larger bin size')
plt.xlabel('Sample Overall')
plt.ylabel('Sample Count')

plt.subplot(729)
plt.xlim([min(shot_power) - 5, max(shot_power) + 5])
plt.hist(shot_power, bins=range(np.int(min(shot_power)), np.int(max(shot_power)) + 1, 1), rwidth=0.9)
plt.title('Shot Power')
plt.xlabel('Shot Power')
plt.ylabel('Count')

plt.subplot(7, 2, 10)
plt.xlim([min(gk_diving) - 5, max(gk_diving) + 5])
plt.hist(gk_diving, bins=range(np.int(min(gk_diving)), np.int(max(gk_diving)) + 1, 1), rwidth=0.9)
plt.title('GK Diving')
plt.xlabel('GK Diving')
plt.ylabel('Count')

plt.subplot(7, 2, 13)
plt.xlim([min(age) - 5, max(age) + 5])
plt.hist(age, bins=range(min(age), max(age) + 1, 1), rwidth=0.9)
plt.title('Age')
plt.xlabel('Age')
plt.ylabel('Count')

plt.show()
