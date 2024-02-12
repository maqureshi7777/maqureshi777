#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[5]:


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

col = ['preg' , 'plas' , 'pres' , 'skin' , 'test', 'pedi' , 'mass' , 'age' , 'Results']

df = pd.read_csv(url , names= col)

df


# In[7]:


x = df.iloc[: , 0:8]

x


# In[8]:


y = df.iloc[: , -1]

y


# In[9]:


X_train , X_test , y_train , Y_test = train_test_split(x,y , test_size=0.2 , random_state= 101)


# In[10]:


model = LogisticRegression()
model.fit(X_train , y_train)


# In[11]:


model.predict(X_test)


# In[12]:


model.score(X_test , Y_test)


# In[ ]:





# In[ ]:





# In[ ]:




