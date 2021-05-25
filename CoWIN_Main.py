#!/usr/bin/env python
# coding: utf-8
'''
File: Covid Vaccine Tacker
Dev.: Abhisek Ghosh
Date: 25/05/2021
'''
# In[207]:


import requests
import json
import pandas as pd
from playsound import playsound
from datetime import datetime
import time
import webbrowser


# In[189]:


t1 = datetime.now()


# In[191]:


t2 = datetime.now()


# In[174]:


date = input('Enter Date(DD/MM/YYYY format only) => ')
date = int(date.replace('/', ''))
dist_code = input("Enter District code => ")
age = int(input('Enter age => '))


# URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=717&date=25052021"
# header = {
#     'User-Agent':
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
# }

# In[175]:


URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
    dist_code, date)
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
}


# # Manual

# In[ ]:


res = requests.get(URL, headers=header)


# In[177]:


response_json = res.json()
response_df = pd.DataFrame(dict(response_json)['sessions'])
#response_df.head()


# In[178]:


filter_df = response_df[(response_df.min_age_limit == age) & (response_df.available_capacity > 0)]

#filter_df
   


# In[179]:


filter_df.columns


# In[180]:


from tkinter import *

if filter_df.shape[0] > 0:
    root = Tk()
    root.title('CoWIN Vaccine Tracker')
    root.geometry('1000x800')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set, width = 150)
    print("\n\n ***Vaccine centre/s found*** ")
    for m in range(0,2):
        playsound('Alarm.mp3')
    webbrowser.open("https://selfregistration.cowin.gov.in/", new=1)
    for i in range(filter_df.shape[0]):
        Data = "Centre Name : {}, Address : {}, Pin :{}, Total dose :{}, Vaccine Type :{}".format(
            filter_df.name.iloc[i], filter_df.address.iloc[i],
            filter_df.pincode.iloc[i], filter_df.available_capacity.iloc[i],
            filter_df.vaccine.iloc[i])
        mylist.insert(END, Data)

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    mainloop()




