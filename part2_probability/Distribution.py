"""
Distribution.py
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

single_die_x = [x for x in range(1, 7)]
size_x = len(single_die_x)
single_die_y = [(1 / size_x)] * size_x

double_dice_list = [(i + j) for i in range(1, 7) for j in range(1, 7)]
double_dice_x = list(sorted(set(double_dice_list)))
double_dice_y = [round(double_dice_list.count(i) / len(double_dice_list), 2) for i in double_dice_x]

plt.figure()

plt.subplot(211)
plt.plot(single_die_x, single_die_y)
plt.title('Roll of single die')
plt.xlabel('Number on single die')
plt.ylabel('Probability')

plt.subplot(212)
cmap = mpl.cm.get_cmap('tab10')
plt.bar(double_dice_x, double_dice_y, width=0.9, label='Sum', color=cmap(1))
plt.title('Roll of double dice')
plt.xlabel('Sum of double dice')
plt.ylabel('Probability')
plt.xticks(double_dice_x)
plt.yticks(np.arange(0.00, max(double_dice_y) + 0.02, 0.01))

plt.show()
