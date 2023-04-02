
import numpy as np
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')


stocks = pd.read_csv(
    "/content/drive/MyDrive/Making Money Project/w7daf8uqcgnpvs0d.csv")
stocks.head()


stocks.head()
close = stocks[['tic', 'prccd', 'datadate']]
close['rettoday'] = (close['prccd'] - close['prccd'].shift(1))/100
close['retyest'] = close["rettoday"].shift(1)

delta = .2
mindelt = 1-delta
pldelt = 1+delta
close['retyestmin'] = mindelt*close["retyest"]
close['retyestpl'] = pldelt*close["retyest"]
close.head()

close['greater'] = close[["retyestmin", "rettoday", "retyestpl"]].apply(
    lambda x: 1
    if (x.rettoday >= 0 and x.retyestmin <= x.rettoday and x.retyestpl >= x.rettoday)
    else 0,
    axis=1
)

close['less'] = close[["retyestmin", "rettoday", "retyestpl"]].apply(
    lambda x: 1
    if (x.rettoday < 0 and x.retyestpl <= x.rettoday and x.retyestmin >= x.rettoday)
    else 0,
    axis=1
)

close['result'] = close[["greater", "less", ]].apply(
    lambda x: 1
    if (x.greater or x.less)
    else 0,
    axis=1
)

insert = {'tic': "ABCD",
          'datadate': "2010-01-05",
          'prccd': 90,
          'rettoday': .9,
          'retyest': .8,
          'retyestmin': .8,
          'retyestpl': 1}
close.append(insert, ignore_index=True)
# close['greater'] = np.where(close['retyestmin'].tolist() <= close['rettoday'].tolist() and close['retyestpl'].tolist() >= close['rettoday'].tolist(), 1, 0)
close[close['greater'] == 1].head()
