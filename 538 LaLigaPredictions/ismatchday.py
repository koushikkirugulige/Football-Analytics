#updates the LaLigaMatchday CSV file once every week

#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import logging
logging.basicConfig(filename="MatchdayLaliga.log", format='%(asctime)s %(message)s', filemode='a')
url ='https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F12%2Fschedule%2FLa-Liga-Scores-and-Fixtures&div=div_sched_ks_10731_1'

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

# In[2]:

df = pd.read_html(url,encoding = 'utf_8')[0]
df.drop_duplicates(inplace=True)
#display(df)

# In[3]:

idx =df.groupby(['Wk'], sort=False)['Date'].transform(max) == df['Date']
df_match_day = df.groupby(['Wk'], sort=False)['Date'].max().to_frame()
if df_match_day.empty == True:
    logger.info("The returned DataFrame is empty")

# In[4]:

df_match_day.to_csv('LaLigaMatchday.csv',index=False)
logger.info("Successfully updated LaLigaMatchday.csv")
