# -*- coding: utf-8 -*-
"""eda-scatter-plots.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jprZmEsJeWSBuAL497G4U5n818my8bPP
"""

import pandas as pd

BANKS = 'banklist.csv'

df = pd.read_csv(filepath_or_buffer=BANKS, encoding='windows-1250',)
df.columns = [column.strip() for column in df.columns]
df['Closing Date'] = pd.to_datetime(arg=df['Closing Date'], dayfirst=True)
df['year'] = df['Closing Date'].dt.year

df.head()

from plotly import express

express.histogram(data_frame=df, x='Fund', ).show()

express.histogram(data_frame=df, x='Closing Date').show()

express.histogram(data_frame=df, x='State')

express.scatter(data_frame=df, x='Closing Date', y='Fund', size='Fund', hover_name='Bank Name', color='year')

express.strip(data_frame=df, x='Closing Date',  hover_name='Bank Name', hover_data=['Acquiring Institution', 'Fund'])

express.scatter(data_frame=df, x='State', y='Closing Date', size='Fund', hover_name='Bank Name', height=800, marginal_y='rug', color='Fund')