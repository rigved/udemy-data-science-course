"""
NumericalVariables_Covariance.py
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
import numpy as np
from matplotlib import pyplot as plt

data = pd.DataFrame({'Size': [650, 785, 1200, 720, 975], 'Price': [772000, 998000, 1200000, 800000, 895000]})
cv = np.cov(data['Size'], data['Price'])[0, 1]

print('Covariance: {:.2f}'.format(cv))

plt.figure()
plt.subplot(111)
plt.scatter(data['Size'], data['Price'])
plt.xlabel('Size')
plt.ylabel('Price')
plt.xlim(600, 1300)
plt.ylim(0, 1400000)
plt.show()
