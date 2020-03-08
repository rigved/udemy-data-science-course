"""
CategoricalVariables_BarChart.py
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
import matplotlib as mpl

csv_data = pd.read_csv('data/CategoricalVariables_FrequencyTable.csv')
car_company = csv_data['Car Company'].values
frequency = csv_data['Frequency'].values

plt.figure()

plt.subplot(111)
cmap = mpl.cm.get_cmap('tab10')
plt.bar(car_company, frequency, width=0.1, label='Sales in Bonn', color=cmap(1))
plt.title('Sales')
plt.xlabel('Car Company')
plt.ylabel('Frequency')

plt.show()
