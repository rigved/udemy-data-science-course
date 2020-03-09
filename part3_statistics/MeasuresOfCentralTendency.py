"""
MeasuresOfCentralTendency.py
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
import statistics

data = pd.DataFrame({'New York': [1.00, 2.00, 3.00, 3.00, 5.00, 6.00, 7.00, 8.00, 9.00, 11.00, 66.00],
                     'Los Angeles': [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, np.NaN]},
                    index=pd.RangeIndex(1, 12))
data.index.name = 'Position'

try:
    print(data)
    print(np.mean(data))
    print(np.nanmedian(data['New York']))
    print(np.nanmedian(data['Los Angeles']))
    print(statistics.mode(data['New York']))
    print(statistics.mode(data['Los Angeles']))
except Exception as e:
    print(e)
