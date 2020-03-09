"""
MeasuresOfCentralTendencyExercise.py
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

raw_data = [62000.00, 64000.00, 49000.00, 324000.00, 1264000.00, 54330.00, 64000.00, 51000.00, 55000.00, 48000.00, 53000.00]
data = pd.DataFrame({'Annual Income': raw_data},
                    index=pd.RangeIndex(1, len(raw_data) + 1))

print(data)
print(np.mean(data))
print(np.median(data))
print(statistics.mode(data['Annual Income']))
