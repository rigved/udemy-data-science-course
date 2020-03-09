"""
NumericalVariablesExercise_FrequencyDistributionTable.py
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

data = pd.DataFrame({'Frequency': pd.cut([8, 30, 30, 50, 86, 94, 102, 110, 169, 170, 176, 236, 240, 241, 242, 255, 262, 276, 279, 282], range(7, 285, 46)).value_counts()})
data['Relative Frequency'] = data['Frequency'] / data['Frequency'].sum()
print(data)

data = pd.DataFrame({'Frequency': pd.cut([8, 30, 30, 50, 86, 94, 102, 110, 169, 170, 176, 236, 240, 241, 242, 255, 262, 276, 279, 282], np.arange(7.99, 285.00, 45.67)).value_counts()})
data['Relative Frequency'] = data['Frequency'] / data['Frequency'].sum()
print(data)
