#!/usr/bin/env python
# coding: utf-8

# In[13]:


print('This {} is a string '.format('INSERTED'))


# --- STRING CAN BE INSERTED VIA INDEX POSITION ---- {INDEX}  ---> always follows .format(0,1,2,...). -> 0,1,2.... are index positions. 

# In[14]:


print('The {2} {1} {0}'.format("fox", 'brown', "quick"))


# In[15]:


print('The {2} {1} {1}'.format("fox", 'brown', "quick"))


# In[18]:


print('The {q} {b} {f}'.format(f="fox", b='brown', q="quick"))   

#you are assigning keywords (kind of variables) inside the .format function.


# # FLOAT FORMATIING  
# 
# GENRAL FORMAT : {value:widht.precision f}  --> 
# 
# value is the variable (if you have 
# width: adds white spaces
# precision: 
# 

# In[20]:


result=100/777
result


# In[25]:


print("The result is {r:10.2f}".format(r=result))


# 
# 
# # FORMATTED STRING LITTERAL - FSTRING 
# 
# FORMATING RESOURCE: https://pyformat.info/
# 
# 
# 

# In[27]:


name = "Elena "

print(f'Hello my name is {name}')


# In[28]:


name = "Elena "
age=23

print(f'{name} is {age} years old.')


# # LISTS  & DICTIONARIES

# In[33]:


my_list=[1,2,"ella", 4,5,6]
print(my_list)


# In[40]:


d={"key1":['a',2,3,4], "key2":"dictionary", "key3": 2}


# In[41]:


d


# In[42]:


d["key1"][0].upper()


# In[47]:


d.values()
d.keys()
d.items()


# In[ ]:




