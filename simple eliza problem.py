#!/usr/bin/env python
# coding: utf-8

# In[2]:


message='Good Day'
message+=""" Please enter your problem, or enter i am feeling great or Q TO QUIT """
answer= True
while not answer=='I am feeling great' and not answer=='Q'and not answer=='q':
    answer=input(message.upper())
    print(answer.upper())
    if  answer=='Q' and answer=='q':
        print('OK')
    if  answer=='I am feeling great':
        print('ok')
        print(answer)
print('good bye')
    


# In[ ]:




