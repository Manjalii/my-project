#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000])
mean = np.mean(data)
std = np.std(data)
satisfy = []
for i in data:
    if i>=(mean-std) and i<=(mean+std):
        satisfy.append(i)
print((len(satisfy)/len(data))*100)

