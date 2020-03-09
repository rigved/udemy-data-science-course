"""
NumericalVariables_ScatterPlot.py
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

import pandas as pd
from matplotlib import pyplot as plt

data = pd.DataFrame({'Reading': [273, 292, 219, 241, 284, 247, 237, 286, 237, 266, 311, 324, 330, 331, 336, 344, 346, 346, 356, 364, 365, 365, 369, 436, 393, 394, 417, 438, 398, 409, 437, 442, 442, 408, 387, 418, 461, 457, 371, 383, 372, 463, 452, 550, 529, 578, 454, 522, 554, 591, 601, 610, 611, 613, 614, 619, 634, 646, 668, 673, 696, 704, 705, 705, 708, 713, 713, 727, 735, 763, 776, 777, 785, 785, 547, 507, 474, 536, 455, 470, 536, 522, 462, 467, 477, 505, 515, 450, 542, 509, 455, 524, 451, 505, 465, 525, 508, 511, 469, 457, 499, 528, 539, 549],
                     'Writing': [216, 282, 250, 217, 266, 294, 215, 203, 286, 263, 270, 211, 243, 275, 367, 378, 315, 208, 451, 346, 435, 579, 390, 589, 365, 480, 499, 414, 530, 366, 453, 396, 531, 453, 444, 597, 407, 589, 489, 349, 584, 446, 451, 300, 480, 580, 457, 525, 483, 470, 585, 406, 503, 16, 639, 546, 556, 599, 534, 526, 613, 536, 578, 608, 717, 718, 719, 720, 724, 734, 735, 736, 738, 740, 476, 452, 451, 503, 499, 509, 540, 496, 507, 457, 549, 519, 491, 487, 455, 546, 514, 533, 536, 503, 507, 489, 488, 520, 527, 521, 462, 536, 549, 521]},
                    index=pd.RangeIndex(1, 105))
data.index.name = 'Student ID'

plt.figure()
plt.subplot(111)
plt.scatter(data['Reading'], data['Writing'])
plt.xlabel('Reading')
plt.ylabel('Writing')
plt.xlim(200, 800)
plt.ylim(200, 800)
plt.show()
