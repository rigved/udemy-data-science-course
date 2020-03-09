"""
NumericalVariablesExercise_SideBySideBarChart.py
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

data = pd.DataFrame({'Employed': [60, 85, 95, 97, 97, 100], 'Unemployed': [40, 15, 5, 3, 3, 0]},
                    index=['18-25', '25-35', '35-45', '45-55', '55-65', '65+'])
indices = np.arange(len(data.index))
width = 0.35

print(data)

plt.figure()
plt.subplot(111)
plt.bar(indices, data['Employed'], width=width)
plt.bar(indices + width, data['Unemployed'], width=width)
plt.xticks(indices + 0.15, data.index)
plt.ylim(0.0, max(data.max()) + 10)
plt.title('Numerical Variables Side-by-Side Bar Chart Exercise')
plt.xlabel('Age Group')
plt.ylabel('Percentage')
plt.legend(['Employed', 'Unemployed'])

plt.show()
