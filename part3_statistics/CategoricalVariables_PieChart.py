"""
CategoricalVariables_PieChart.py
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

csv_data = pd.read_csv('data/CategoricalVariables_FrequencyTable.csv')
car_company = csv_data['Car Company'].values
frequency = csv_data['Frequency'].values
total = sum(frequency)
relative_frequency = frequency / total

plt.figure()

plt.subplot(111)
plt.pie(relative_frequency, labels=car_company, autopct='%1.2f%%')
plt.title('Market Share in Bonn')

plt.show()
