#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('task.php') as f:
    x = f.read()


# In[2]:


if '<?php' in x:
    print('OK')
else:
    print('not OK')


# In[ ]:




