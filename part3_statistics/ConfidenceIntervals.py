"""
ConfidenceIntervals.py
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
from scipy.stats import t

pd.set_option('display.max_column', 25)
pd.set_option('display.width', 512)

df = pd.read_excel('data/ConfidenceIntervals.xlsx', sheet_name='Al Bundy', skiprows=[0, 1, 2], parse_dates=[1], index_col=0, dayfirst=True, usecols='A:O')

countries = sorted(set(df['Country']))

data_male = pd.DataFrame(columns=countries)
data_female = pd.DataFrame(columns=countries)
for country in countries:
    data_male[country] = df.loc[(df['Gender'] == 'Male') & (df['Country'] == country)]['Size (US)'].value_counts(sort=False)
    data_female[country] = df.loc[(df['Gender'] == 'Female') & (df['Country'] == country)]['Size (US)'].value_counts(sort=False)

data_male['Total'] = df.loc[df['Gender'] == 'Male']['Size (US)'].value_counts(sort=False)
data_female['Total'] = df.loc[df['Gender'] == 'Female']['Size (US)'].value_counts(sort=False)

data_male.index.name = 'Male Size (US)'
data_male.sort_index(inplace=True)
data_male.loc['Total'] = data_male.sum()

data_female.index.name = 'Female Size (US)'
data_female.sort_index(inplace=True)
data_female.loc['Total'] = data_female.sum()

print(data_male)
print(data_female)

months = sorted(set(df.loc[df['Year'] == 2016]['Month']))
confidence_level = 0.95

data_male_united_states_monthly = pd.DataFrame()
data_female_united_states_monthly = pd.DataFrame()

for month in months:
    data_male_united_states_monthly = pd.concat([data_male_united_states_monthly, df.loc[(df['Year'] == 2016) & (df['Month'] == month) & (df['Gender'] == 'Male') & (df['Country'] == 'United States')]['Size (US)'].value_counts(sort=False, dropna=False)], axis=1, ignore_index=True)
    data_female_united_states_monthly = pd.concat([data_female_united_states_monthly, df.loc[(df['Year'] == 2016) & (df['Month'] == month) & (df['Gender'] == 'Female') & (df['Country'] == 'United States')]['Size (US)'].value_counts(sort=False, dropna=False)], axis=1, ignore_index=True)

data_male_united_states_monthly.columns = months
data_female_united_states_monthly.columns = months

data_male_united_states_monthly.fillna(value=0, inplace=True)
data_female_united_states_monthly.fillna(value=0, inplace=True)

data_male_united_states_monthly.index.name = 'Male Size (US)'
data_male_united_states_monthly.sort_index(inplace=True)

data_female_united_states_monthly.index.name = 'Female Size (US)'
data_female_united_states_monthly.sort_index(inplace=True)

data_male_united_states_monthly['Mean'] = data_male_united_states_monthly.mean(axis=1).round(decimals=2)
data_female_united_states_monthly['Mean'] = data_female_united_states_monthly.mean(axis=1).round(decimals=2)
data_male_united_states_monthly['Standard Error'] = [round(np.std(data_male_united_states_monthly.loc[i, months], ddof=1) / np.sqrt(data_male_united_states_monthly.shape[1] - 1), 2) for i in data_male_united_states_monthly.index]
data_female_united_states_monthly['Standard Error'] = [round(np.std(data_female_united_states_monthly.loc[i, months], ddof=1) / np.sqrt(data_female_united_states_monthly.shape[1] - 1), 2) for i in data_female_united_states_monthly.index]

t_score_male_united_states_monthly = t.ppf(np.around(1 - ((1 - confidence_level) / 2), 3), df=(data_male_united_states_monthly.shape[1] - 3))
t_score_female_united_states_monthly = t.ppf(np.around(1 - ((1 - confidence_level) / 2), 3), df=(data_female_united_states_monthly.shape[1] - 3))

print('t-score for monthly Male sales in the United States with 95% confidence and {} degrees of freedom: {:.2f}'.format(data_male_united_states_monthly.shape[1] - 3, t_score_male_united_states_monthly))
print('t-score for monthly Female sales in the United States with 95% confidence and {} degrees of freedom: {:.2f}'.format(data_female_united_states_monthly.shape[1] - 3, t_score_female_united_states_monthly))

data_male_united_states_monthly['Margin of Error'] = (data_male_united_states_monthly['Standard Error'] * t_score_male_united_states_monthly).round(decimals=2)
data_female_united_states_monthly['Margin of Error'] = (data_female_united_states_monthly['Standard Error'] * t_score_female_united_states_monthly).round(decimals=2)

data_male_united_states_monthly.loc['Total'] = data_male_united_states_monthly.sum()
data_female_united_states_monthly.loc['Total'] = data_female_united_states_monthly.sum()

data_male_united_states_monthly['{}% Confidence Interval Lower Bound'.format(confidence_level * 100)] = (data_male_united_states_monthly['Mean'] - data_male_united_states_monthly['Margin of Error']).round(decimals=2)
data_male_united_states_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)] = (data_male_united_states_monthly['Mean'] + data_male_united_states_monthly['Margin of Error']).round(decimals=2)
data_female_united_states_monthly['{}% Confidence Interval Lower Bound'.format(confidence_level * 100)] = (data_female_united_states_monthly['Mean'] - data_female_united_states_monthly['Margin of Error']).round(decimals=2)
data_female_united_states_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)] = (data_female_united_states_monthly['Mean'] + data_female_united_states_monthly['Margin of Error']).round(decimals=2)

data_male_united_states_monthly['Number of Pairs'] = data_male_united_states_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)].round(decimals=0)
data_female_united_states_monthly['Number of Pairs'] = data_female_united_states_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)].round(decimals=0)

print(data_male_united_states_monthly)
print(data_female_united_states_monthly)

data_male_germany1_monthly = pd.DataFrame()
data_female_germany1_monthly = pd.DataFrame()
data_male_germany2_monthly = pd.DataFrame()
data_female_germany2_monthly = pd.DataFrame()

for month in months:
    data_male_germany1_monthly = pd.concat([data_male_germany1_monthly, df.loc[(df['Year'] == 2016) & (df['Month'] == month) & (df['Gender'] == 'Male') & (df['Country'] == 'Germany') & (df['Shop'] == 'GER1')]['Size (US)'].value_counts(sort=False, dropna=False)], axis=1, ignore_index=True)
    data_male_germany2_monthly = pd.concat([data_male_germany2_monthly, df.loc[(df['Year'] == 2016) & (df['Month'] == month) & (df['Gender'] == 'Male') & (df['Country'] == 'Germany') & (df['Shop'] == 'GER2')]['Size (US)'].value_counts(sort=False, dropna=False)], axis=1, ignore_index=True)
    data_female_germany1_monthly = pd.concat([data_female_germany1_monthly, df.loc[(df['Year'] == 2016) & (df['Month'] == month) & (df['Gender'] == 'Female') & (df['Country'] == 'Germany') & (df['Shop'] == 'GER1')]['Size (US)'].value_counts(sort=False, dropna=False)], axis=1, ignore_index=True)
    data_female_germany2_monthly = pd.concat([data_female_germany2_monthly, df.loc[(df['Year'] == 2016) & (df['Month'] == month) & (df['Gender'] == 'Female') & (df['Country'] == 'Germany') & (df['Shop'] == 'GER2')]['Size (US)'].value_counts(sort=False, dropna=False)], axis=1, ignore_index=True)

data_male_germany1_monthly.columns = months
data_male_germany2_monthly.columns = months
data_female_germany1_monthly.columns = months
data_female_germany2_monthly.columns = months

data_male_germany1_monthly.fillna(value=0, inplace=True)
data_male_germany2_monthly.fillna(value=0, inplace=True)
data_female_germany1_monthly.fillna(value=0, inplace=True)
data_female_germany2_monthly.fillna(value=0, inplace=True)

data_male_germany1_monthly.index.name = 'Male Size (US)'
data_male_germany1_monthly.sort_index(inplace=True)
data_male_germany2_monthly.index.name = 'Male Size (US)'
data_male_germany2_monthly.sort_index(inplace=True)

data_female_germany1_monthly.index.name = 'Female Size (US)'
data_female_germany1_monthly.sort_index(inplace=True)
data_female_germany2_monthly.index.name = 'Female Size (US)'
data_female_germany2_monthly.sort_index(inplace=True)

data_male_germany1_monthly['Mean'] = data_male_germany1_monthly.mean(axis=1).round(decimals=2)
data_male_germany2_monthly['Mean'] = data_male_germany2_monthly.mean(axis=1).round(decimals=2)
data_female_germany1_monthly['Mean'] = data_female_germany1_monthly.mean(axis=1).round(decimals=2)
data_female_germany2_monthly['Mean'] = data_female_germany2_monthly.mean(axis=1).round(decimals=2)

data_male_germany1_monthly['Standard Deviation'] = [round(np.std(data_male_germany1_monthly.loc[i, months], ddof=1), 2) for i in data_male_germany1_monthly.index]
data_male_germany2_monthly['Standard Deviation'] = [round(np.std(data_male_germany2_monthly.loc[i, months], ddof=1), 2) for i in data_male_germany2_monthly.index]
data_female_germany1_monthly['Standard Deviation'] = [round(np.std(data_female_germany1_monthly.loc[i, months], ddof=1), 2) for i in data_female_germany1_monthly.index]
data_female_germany2_monthly['Standard Deviation'] = [round(np.std(data_female_germany2_monthly.loc[i, months], ddof=1), 2) for i in data_female_germany2_monthly.index]

data_male_germany_monthly = pd.DataFrame({'Pooled Variance': (((data_male_germany1_monthly.shape[1] - 3) * np.square(data_male_germany1_monthly['Standard Deviation'])) + ((data_male_germany2_monthly.shape[1] - 3) * np.square(data_male_germany2_monthly['Standard Deviation']))) / (data_male_germany1_monthly.shape[1] + data_male_germany2_monthly.shape[1] - 6)})
data_female_germany_monthly = pd.DataFrame({'Pooled Variance': (((data_female_germany1_monthly.shape[1] - 3) * np.square(data_female_germany1_monthly['Standard Deviation'])) + ((data_female_germany2_monthly.shape[1] - 3) * np.square(data_female_germany2_monthly['Standard Deviation']))) / (data_female_germany1_monthly.shape[1] + data_female_germany2_monthly.shape[1] - 6)})

t_score_male_germany_monthly = t.ppf(np.around(1 - ((1 - confidence_level) / 2), 3), df=(data_male_germany1_monthly.shape[1] + data_male_germany2_monthly.shape[1] - 6))
t_score_female_germany_monthly = t.ppf(np.around(1 - ((1 - confidence_level) / 2), 3), df=(data_female_germany1_monthly.shape[1] + data_female_germany2_monthly.shape[1] - 8))

print('t-score for monthly Male sales in Germany with 95% confidence and {} degrees of freedom: {:.2f}'.format(data_male_germany1_monthly.shape[1] + data_male_germany2_monthly.shape[1] - 6, t_score_male_germany_monthly))
print('t-score for monthly Female sales in Germany with 95% confidence and {} degrees of freedom: {:.2f}'.format(data_female_germany1_monthly.shape[1] + data_female_germany2_monthly.shape[1] - 6, t_score_female_germany_monthly))

data_male_germany_monthly['Margin of Error'] = (t_score_male_germany_monthly * np.sqrt((data_male_germany_monthly['Pooled Variance'] / (data_male_germany1_monthly.shape[1] - 2)) + (data_male_germany_monthly['Pooled Variance'] / (data_male_germany2_monthly.shape[1] - 2)))).round(decimals=2)
data_female_germany_monthly['Margin of Error'] = (t_score_female_germany_monthly * np.sqrt((data_female_germany_monthly['Pooled Variance'] / (data_female_germany1_monthly.shape[1]- 2)) + (data_female_germany_monthly['Pooled Variance'] / (data_female_germany2_monthly.shape[1] - 2)))).round(decimals=2)

data_male_germany_monthly['{}% Confidence Interval Lower Bound'.format(confidence_level * 100)] = data_male_germany1_monthly['Mean'] - data_male_germany2_monthly['Mean'] - data_male_germany_monthly['Pooled Variance']
data_male_germany_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)] = data_male_germany1_monthly['Mean'] - data_male_germany2_monthly['Mean'] + data_male_germany_monthly['Pooled Variance']
data_female_germany_monthly['{}% Confidence Interval Lower Bound'.format(confidence_level * 100)] = data_female_germany1_monthly['Mean'] - data_female_germany2_monthly['Mean'] - data_female_germany_monthly['Margin of Error']
data_female_germany_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)] = data_female_germany1_monthly['Mean'] - data_female_germany2_monthly['Mean'] + data_female_germany_monthly['Margin of Error']

data_male_germany_monthly['Number of Pairs'] = data_male_germany_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)].round(decimals=0)
data_female_germany_monthly['Number of Pairs'] = data_female_germany_monthly['{}% Confidence Interval Upper Bound'.format(confidence_level * 100)].round(decimals=0)

data_male_germany1_monthly.loc['Total'] = data_male_germany1_monthly.sum()
data_male_germany2_monthly.loc['Total'] = data_male_germany2_monthly.sum()
data_male_germany_monthly.loc['Total'] = data_male_germany_monthly.sum()
data_female_germany1_monthly.loc['Total'] = data_female_germany1_monthly.sum()
data_female_germany2_monthly.loc['Total'] = data_female_germany2_monthly.sum()
data_female_germany_monthly.loc['Total'] = data_female_germany_monthly.sum()

data_male_germany_monthly.fillna(value=0, inplace=True)
data_female_germany_monthly.fillna(value=0, inplace=True)

print(data_male_germany1_monthly)
print(data_male_germany2_monthly)
print(data_male_germany_monthly)
print(data_female_germany1_monthly)
print(data_female_germany2_monthly)
print(data_female_germany_monthly)
