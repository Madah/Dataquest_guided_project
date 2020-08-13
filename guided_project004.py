#!/usr/bin/env python
# coding: utf-8

# # Guided project 4
# 
# The purpose of this project is to explore how to use pandas plotting for quickly explore data using visualizations.
# The dataset used represents the job outcomes of students who graduated from college between 2010 and 2012. The original data was released by the American Community Survey. It can be found in the Github repo of FiveThirtyEight [here](https://github.com/fivethirtyeight/data/tree/master/college-majors). 
# 
# A few of the questions to be answered:
# - Do students in more popular majors make more money?
# - How many majors are predominantly male? Prefominantly female?
# - Which category of majors have the most students?

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
recent_grads = pd.read_csv('recent-grads.csv')
print(recent_grads.iloc[0])


# In[2]:


recent_grads.head()


# In[3]:


recent_grads.tail()


# In[4]:


print(recent_grads.describe())


# In[5]:


raw_data_count = recent_grads.shape[0]
print(raw_data_count)


# In[6]:


recent_grads = recent_grads.dropna()


# In[7]:


cleaned_data_count = recent_grads.shape[0]
print(cleaned_data_count)


# - Rank - Rank by median earnings (the dataset is ordered by this column).
# - Major_code - Major code.
# - Major - Major description.
# - Major_category - Category of major.
# - Total - Total number of people with major.
# - Sample_size - Sample size (unweighted) of full-time.
# - Men - Male graduates.
# - Women - Female graduates.
# - ShareWomen - Women as share of total.
# - Employed - Number employed.
# - Median - Median salary of full-time, year-round workers.
# - Low_wage_jobs - Number in low-wage service jobs.
# - Full_time - Number employed 35 hours or more.
# - Part_time - Number employed less than 35 hours

# # part 2 - Pandas, Scatter Plots

# - test example

# In[8]:


#recent_grads.plot(x='Sample_size', y='Employed', kind='scatter', title='Employed vs. Sample_size', figsize=(5,10))

ax = recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')
ax.set_title('Employed vs. Sample_size');


# In[9]:


recent_grads.columns


# In[10]:


ax1 = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax1.set_title('Sample_size vs. Median');


# In[11]:


ax2 = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
ax2.set_title('Sample_size vs. Unemployment_rate');


# In[12]:


ax3 = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax3.set_title('Full_time vs. Median');


# In[13]:


ax4 = recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')
ax4.set_title('ShareWomen vs. Unemployment_rate');


# In[14]:


ax5 = recent_grads.plot(x='Men', y='Median', kind='scatter')
ax5.set_title('Men vs. Median');


# In[15]:


ax6 = recent_grads.plot(x='Women', y='Median', kind='scatter')
ax6.set_title('Women vs. Median');


# # Part 3 - Pandas, Histograms

# In[16]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(12,30));

for i in range(0,8):
    ax = fig.add_subplot(8,1,i+1)
    ax = recent_grads[cols[i]].hist(bins=25)


# In[17]:


fig = plt.figure(figsize=(12,30));

for i in range(0,8):
    ax = fig.add_subplot(8,1,i+1)
    ax = recent_grads[cols[i]].hist(bins=100)


# # Part 4 - Pandas, Scatter Matrix Plot

# In[18]:


from pandas.plotting import scatter_matrix

scatter_matrix(recent_grads[["Sample_size","Median"]], figsize=(10,10));


# In[19]:


scatter_matrix(recent_grads[["Sample_size","Median","Unemployment_rate"]], figsize=(10,10));


# # Part 5 - Pandas, Bar Plots

# In[29]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[-10:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[ ]:





# In[ ]:





# In[ ]:




