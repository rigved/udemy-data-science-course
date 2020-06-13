"""
SimpleLinearRegressionExercise.py
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
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

sns.set()

data = pd.read_csv('data/real_estate_price_size.csv')

print(data)

y = data['price']
x1 = data['size']

plt.scatter(x1, y)
plt.xlabel('Size', fontsize=20)
plt.ylabel('Price', fontsize=20)
plt.show()

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()

print(results.summary())

plt.scatter(x1, y)
yhat = 223.1787 * x1 + 1.019e+05
fig = plt.plot(x1, yhat, lw=4, c='orange', label='Regression Line')
plt.xlabel('Size', fontsize=20)
plt.ylabel('Prize', fontsize=20)
plt.show()
