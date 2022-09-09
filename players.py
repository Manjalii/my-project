#!/usr/bin/env python
# coding: utf-8

# In[ ]:


players = [180, 172, 178, 185, 190, 195, 192]
mean = sum(players)/len(players)
var = 0
No_play = []
for i in players:
    i = (i-mean)**2
    var = var+i
    variance = var/len(players)
    std = variance**0.5
for i in players:
    if i>=(mean-std) and i<=(mean+std):
        No_play.append(i)
print(len(No_play))

