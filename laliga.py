#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import logging
#yesterday gets yesterday's date in MMDDYYYY format and compare if that is a laliga matchday max date and proceed to get the prediction from 538 website

logging.basicConfig(filename="laliga.log",format='%(asctime)s %(message)s',filemode='a')

yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%m/%d/%Y")

df_match_day = pd.read_csv('LaLigaMatchday.csv')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

if yesterday not in df_match_day.Date.values:
    logger.info("not an end of matchday")
    exit()
# In[81]:
#else part
matchday_no = df_match_day.index[df_match_day['Date'] == yesterday].to_list()[0]
logger.info("it is end of matchday number: %d",matchday_no)
df = pd.read_html('https://projects.fivethirtyeight.com/soccer-predictions/la-liga/',attrs={'class': 'forecast-table'},header=2)
df = pd.DataFrame(df[0])


# In[83]:


df = df[['team','win La Ligawin league']]
#df.head()


# In[79]:


import re
def clean(team_name):
    #print(team_name)
    #print(re.sub("pts","",team_name))
    team_name = re.sub("\ pts","",team_name)
    return re.sub("[0-9]+","",team_name)



# In[91]:


def merge_col(row):
    if 'list' in str(type(row['Win League'])):
        lst = list(row['Win League'])
    else:
        lst = []
        lst.append(int(row['Win League']))

    lst.append(int(row['new column']))
    return lst



import re
df['win La Ligawin league'] = df['win La Ligawin league'].str.replace(r'\%','')
df['win La Ligawin league'] = df['win La Ligawin league'].str.replace(r'\<','')
df = df.rename(columns={'2':'rows','win La Ligawin league':'Win League'})
df['team'] = df['team'].apply(clean)
df = df.sort_values(by=['team'])
#df.head()


import glob
filename  = 'la liga.csv'
ispresent = glob.glob(filename)
if not ispresent:
    df.to_csv(filename,index=False,encoding='utf-8-sig')
    # exit here
    exit()
else:
    main_df = pd.read_csv(filename)
    print(main_df.head())

# In[88]:


main_df = pd.merge(main_df,df,on='team')
main_df = main_df.rename(columns = {'Win League_x':'Win League','Win League_y':'new column'})



main_df['Win League'] = main_df.apply(merge_col,axis = 1)
main_df = main_df.drop(['new column'],axis = 1)
main_df.to_csv(filename,index=False,encoding='utf-8-sig')
#main_df.head()
logger.info("Done writing to laliga.csv")
