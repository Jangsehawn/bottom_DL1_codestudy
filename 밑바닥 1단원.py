#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x=np.array([1,2,3])
print(x)


# In[3]:


type(x)


# In[5]:


a=np.array([[1,2],[3,4]])
print(a)


# In[9]:


x=np.array([[51,55],[14,19],[0,4]])
print(x)
x[0]


# In[10]:


for i in x:
    print(i)


# In[11]:


x=x.flatten()
print(x)


# In[12]:


x[np.array([0,2,4])]


# In[26]:


x[True,False]#bool값을 갖고있는 tuple형이므로 비어있는 array로 출력


# In[21]:


print(x[x>15])
print(x>15)
x


# In[28]:


import matplotlib.pyplot as plt


# In[31]:


x=np.arange(0,6,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()


# In[35]:


x=np.arange(0,6,0.1)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cos',linestyle="--")
plt.legend()
plt.title('sin&cos')
plt.show()


# In[36]:


from matplotlib.image import imread


# In[41]:


img= imread('C:/Users/장세환/Documents/카카오톡 받은 파일/KakaoTalk_20181028_195127089.jpg')
plt.imshow(img)
plt.show()

