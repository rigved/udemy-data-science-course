"""
CategoricalVariablesExercise_ParettoChart.py
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
from matplotlib.ticker import PercentFormatter
import matplotlib as mpl

csv_data = pd.read_csv('data/CategoricalVariablesExercise_FrequencyTable.csv')
sales_data = pd.DataFrame()
sales_data = csv_data.sort_values(by='Frequency', ascending=False)
sales_data['Relative Frequency'] = (sales_data['Frequency'] / sales_data['Frequency'].sum()) * 100
sales_data['Cumulative Frequency'] = sales_data['Relative Frequency'].cumsum()

plt.figure()

ax1 = plt.subplot(111)
cmap = mpl.cm.get_cmap('tab10')
ax1.bar(sales_data['City'], sales_data['Frequency'], label='Sales', color=cmap(1))
ax1.set_ylim(bottom=0, top=25000)
plt.title('Sales')
plt.xlabel('City')
plt.ylabel('Frequency')
ax2 = ax1.twinx()
ax2.plot(sales_data['City'], sales_data['Cumulative Frequency'], color=cmap(2), marker='D')
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel('Cumulative Frequency')
ax2.set_ylim(bottom=0.0, top=100.0)
ax2.set_yticks(range(0, 101, 10))

ax1.tick_params(axis='y', colors=cmap(1))
ax2.tick_params(axis='y', colors=cmap(2))

plt.tight_layout()
plt.show()
