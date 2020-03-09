"""
PracticalExample.py
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

gender_raw_data = ['F', 'F', 'M', 'M', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'F', 'M', 'F', 'F', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'M', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
gender_labels = ['Male', 'Female', 'Firm']
gender = [1 if i == 'M' else 2 if i == 'F' else 3 for i in gender_raw_data]
customer_data_gender = pd.DataFrame({'Frequency': pd.cut(gender, [0, 1, 2, 3], labels=gender_labels).value_counts()})
customer_data_gender['RelativeFrequency'] = round((customer_data_gender['Frequency'] / customer_data_gender['Frequency'].sum()) * 100)

print(customer_data_gender)

plt.figure()

plt.subplot(111)
plt.pie(customer_data_gender['RelativeFrequency'], labels=gender_labels)
plt.title('Gender')

plt.show()

location_raw_data = ['California', 'California', 'California', 'California', 'California', 'Virginia', 'Virginia', 'California', 'Arizona', 'Virginia', 'Oregon', 'California', 'Nevada', 'California', 'California', 'California', 'Nevada', 'Colorado', 'Arizona', 'Arizona', 'Nevada', 'California', 'California', 'Colorado', 'California', 'California', 'Utah', 'California', 'California', 'California', 'Nevada', 'California', 'Arizona', 'California', 'California', 'California', 'Colorado', 'California', 'California', 'Arizona', 'California', 'None', 'Kansas', 'California', 'California', 'California', 'California', 'California', 'Colorado', 'Arizona', 'Colorado', 'California', 'California', 'Nevada', 'Colorado', 'California', 'California', 'California', 'None', 'California', 'California', 'Oregon', 'Utah', 'California', 'None', 'California', 'Colorado', 'Oregon', 'California', 'California', 'California', 'California', 'California', 'Oregon', 'California', 'Nevada', 'None', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'Colorado', 'California', 'California', 'California', 'California', 'California', 'California', 'Utah', 'California', 'California', 'California', 'California', 'Oregon', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'None', 'California', 'Nevada', 'California', 'California', 'California', 'Arizona', 'Arizona', 'Nevada', 'Colorado', 'California', 'California', 'Utah', 'Nevada', 'Colorado', 'California', 'Nevada', 'Nevada', 'California', 'California', 'California', 'California', 'California', 'California', 'Utah', 'None', 'Nevada', 'Arizona', 'Wyoming', 'Oregon', 'California', 'California', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'Virginia', 'California', 'California', 'Colorado', 'Arizona', 'California', 'California', 'California', 'California', 'California', 'California', 'Nevada', 'California', 'Oregon', 'Utah', 'California', 'California', 'Oregon', 'Oregon', 'Oregon', 'Oregon', 'None', 'California', 'California', 'Arizona', 'None', 'California', 'Nevada', 'Nevada', 'Nevada', 'Nevada', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California', 'California']
location = pd.Series([i for i in location_raw_data if i != 'None'])
customer_data_location = pd.DataFrame({'Frequency': location.value_counts(),
                                       'Relative Frequency': round(location.value_counts(normalize=True) * 100)})
customer_data_location['Cumulative Frequency'] = customer_data_location['Relative Frequency'].cumsum()

print(customer_data_location)

plt.figure()

ax1 = plt.subplot(111)
cmap = mpl.cm.get_cmap('tab10')
ax1.bar(customer_data_location.index, customer_data_location['Frequency'], label='Segmentation of US clients by State', color=cmap(1))
ax1.set_ylim(bottom=0, top=140)
plt.title('Segmentation of US clients by State')
plt.xlabel('State')
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

age = [19, 22, 22, 22, 25, 26, 26, 26, 27, 27, 28, 26, 29, 29, 29, 29, 29, 30, 30, 30, 31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 35, 35, 35, 36, 36, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 43, 49, 43, 43, 43, 43, 48, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 57, 57, 57, 57, 59, 59, 59, 48, 48, 60, 60, 60, 60, 60, 60, 60, 61, 61, 64, 65, 65, 65, 65, 66, 66, 66, 66, 67, 67, 67, 68, 69, 69, 69, 69, 71, 71, 73, 73, 73, 76]
age_series = pd.Series(age)
x_labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
bin_edges = [18, 25, 35, 45, 55, 65, age_series.max() + 1]
customer_data_age = pd.DataFrame({'Frequency': pd.cut(age, bin_edges).value_counts()})
customer_data_age['Relative Frequency'] = round((customer_data_age['Frequency'] / customer_data_age['Frequency'].sum()) * 100)
age_frequency = age_series.value_counts(sort=False)

print(customer_data_age)
print('Mean: {:.2f}'.format(age_series.mean()))
print('Median: {:.2f}'.format(age_series.median()))
print('Mode: {:.2f}'.format(age_series.mode().tolist()[0]))
print('Skewness: {:.2f}'.format(skew(age_series)))
print('Variance: {:.2f}'.format(tvar(age_series)))
print('Standard Deviation: {:.2f}'.format(tstd(age_series)))

plt.figure()

plt.subplot(211)
age_frequency.plot.bar(rot=0, title='Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(212)
plt.bar(x_labels, customer_data_age['Relative Frequency'].values, width=0.9)
plt.ylim(0.0, max(customer_data_age['Relative Frequency'].values) + 0.1)
plt.title('Age')
plt.xlabel('Age')
plt.ylabel('Relative Frequency')

plt.show()

customer_data_price = pd.DataFrame({'Price': [246172.68, 246331.90, 209280.91, 452667.01, 467083.31, 203491.85, 212520.83, 198591.85, 265467.68, 235633.26, 317473.86, 503790.23, 217786.38, 460001.26, 460001.26, 448134.27, 249591.99, 196142.19, 258572.48, 310831.21, 207281.59, 168834.04, 396973.83, 188743.11, 179674.08, 306363.64, 200300.63, 382041.13, 245572.79, 407214.29, 355073.40, 256821.64, 226342.80, 191389.87, 297008.97, 250773.15, 312211.14, 190119.50, 225050.52, 261742.74, 344530.89, 215410.28, 252185.99, 480545.81, 300385.62, 240539.35, 222138.72, 228410.05, 197053.51, 193660.62, 237060.15, 372001.70, 290031.26, 238811.06, 199054.20, 496266.41, 346906.89, 376964.62, 315733.15, 188273.73, 253831.02, 278575.87, 402081.80, 310832.59, 257183.48, 326885.34, 344568.74, 214631.68, 237207.68, 464549.19, 310577.04, 205098.21, 248525.12, 224463.87, 220606.28, 220865.00, 338181.18, 432679.91, 196220.05, 323915.81, 200719.02, 380809.52, 213942.56, 207581.43, 241671.52, 336695.25, 171262.65, 299159.14, 212265.67, 388515.14, 263790.81, 367976.46, 243052.59, 269075.30, 223577.32, 198075.99, 354553.23, 456919.46, 233142.80, 225401.62, 195153.16, 206631.81, 358525.59, 223917.34, 201518.89, 269278.57, 204808.16, 306878.46, 275394.25, 192092.24, 165430.28, 310223.29, 231552.33, 215774.28, 289727.99, 195874.94, 357538.20, 239248.75, 382277.15, 248422.66, 242740.66, 253025.78, 234172.39, 200678.75, 226578.51, 200148.89, 218585.92, 198841.70, 252927.84, 225290.22, 234750.59, 287466.41, 229464.71, 377313.56, 276759.18, 219373.41, 230216.22, 410932.67, 214341.34, 248274.31, 390494.27, 293876.27, 204286.67, 230154.53, 228170.03, 205085.40, 177555.06, 217748.48, 247739.44, 484458.03, 356506.37, 197869.36, 236608.95, 208930.81, 263123.42, 286433.57, 229581.78, 252053.03, 244820.67, 241620.48, 235762.34, 236639.56, 294807.65, 293828.69, 412856.56, 224076.84, 258015.61, 153466.71, 261871.70, 210038.70, 210824.06, 249075.66, 219865.76, 204292.49, 261579.89, 222867.42, 291494.36, 296483.14],
                                    'Size': [743.09, 756.21, 587.28, 1604.75, 1375.45, 675.19, 670.89, 720.81, 782.25, 794.52, 1160.36, 1942.50, 794.52, 1109.25, 1400.95, 1479.72, 790.54, 723.93, 781.07, 1127.76, 720.70, 649.69, 1307.45, 618.38, 625.80, 1203.29, 670.89, 1434.09, 781.07, 1596.35, 1110.32, 781.07, 697.89, 625.80, 957.53, 722.96, 923.21, 670.24, 785.48, 798.28, 1121.95, 782.25, 923.21, 1434.09, 1160.36, 798.28, 733.19, 798.28, 733.19, 717.05, 747.50, 1121.95, 1121.95, 827.87, 747.50, 1608.84, 1132.06, 1383.84, 927.83, 669.16, 928.16, 798.50, 1305.62, 1121.95, 785.48, 927.08, 1109.25, 649.80, 785.48, 1596.35, 1121.95, 743.41, 756.21, 649.80, 785.48, 785.48, 1283.45, 1434.09, 782.25, 1288.62, 781.07, 1222.34, 781.07, 743.09, 785.48, 1109.25, 579.75, 1128.40, 701.66, 1336.93, 794.52, 1171.55, 794.52, 798.28, 798.28, 649.80, 1137.44, 1604.75, 675.19, 649.69, 785.48, 781.07, 1127.76, 794.52, 794.52, 781.07, 720.81, 927.83, 927.83, 785.48, 618.16, 1109.25, 720.70, 720.81, 927.08, 798.28, 1057.92, 781.07, 1396.86, 794.52, 923.21, 781.07, 782.25, 733.19, 733.19, 794.52, 756.21, 736.63, 785.48, 781.07, 798.28, 798.28, 827.87, 1160.36, 827.87, 723.83, 798.28, 1238.58, 723.83, 977.87, 1093.00, 927.83, 701.66, 680.57, 723.93, 649.80, 649.80, 85.48, 785.48, 1615.29, 1132.06, 720.38, 733.19, 782.25, 798.28, 1057.92, 723.83, 798.28, 794.52, 794.52, 782.25, 785.48, 923.21, 923.21, 1434.09, 782.25, 781.07, 618.38, 923.21, 781.07, 781.07, 781.07, 697.89, 670.89, 782.25, 743.41, 923.21, 923.21],
                                    'Age': age
                                    })

print('\n\nCovariance - Price and Age: {:.2f}'.format(np.cov(customer_data_price['Price'], customer_data_price['Age'])[0, 1]))
print('Linear Correlation Coefficient - Price and Age: {:.2f}'.format(customer_data_price['Price'].corr(customer_data_price['Age'])))
print('\n\nCovariance - Price and Size: {:.2f}'.format(np.cov(customer_data_price['Price'], customer_data_price['Size'])[0, 1]))
print('Linear Correlation Coefficient - Price and Size: {:.2f}'.format(customer_data_price['Price'].corr(customer_data_price['Size'])))

plt.figure()

plt.subplot(211)
plt.scatter(customer_data_price['Price'], customer_data_price['Age'])
plt.xlabel('Price')
plt.ylabel('Age')
plt.xlim(0, customer_data_price['Price'].max() + 10000)
plt.ylim(0, customer_data_price['Age'].max() + 10)

plt.subplot(212)
plt.scatter(customer_data_price['Price'], customer_data_price['Size'])
plt.xlabel('Price')
plt.ylabel('Size')
plt.xlim(0, customer_data_price['Price'].max() + 10000)
plt.ylim(0, customer_data_price['Size'].max() + 100)

plt.show()
