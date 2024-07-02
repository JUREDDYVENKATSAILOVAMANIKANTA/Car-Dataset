#!/usr/bin/env python
# coding: utf-8

# # Car Dataset

# In[1]:


import pandas as pd


# In[7]:




car = pd.read_csv( r"‪C:\Users\\2024.csv".replace('\u202a', '')



# In[8]:


car.head()


# In[9]:


car.shape


# In[10]:


#data Cleaning ( null values)


# In[19]:


car.isnull().sum()


# In[17]:


car['body_styles'].fillna(car['body_styles'].mean(),inplace = True)


# In[15]:


car


# In[20]:


#value count function


# In[21]:


car.head(2)


# In[24]:


car['make'].value_counts()


# In[25]:


#filtering 


# In[26]:


car.head(2)


# In[28]:


car[car['make'].isin(['Acura','Volvo'])]


# In[29]:





# In[ ]:




