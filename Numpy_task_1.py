#!/usr/bin/env python
# coding: utf-8

# 1.Write a python code to create a array in different ways

# ### creating a array

# In[1]:


# from list
list1 = [1,2,3,4,5,5,4,3]


# In[2]:


import numpy as np


# In[3]:


arr = np.array(list1)
arr


# In[4]:


type(arr)


# In[5]:


# from tuple
tup = (1,2,3,4,6,7,89,45)


# In[6]:


arr1 = np.array(tup)
arr1


# In[7]:


type(arr1)


# In[8]:


# direct array creation
arr2 = np.array([1,2,3,4,5,6,57,56])
arr2


# In[9]:


type(arr2)


# In[ ]:





# 2. Array Creation:
#     
#     a. Create a 1D Numpy array containing the first  12 positive integers as arr1.
#     
#     b. Create a 1D Numpy array1 with 20 elements containing integers between 0 and 12 using linspace.

# In[10]:


# a
arr1 = np.arange(1,13)
arr1


# In[11]:


# b 
array1 = np.linspace(0,12,20)
array1


# In[ ]:





# 3 . Find all atrributes of array1 and array2

# In[12]:


array1 = np.arange(1,13)
array1


# In[13]:


array2 =  np.linspace(0,12,20)
array2


# ### Attributes of array1

# In[14]:


array1.dtype


# In[15]:


array1.ndim


# In[16]:


array1.size


# In[17]:


array1.nbytes


# In[18]:


array1.itemsize


# ### Attributes of array2

# In[20]:


array2.dtype


# In[21]:


array2.ndim


# In[22]:


array2.size


# In[23]:


array2.nbytes


# In[24]:


array2.itemsize


# In[ ]:





# Apply measure and describe the data to above arrays usind Numpy.

# ### Measure of central tendancy of array1

# In[28]:


# Mean
np.mean(array1)


# In[29]:


#median
np.median(array1)


# ### Measure of spread of array1

# In[31]:


# range 
range1 = np.max(array1)-np.min(array1)
range1


# In[32]:


# varince
np.var(array1)


# In[33]:


# std
np.std(array1)


# ##### IOR of array1

# In[34]:


array1


# In[36]:


q3 = np.percentile(array1,75)
q3


# In[37]:


q1 = np.percentile(array1,25)
q1


# In[38]:


IQR = q3-q1
IQR


# ### to find outlier

# In[39]:


lower_limit = q1-(1.5 * IQR)
lower_limit


# In[40]:


upper_limit = q3+(1.5*IQR)
upper_limit


# In[42]:


array1>upper_limit


# In[45]:


array1<lower_limit


# - from above upper limit and lower limit both case are fail, hence there is no outlier

# In[ ]:





# ### Measure of central Tendancy of array2

# In[46]:


array2


# In[47]:


# mean
np.mean(array2)


# In[48]:


# median
np.median(array2)


# ### Measure of spread

# In[49]:


# range
range2 = np.max(array2)-np.min(array2)
range2


# In[50]:


# varinace
np.var(array2)


# In[51]:


# std
np.std(array2)


# ##### IQR

# In[53]:


q1 = np.percentile(array2,25)
q1


# In[54]:


q3 = np.percentile(array2,75)
q3


# In[55]:


# IQR
IQR = q3-q1
IQR


# #### To find outlier of array2

# In[56]:


array2


# In[57]:


lower_limit = q1-(1.5*IQR)
lower_limit


# In[58]:


upper_limit = q3+(1.5*IQR)
upper_limit


# In[59]:


array2>upper_limit


# In[61]:


array2<lower_limit


# - from above upper limit and lower limit both case are fail, hence there is no outlier

# In[ ]:




