#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[65]:


df=pd.read_csv('311_Service_Requests_from_2010_to_Present.csv')


# In[66]:


df.head()


# In[67]:


df.shape


# In[68]:


#checking for null values
df.isnull().any()


# In[69]:


df.isnull().sum()


# In[70]:


#droping columns
df =df.drop(['School or Citywide Complaint','Vehicle Type','Taxi Company Borough', 'Taxi Pick Up Location',
            'Garage Lot Name'], axis=1)
df.head()


# In[71]:


#display city names
df['City'].unique()


# In[72]:


#changing city names into title form
def to_title(city):
    try:
        city= city.title()
        return city
    except:
        return np.nan
    
df['City'] = df['City'].apply(to_title)
df['City'].value_counts()


# In[73]:


df['Complaint Type'].value_counts()


# In[74]:


#types of complaints in each city in a separate dataset
df.groupby(['City', 'Complaint Type']).size()


# In[75]:


#Displaying all type of complaints
df['Complaint Type'].value_counts().plot(kind="bar",color=list('rgbkymc'),alpha=0.7,figsize=(20,6))
plt.title(" All Types of complaints  ")


# In[76]:


#city wise complaints
ny=df.loc[df['City']== 'New York']
ny['Complaint Type'].value_counts().plot(kind="bar",figsize=(20,6))
plt.title("complaints in New York City ")


# In[77]:


brooklyn = df.loc[df['City']== 'Brooklyn']


# In[84]:


brooklyn=df.loc[df['City']== 'Brooklyn']
brooklyn['Complaint Type'].value_counts().plot(kind="bar",figsize=(20,6))
plt.title("complaints in Brooklyn")


# In[79]:


#Scatter plots for complaint concentration across Brooklyn
brooklyn[['Longitude', 'Latitude']].plot(kind="scatter", x= 'Longitude',y= 'Latitude',figsize=(20,6))
plt.title("Complaint Concentration in Brooklyn")


# In[80]:


#Hexbin plots for complaint concentration across Brooklyn
brooklyn[['Longitude', 'Latitude']].plot(kind="hexbin", x= 'Longitude',y= 'Latitude',gridsize=40,figsize=(20,6))
plt.title("Complaint Concentration in Brooklyn")


# In[81]:


#Plot a bar graph of count vs. complaint types
df['Complaint Type'].value_counts().plot(kind="bar",color=list('rgbkymc'),alpha=0.7,figsize=(20,7))
plt.title('Complaint Counts vs Complaint Types')
plt.xlabel('Complaint Type')
plt.ylabel('Complaint Counts')
plt.show()


# In[82]:


#Find the top 10 types of complaints
df['Complaint Type'].value_counts()[:10].plot(kind="bar",color=list('rgbkymc'),alpha=0.7,figsize=(20,5))
plt.title("Top 10 Complaints")


# In[83]:


#coverting Created and Closed Date into datetime
df['Created Date']= pd.to_datetime(df['Created Date'])
df['Closed Date'] = pd.to_datetime(df['Closed Date'])


# In[85]:


df.loc[df['Created Date']>=df['Closed Date']].shape


# In[86]:


#droping empty rows of Closed Date
df=df[df['Closed Date'].notnull()]


# In[87]:


#Calculating Avg_Rsponse_Time 
df['Avg_Rsponse_Time']= (df['Closed Date']-df['Created Date']).dt.days


# In[88]:


df.head()


# In[89]:


#average response time across various types of complaints
df.groupby('Complaint Type')['Avg_Rsponse_Time'].mean().sort_values()


# In[ ]:





# In[ ]:




