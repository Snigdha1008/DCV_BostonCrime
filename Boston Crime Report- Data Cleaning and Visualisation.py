#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


crime = pd.read_csv("crime_boston.csv")


# In[5]:


crime


# In[6]:


crime.isnull()


# In[7]:


crime.isnull().any(axis=1)


# In[8]:


rows_with_missing_values = crime.isnull().any(axis=1)


# In[9]:


crime[rows_with_missing_values]


# In[10]:


cleaned_crime = crime.drop(columns=['YEAR', 'MONTH', 'HOUR'])


# In[11]:


cleaned_crime


# In[12]:


cleaned_crime['OFFENSE_CODE_GROUP'].unique()


# In[13]:


cleaned_crime['OFFENSE_DESCRIPTION'].unique()


# In[16]:


cleaned_crime = crime.drop(columns='Location')


# In[17]:


cleaned_crime


# In[18]:


cleaned_crime


# In[19]:


import numpy as np
import seaborn as sn


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


sn.countplot(x='OFFENSE_CODE_GROUP', y = '', data = cleaned_crime)


# In[23]:


cleaned_crime['YEAR']


# In[24]:


cleaned_crime['YEAR'] ==2019 


# In[25]:


cleaned_crime1= cleaned_crime.loc[cleaned_crime['YEAR'] ==2019,: ]


# In[26]:


cleaned_crime1


# In[27]:


cleaned_crime['OFFENSE_CODE_GROUP'] =="Warrant Arrests"


# In[28]:


cleaned_crime2= cleaned_crime.loc[cleaned_crime['OFFENSE_CODE_GROUP'] =="Warrant Arrests",: ]


# In[29]:


cleaned_crime2


# In[31]:


sn.countplot(x="DAY_OF_WEEK", data=cleaned_crime2); plt.ylabel("Count of Warrant Arrests")


# In[47]:


sn.countplot(x="DISTRICT", data=cleaned_crime2); plt.ylabel("Count of Warrant Arrests")


# In[ ]:




