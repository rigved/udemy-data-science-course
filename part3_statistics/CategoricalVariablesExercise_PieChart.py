"""
CategoricalVariablesExercise_PieChart.py
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

csv_data = pd.read_csv('data/CategoricalVariablesExercise_FrequencyTable.csv')
city = csv_data['City'].values
frequency = csv_data['Frequency'].values
total = sum(frequency)
relative_frequency = frequency / total

plt.figure()

plt.subplot(111)
plt.pie(relative_frequency, labels=city, autopct='%1.2f%%')
plt.title('Sales')

plt.show()
