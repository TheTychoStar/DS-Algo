# demo of pandas

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://data.ontario.ca/dataset/5472ffc1-88e2-48ca-bc9f-4aa249c1298d/resource/66d15cce-bfee-4f91-9e6e-0ea79ec52b3d/download/ongoing_outbreaks.csv'
df = pd.read_csv(url)

# Shape of df
print(df.shape)

# Preview first 3 rows of df
print(df.head(3))
'''
>>>          date     outbreak_group       outbreak_subgroup  number_ongoing_outbreaks
    0  11/01/2020  1 Congregate Care  1 Long-Term Care Homes                        73
    1  11/01/2020  1 Congregate Care             2 Hospitals                        21
    2  11/01/2020  1 Congregate Care      3 Retirement Homes                        51
'''

# Review col
print(df.columns)
'''>>> ['date', 'outbreak_group', 'outbreak_subgroup', 'number_ongoing_outbreaks']'''

# Review types
print(df.dtypes)
'''
>>> date                        object
    outbreak_group              object
    outbreak_subgroup           object
    number_ongoing_outbreaks     int64
'''

# group by outbreak_group
print(df.groupby(['outbreak_group']).sum())
'''                     
>>> outbreak_group                           number_ongoing_outbreaks            
    1 Congregate Care                        8660
    2 Congregate Living                      2757
    3 Education                              6459
    4 Workplace                              8514
    5 Recreational                           2217
    6 Other/Unknown                           884
'''

# group by date
df_date = df[['date', 'number_ongoing_outbreaks']].groupby(['date']).sum()
# Without slice it also works
print(df_date)
'''            
>>> date                             number_ongoing_outbreaks                    
    11/01/2020                       461
    11/02/2020                       461
    11/03/2020                       474
    11/04/2020                       492
    11/05/2020                       503
    11/06/2020                       517
    11/07/2020                       542
    .                                 .
    .                                 .
    .                                 .
'''
# Show line chart
df_date.plot()
plt.show()

# Show pie plot
df.groupby(['outbreak_group']).sum().plot.pie(y='number_ongoing_outbreaks',
                                              autopct='%1.2f%%',
                                              textprops={'color': 'b'},
                                              figsize=(10, 10))
plt.show()