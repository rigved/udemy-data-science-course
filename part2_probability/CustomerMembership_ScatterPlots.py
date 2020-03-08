"""
CustomerMembership_ScatterPlots.py
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
import seaborn as sns

data = pd.read_excel('Customers_Membership.xlsx', sheet_name='Membership Status', usecols='A:B')

print(data)

plt.figure()

sns.set(color_codes=True)
sns.regplot(x='Customer Age', y='Membership Status', data=data, logistic=True)

plt.show()
