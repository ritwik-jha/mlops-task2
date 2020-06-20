#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib


# In[2]:


s = smtplib.SMTP('smtp.gmail.com', 587) 


# In[3]:


s.starttls() 


# In[ ]:


s.login("ritwikjha46@gmail.com", "**************") 
  
message = "the site is not working"
  
s.sendmail("ritwikjha46@gmail.com", "dev@gmail.com", message) 

s.quit() 

