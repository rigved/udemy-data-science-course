"""
DailyViews_ScatterPlots.py
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
from matplotlib import pyplot as plt
import matplotlib as mpl

data = pd.read_excel('Daily_Views.xlsx', sheet_name='Views', usecols='A:B')
days_after_release = data['Days after release'].values
daily_views = data['Daily Views'].values
cdf = np.cumsum(daily_views)

plt.figure()

plt.subplot(211)
cmap = mpl.cm.get_cmap('tab10')
plt.scatter(days_after_release, daily_views, label='Daily Views', color=cmap(1))
z = np.polyfit(days_after_release, daily_views, 2)
p = np.polyval(z, days_after_release)
axes = plt.gca()
axes.set_xlim([min(days_after_release), max(days_after_release)])
axes.set_ylim([min(p), max(p)])
plt.title('Daily Views')
plt.xlabel('Days after Release')
plt.ylabel('Daily Views')
plt.plot(days_after_release, p, color=cmap(2))

plt.subplot(212)
cmap = mpl.cm.get_cmap('tab20')
plt.scatter(days_after_release, cdf, label='Daily Views', color=cmap(1))
z = np.polyfit(days_after_release, cdf, 2)
p = np.polyval(z, days_after_release)
axes = plt.gca()
axes.set_xlim([min(days_after_release), max(days_after_release)])
axes.set_ylim([min(p), max(p)])
plt.title('Daily Views')
plt.xlabel('Days after Release')
plt.ylabel('Daily Views: CDF')
plt.plot(days_after_release, p, color=cmap(2))

plt.show()
