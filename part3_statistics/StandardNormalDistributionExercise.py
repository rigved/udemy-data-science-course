"""
StandardNormalDistributionExercise.py
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
from matplotlib import pyplot as plt
import matplotlib as mpl

original_distribution = [567.45, 572.45, 572.45, 589.12, 613.87, 615.78, 628.45, 644.87, 650.45, 652.20, 656.87, 661.45, 666.45, 667.70, 668.95,675.28, 675.78, 685.53, 694.28, 697.62, 705.78, 705.87, 708.12, 711.03, 714.03, 716.03, 722.28, 728.12, 728.70, 729.03, 730.12, 731.95, 735.03, 736.95, 737.37, 738.28, 739.78, 740.62, 743.62, 747.20, 748.20, 748.28, 748.53, 750.03, 752.12, 754.70, 755.03, 758.37, 760.53, 764.03, 769.28, 775.45, 781.20, 781.70, 785.62, 792.78, 793.37, 795.28, 797.62, 798.95, 799.70, 799.95, 810.87, 811.53, 813.62, 814.03, 814.78, 817.87, 818.87, 820.70, 821.12, 825.62, 828.62, 841.45, 842.03, 842.87, 849.62, 874.70, 878.78, 897.45]

original_mean = np.mean(original_distribution)
original_stdev = np.std(original_distribution)
temp_distribution = original_distribution - original_mean
converted_standard_normal_distribution = temp_distribution / original_stdev

print('Original Distribution - Mean and Standard Deviation:                                     {:.2f}, {:.2f}'.format(original_mean, original_stdev))
print('Temporary Distribution (Subtract Mean) - Mean and Standard Deviation:                      {:.2f}, {:.2f}'.format(np.mean(temp_distribution), np.std(temp_distribution)))
print('Standard Normal Distribution (Divide by Standard Deviation) - Mean and Standard Deviation: {:.2f}, {:.2f}'.format(np.mean(converted_standard_normal_distribution), np.std(converted_standard_normal_distribution)))

plt.figure()

plt.subplot(311)
cmap = mpl.cm.get_cmap('tab20')
plt.bar(range(1, len(original_distribution) + 1), original_distribution, width=0.9, label='Original Distribution', color=cmap(1))
plt.title('Original Distribution')
plt.xlabel('Serial Number')
plt.ylabel('Number')

plt.subplot(312)
cmap = mpl.cm.get_cmap('tab20b')
plt.bar(range(1, len(temp_distribution) + 1), temp_distribution, width=0.9, label='Temporary Distribution', color=cmap(1))
plt.title('Standard Normal Distribution - Subtract Mean')
plt.xlabel('Serial Number')
plt.ylabel('Number')

plt.subplot(313)
cmap = mpl.cm.get_cmap('tab20c')
plt.bar(range(1, len(converted_standard_normal_distribution) + 1), converted_standard_normal_distribution, width=0.9, label='Standard Normal Distribution', color=cmap(1))
plt.title('Standard Normal Distribution - Divide by Standard Deviation')
plt.xlabel('Serial Number')
plt.ylabel('Number')

plt.show()
