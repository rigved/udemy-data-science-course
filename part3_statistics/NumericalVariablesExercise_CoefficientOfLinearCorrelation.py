"""
NumericalVariablesExercise_CoefficientOfLinearCorrelation.py
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

data = pd.DataFrame({'Writing': [344, 383, 611, 713, 536], 'Reading': [378, 349, 503, 719, 503]})

print('Coefficient of Linear Correlation: {:.2f}'.format(data['Writing'].corr(data['Reading'])))

plt.figure()

plt.subplot(211)
plt.scatter(data['Writing'], data['Reading'])
plt.xlabel('Writing')
plt.ylabel('Reading')
plt.xlim(200, 800)
plt.ylim(200, 800)

plt.subplot(212)
plt.scatter(data['Reading'], data['Writing'])
plt.xlabel('Reading')
plt.ylabel('Writing')
plt.xlim(200, 800)
plt.ylim(200, 800)

plt.show()
