"""
NumericalVariables_FrequencyDistributionTable.py
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

data = pd.DataFrame({'Frequency': pd.cut([1, 9, 22, 24, 32, 41, 44, 48, 57, 66, 70, 73, 75, 76, 79, 82, 87, 89, 95, 100], [0, 21, 41, 61, 81, 101]).value_counts()})
data['Relative Frequency'] = data['Frequency'] / data['Frequency'].sum()
print(data)
