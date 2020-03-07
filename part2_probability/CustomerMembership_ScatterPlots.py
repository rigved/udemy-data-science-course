import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_excel('Customers_Membership.xlsx', sheet_name='Membership Status', usecols='A:B')

print(data)

plt.figure()

sns.set(color_codes=True)
sns.regplot(x='Customer Age', y='Membership Status', data=data, logistic=True)

plt.show()
