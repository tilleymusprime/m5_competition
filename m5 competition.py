#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


calendar = pd.read_csv('C://Users//tilleymusprime//Desktop//calendar.csv') #Calendar Data
ste = pd.read_csv('C://Users//tilleymusprime//Desktop//sales_train_evaluation.csv')
stv = pd.read_csv('C://Users//tilleymusprime//Desktop//sales_train_validation.csv') # Won't need this sheet until testing


# In[73]:


print(calendar.shape)
print(ste.shape)
print(stv.shape)
stecols = ['id', 'item_id', 'dept_id', 'cat_id', 'store_id', 'state_id']


# In[78]:


date = list(calendar['date'])
date1 = date[0:1941]
df = pd.DataFrame()
df['Date'] = date1
df['Date'].replace('/', '-', inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d')
df['Date']


# In[82]:


#First, let's take a look at each state
ca = ste[ste['state_id'] == 'CA']
print(ca.shape)
wi = ste[ste['state_id'] == 'WI']
print(wi.shape)
tx = ste[ste['state_id'] == 'TX']
print(tx.shape)
##It looks like there are more rows in the CA dataframe. Let's look and see why that is


# In[83]:


print(ca.columns)
ca.drop(['id', 'dept_id', 'item_id', 'store_id', 'state_id'], axis=1, inplace=True)
print(ca.columns)


# In[88]:


cadfinda = list(ca.columns)
cats = list(ca['cat_id'])
cadfind = cadfinda[1:]
cadf = pd.DataFrame(index=cadfind, columns = cats)
cadf


# In[ ]:





# In[5]:


print(ca['store_id'].value_counts())
print(wi['store_id'].value_counts())
print(tx['store_id'].value_counts())
#It looks like there are 4 stores in California and 3 stores in Wisconsin and Texas


# In[ ]:





# In[ ]:





# In[44]:


##California By Store
#In this section, we will look at each store in california
ca1 = ca[ca['store_id'] == 'CA_1']
ca2 = ca[ca['store_id'] == 'CA_2']
ca3 = ca[ca['store_id'] == 'CA_3']
ca4 = ca[ca['store_id'] == 'CA_4']
print(stecols)


# In[ ]:





# In[13]:


print("Ca Store 1 Categories: \n:", ca1['cat_id'].value_counts())
print("Ca Store 2 Categories: \n:", ca2['cat_id'].value_counts())
print("Ca Store 3 Categories: \n:", ca3['cat_id'].value_counts())
print("Ca Store 4 Categories: \n:", ca4['cat_id'].value_counts())


# In[14]:


print("Ca Store 1 Departments: \n:", ca1['dept_id'].value_counts())
print("Ca Store 2 Departments: \n:", ca2['dept_id'].value_counts())
print("Ca Store 3 Departments: \n:", ca3['dept_id'].value_counts())
print("Ca Store 4 Departments: \n:", ca4['dept_id'].value_counts())


# In[15]:


print("Ca Store 1 Items: \n:", ca1['item_id'].value_counts())
print("Ca Store 2 Items: \n:", ca2['item_id'].value_counts())
print("Ca Store 3 Items: \n:", ca3['item_id'].value_counts())
print("Ca Store 4 Items: \n:", ca4['item_id'].value_counts())


# In[72]:


ca1_hobbies = ca1[ca1['cat_id'] == 'HOBBIES']
print(ca1_hobbies.shape)
print(ca1_hobbies.head())


# In[54]:


ca1_hobbies.columns


# In[60]:


calendar.columns


# In[71]:


date = list(calendar['date'])
df = pd.DataFrame()
df['Date'] = date
df['Date'].replace('/', '-', inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d')
df['Date']


# In[ ]:





# In[69]:


ca1_hobbies_items = list(ca1_hobbies['item_id'])
print(len(ca1_hobbies_items))


# In[70]:


ca1_hobbies_items = list(ca1_hobbies['item_id'])
for i in ca1_hobbies_items:
    df1 = ca1_hobbies[ca1_hobbies['item_id'] == i]
    print(df1.shape)
    dfarray = np.array(df1.iloc[0, 6:])
    print(len(dfarray))
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[49]:


ca1_hobbies11= np.array(ca1_hobbies.iloc[0, 6:])
ca1_hobbies11


# In[ ]:





# In[43]:





# In[ ]:


ca1.groupby('dept_id')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


##Wisconsin
wi1 = wi[wi['store_id'] == 'WI_1']
wi2 = wi[wi['store_id'] == 'WI_2']
wi3 = wi[wi['store_id'] == 'WI_3']


# In[ ]:





# In[ ]:


#Texas By Store
tx1 = tx[tx['store_id'] == 'TX_1']
tx2 = tx[tx['store_id'] == 'TX_2']
tx3 = tx[tx['store_id'] == 'TX_3']


# In[ ]:





# In[14]:


expste = pd.DataFrame(ste.iloc[:100, :100])
print(expste.shape)
#expste.to_csv('C://Users//tilleymusprime//Desktop//sales_train_eval_mini.csv')


# In[15]:


expste.columns


# In[20]:


print(ste['id'].value_counts())
#print(ste['d_5'].value_counts())
print(ste['dept_id'].value_counts())


# In[22]:


print(ste['store_id'].value_counts())
print(ste['state_id'].value_counts())


# In[ ]:


print(ca['store_id']


# In[5]:


print(calendar.shape)
print(calendar.columns)
print(calendar.head())


# In[7]:


stecols = list(ste.columns)
print(stecols)


# In[9]:


print(ste['state_id'].value_counts())


# In[10]:


ste['store_id'].value_counts()


# In[12]:


ste['cat_id'].value_counts()


# In[14]:


ste['dept_id'].value_counts()


# In[16]:


ste['item_id'].value_counts()


# In[17]:


print(ste['d_1'].value_counts())

