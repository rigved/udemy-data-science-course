"""
NumericalVariables_SideBySideBarChart.py
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

data = pd.DataFrame({'Investor A': [96, 181, 88], 'Investor B': [185, 3, 152], 'Investor C': [39, 29, 142]},
                    index=['Stocks', 'Bonds', 'Real Estate'])
indices = np.arange(len(data.columns))
width = 0.25

print(data)

plt.figure()
plt.subplot(111)
for i in range(len(data.columns)):
    plt.bar(indices + (i * width), data.iloc[i], width=width)
locations = [indices + (i * width) for i in range(len(data.columns))]
plt.xticks(indices + width, data.columns)
plt.ylim(0.0, max(data.max()) + 10)
plt.title('Numerical Variables Side-by-Side Bar Chart')
plt.xlabel('Type of Investment')
plt.ylabel('Investment')

plt.show()
