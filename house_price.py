#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
mean = np.mean(data)
std = np.std(data)
satisfy = []
for i in data:
    if i>=(mean-std) and i<=(mean+std):
        satisfy.append(i)
print((len(satisfy)/len(data))*100)

