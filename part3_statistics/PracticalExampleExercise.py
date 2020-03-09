"""
PracticalExampleExercise.py
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
import matplotlib as mpl
from scipy.stats import skew, tstd, tvar
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter

customer_data_price_list = [246172.68, 246331.90, 209280.91, 452667.01, 467083.31, 203491.85, 212520.83, 198591.85, 265467.68, 235633.26, 317473.86, 503790.23, 217786.38, 460001.26, 460001.26, 448134.27, 249591.99, 196142.19, 258572.48, 310831.21, 207281.59, 168834.04, 396973.83, 188743.11, 179674.08, 306363.64, 200300.63, 382041.13, 245572.79, 407214.29, 355073.40, 256821.64, 226342.80, 191389.87, 297008.97, 250773.15, 312211.14, 190119.50, 225050.52, 261742.74, 344530.89, 215410.28, 252185.99, 480545.81, 300385.62, 240539.35, 222138.72, 228410.05, 197053.51, 193660.62, 237060.15, 372001.70, 290031.26, 238811.06, 199054.20, 496266.41, 346906.89, 376964.62, 315733.15, 188273.73, 253831.02, 278575.87, 402081.80, 310832.59, 257183.48, 326885.34, 344568.74, 214631.68, 237207.68, 464549.19, 310577.04, 205098.21, 248525.12, 224463.87, 220606.28, 220865.00, 338181.18, 432679.91, 196220.05, 323915.81, 200719.02, 380809.52, 213942.56, 207581.43, 241671.52, 336695.25, 171262.65, 299159.14, 212265.67, 388515.14, 263790.81, 367976.46, 243052.59, 269075.30, 223577.32, 198075.99, 354553.23, 456919.46, 233142.80, 225401.62, 195153.16, 206631.81, 358525.59, 223917.34, 201518.89, 269278.57, 204808.16, 306878.46, 275394.25, 192092.24, 165430.28, 310223.29, 231552.33, 215774.28, 289727.99, 195874.94, 357538.20, 239248.75, 382277.15, 248422.66, 242740.66, 253025.78, 234172.39, 200678.75, 226578.51, 200148.89, 218585.92, 198841.70, 252927.84, 225290.22, 234750.59, 287466.41, 229464.71, 377313.56, 276759.18, 219373.41, 230216.22, 410932.67, 214341.34, 248274.31, 390494.27, 293876.27, 204286.67, 230154.53, 228170.03, 205085.40, 177555.06, 217748.48, 247739.44, 484458.03, 356506.37, 197869.36, 236608.95, 208930.81, 263123.42, 286433.57, 229581.78, 252053.03, 244820.67, 241620.48, 235762.34, 236639.56, 294807.65, 293828.69, 412856.56, 224076.84, 258015.61, 153466.71, 261871.70, 210038.70, 210824.06, 249075.66, 219865.76, 204292.49, 261579.89, 222867.42, 291494.36, 296483.14, 532877.38, 117564.07, 317196.40, 264142.16, 222947.21, 250312.53, 246050.40, 529317.28, 169158.29, 206958.71, 206445.42, 239341.58, 398903.42, 210745.17, 331154.88, 204434.68, 189194.31, 204027.09, 400865.92, 217787.71, 219630.90, 244624.87, 163162.88, 401302.82, 538271.74, 461464.99, 275812.49, 216552.71, 495570.44, 388656.81, 495024.09, 526947.16, 427236.10, 327044.37, 385447.69, 401894.82, 264275.78, 231348.93, 264238.95, 217357.63, 482404.31, 228937.90, 498994.03, 256376.28, 255243.11, 506786.66, 233172.49, 233834.00, 523373.45, 228872.91, 208655.67, 322952.56, 216826.00, 298730.40, 230495.01, 346048.04, 377043.60, 413761.71, 212644.39, 250415.38, 219252.89, 264011.70, 211406.87, 396330.29, 227072.88, 276323.87, 230943.38, 315382.11, 372016.56, 237680.88, 234032.88, 273165.58, 271227.49, 349865.22, 199730.73, 338482.45, 351304.58, 338472.13, 212916.36, 308660.80, 147343.69, 448574.67, 255337.90, 175773.59, 322610.74, 279191.26, 287996.53, 365868.78, 199216.40]
customer_data_price_series = pd.Series(customer_data_price_list)
customer_data_price_frequency = customer_data_price_series.value_counts(sort=False, bins=272)
customer_data_price = pd.DataFrame({'Frequency': pd.cut(customer_data_price_list, [i for i in np.arange(min(customer_data_price_list), max(customer_data_price_series) + 100000, 100000)]).value_counts()})
customer_data_price['Relative Frequency'] = customer_data_price['Frequency'] / customer_data_price['Frequency'].sum()
x_labels = [str(i) for i in customer_data_price.index]

print(customer_data_price)

plt.figure()

plt.subplot(211)
customer_data_price_frequency.plot.bar(rot=0, title='Price')
plt.xticks([])
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.subplot(212)
plt.bar(x_labels, customer_data_price['Frequency'].values, width=1.0)
plt.ylim(0.0, 140)
plt.title('Price Histogram')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.show()

customer_data_area_list = [743.09, 756.21, 587.28, 1604.75, 1375.45, 675.19, 670.89, 720.81, 782.25, 794.52, 1160.36, 1942.50, 794.52, 1109.25, 1400.95, 1479.72, 790.54, 723.93, 781.07, 1127.76, 720.70, 649.69, 1307.45, 618.38, 625.80, 1203.29, 670.89, 1434.09, 781.07, 1596.35, 1110.32, 781.07, 697.89, 625.80, 957.53, 722.96, 923.21, 670.24, 785.48, 798.28, 1121.95, 782.25, 923.21, 1434.09, 1160.36, 798.28, 733.19, 798.28, 733.19, 717.05, 747.50, 1121.95, 1121.95, 827.87, 747.50, 1608.84, 1132.06, 1383.84, 927.83, 669.16, 928.16, 798.50, 1305.62, 1121.95, 785.48, 927.08, 1109.25, 649.80, 785.48, 1596.35, 1121.95, 743.41, 756.21, 649.80, 785.48, 785.48, 1283.45, 1434.09, 782.25, 1288.62, 781.07, 1222.34, 781.07, 743.09, 785.48, 1109.25, 579.75, 1128.40, 701.66, 1336.93, 794.52, 1171.55, 794.52, 798.28, 798.28, 649.80, 1137.44, 1604.75, 675.19, 649.69, 785.48, 781.07, 1127.76, 794.52, 794.52, 781.07, 720.81, 927.83, 927.83, 785.48, 618.16, 1109.25, 720.70, 720.81, 927.08, 798.28, 1057.92, 781.07, 1396.86, 794.52, 923.21, 781.07, 782.25, 733.19, 733.19, 794.52, 756.21, 736.63, 785.48, 781.07, 798.28, 798.28, 827.87, 1160.36, 827.87, 723.83, 798.28, 1238.58, 723.83, 977.87, 1093.00, 927.83, 701.66, 680.57, 723.93, 649.80, 649.80, 785.48, 785.48, 1615.29, 1132.06, 720.38, 733.19, 782.25, 798.28, 1057.92, 723.83, 798.28, 794.52, 794.52, 782.25, 785.48, 923.21, 923.21, 1434.09, 782.25, 781.07, 618.38, 923.21, 781.07, 781.07, 781.07, 697.89, 670.89, 782.25, 743.41, 923.21, 923.21, 1769.48, 410.71, 1200.82, 800.96, 827.87, 775.69, 775.69, 1604.75, 587.28, 756.21, 743.09, 827.87, 1160.36, 743.09, 1160.36, 625.80, 756.21, 625.80, 1238.58, 713.71, 763.21, 798.50, 618.38, 1479.72, 1603.99, 1615.29, 784.19, 720.38, 1596.35, 1121.95, 1596.35, 1596.35, 1273.88, 966.57, 1357.16, 1343.39, 758.69, 789.25, 789.25, 733.19, 1611.85, 789.25, 1611.85, 789.25, 794.52, 1611.85, 789.25, 794.52, 1611.85, 789.25, 794.52, 1111.72, 785.48, 1058.25, 791.72, 1068.58, 1325.31, 1273.88, 798.50, 798.50, 798.50, 1058.25, 618.16, 1273.88, 798.50, 798.50, 798.50, 1058.25, 1273.55, 798.50, 798.50, 798.28, 1057.92, 1273.55, 618.16, 1273.55, 1057.92, 1273.55, 798.28, 1057.92, 606.33, 1273.55, 798.28, 598.58, 1238.58, 794.52, 1013.27, 1074.71, 789.25]

plt.figure()

plt.subplot(111)
plt.scatter(customer_data_area_list, customer_data_price_list)
plt.title('Area - Price Scatter Plot')
plt.xlabel('Area')
plt.ylabel('Price')
plt.xlim(min(customer_data_area_list) - 200.0, max(customer_data_area_list) + 200.0)
plt.ylim(min(customer_data_price_list) - 10000, max(customer_data_price_list) + 10000)

plt.show()

customer_data_location_series = pd.Series(['USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'UK', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Belgium', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Russia', 'USA', 'USA', 'USA', 'USA', 'USA', 'Denmark', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Germany', 'USA', 'USA', 'USA', 'USA', 'Mexico', 'USA', 'USA', 'USA', 'USA', 'USA', 'UK', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Russia', 'USA', 'USA', 'USA', 'USA', 'USA', 'Belgium', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Russia', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Canada', 'Canada', 'Canada', 'Canada', 'Canada', 'Canada', 'Canada', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'Russia', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA'])

customer_data_location = pd.DataFrame({'Frequency': customer_data_location_series.value_counts()})
customer_data_location['Relative Frequency'] = (customer_data_location_series.value_counts(normalize=True) * 100).round(2)
customer_data_location['Cumulative Frequency'] = customer_data_location['Relative Frequency'].cumsum()
customer_data_location.index.name = 'Country'

print(customer_data_location)

plt.figure()

ax1 = plt.subplot(111)
cmap = mpl.cm.get_cmap('tab10')
ax1.bar(customer_data_location.index, customer_data_location['Frequency'], label='Segmentation by Country', color=cmap(1))
ax1.set_ylim(bottom=0, top=200)
plt.title('Segmentation by Country')
plt.xlabel('Country')
plt.ylabel('Frequency')
ax2 = ax1.twinx()
ax2.plot(customer_data_location.index, customer_data_location['Cumulative Frequency'], color=cmap(2), marker='D')
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel('Cumulative Frequency')
ax2.set_ylim(bottom=0.0, top=100.0)
ax2.set_yticks(range(0, 101, 10))

ax1.tick_params(axis='y', colors=cmap(1))
ax2.tick_params(axis='y', colors=cmap(2))

plt.tight_layout()

plt.show()

print('Mean: {:.2f}'.format(customer_data_price_series.mean()))
print('Median: {:.2f}'.format(customer_data_price_series.median()))
print('Mode: {:.2f}'.format(customer_data_price_series.mode().tolist()[0]))
print('Skewness: {:.2f}'.format(skew(customer_data_price_series)))
print('Variance: {:.2f}'.format(tvar(customer_data_price_series)))
print('Standard Deviation: {:.2f}'.format(tstd(customer_data_price_series)))
print('Covariance: {:.2f}'.format(np.cov(customer_data_price_list, customer_data_area_list)[0, 1]))
customer_data_area = pd.DataFrame({'Price': customer_data_price_list, 'Area': customer_data_area_list})
print('Linear Correlation Coefficient: {:.2f}'.format(customer_data_area['Price'].corr(customer_data_area['Area'])))
