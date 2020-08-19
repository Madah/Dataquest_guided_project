#!/usr/bin/env python
# coding: utf-8

# # Guided project 5
# 
# This guided project aims at exploring how to export the final diagram created as an image file.

# In[10]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()


# # Part 2

# In[11]:


cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(18, 20))

# Filling in the plots for the STEM categories
for sp in range(0,len(stem_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if index == 0:
        ax.text(2005, 87, 'Women')
        ax.text(2005, 8, 'Men')
    elif index == len(stem_cats)-1:
        ax.text(2005, 75, 'Men')
        ax.text(2005, 25, 'Women')

# Filling in the plots for the Liberal Arts categories
for sp in range(0,len(lib_arts_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+2)
    
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(lib_arts_cats)-1:
        ax.text(2005, 55, 'Men')
        ax.text(2005, 40, 'Women')

# Filling in the plots for the Other categories
for sp in range(0,len(other_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+3)
    
    ax.plot(women_degrees['Year'], women_degrees[other_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(other_cats)-1:
        ax.text(2005, 65, 'Men')
        ax.text(2005, 30, 'Women')
          
    
plt.show()


# # Part 3
# Removing the labelbottom

# In[12]:


cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(18, 20))

# Filling in the plots for the STEM categories
for sp in range(0,len(stem_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 87, 'Women')
        ax.text(2005, 8, 'Men')
    elif index == len(stem_cats)-1:
        ax.text(2005, 75, 'Men')
        ax.text(2005, 25, 'Women')
        ax.tick_params(labelbottom='on')

# Filling in the plots for the Liberal Arts categories
for sp in range(0,len(lib_arts_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+2)
    
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(lib_arts_cats)-1:
        ax.text(2005, 55, 'Men')
        ax.text(2005, 40, 'Women')
        ax.tick_params(labelbottom='on')

# Filling in the plots for the Other categories
for sp in range(0,len(other_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+3)
    
    ax.plot(women_degrees['Year'], women_degrees[other_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(other_cats)-1:
        ax.text(2005, 65, 'Men')
        ax.text(2005, 30, 'Women')
        ax.tick_params(labelbottom='on')
          
    
plt.show()


# # Part 4
# 
# Setting the y-axis labels

# In[13]:


cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(18, 20))

# Filling in the plots for the STEM categories
for sp in range(0,len(stem_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(stem_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 87, 'Women')
        ax.text(2005, 8, 'Men')
    elif index == len(stem_cats)-1:
        ax.text(2005, 75, 'Men')
        ax.text(2005, 25, 'Women')
        ax.tick_params(labelbottom='on')

# Filling in the plots for the Liberal Arts categories
for sp in range(0,len(lib_arts_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+2)
    
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(lib_arts_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(lib_arts_cats)-1:
        ax.text(2005, 55, 'Men')
        ax.text(2005, 40, 'Women')
        ax.tick_params(labelbottom='on')

# Filling in the plots for the Other categories
for sp in range(0,len(other_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+3)
    
    ax.plot(women_degrees['Year'], women_degrees[other_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(other_cats[index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(other_cats)-1:
        ax.text(2005, 65, 'Men')
        ax.text(2005, 30, 'Women')
        ax.tick_params(labelbottom='on')
          
    
plt.show()


# # Part 5
# 
# Adding a horizontal line

# In[18]:


cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(18, 20))

# Filling in the plots for the STEM categories
for sp in range(0,len(stem_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(stem_cats[index])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 87, 'Women')
        ax.text(2005, 8, 'Men')
    elif index == len(stem_cats)-1:
        ax.text(2005, 75, 'Men')
        ax.text(2005, 25, 'Women')
        ax.tick_params(labelbottom='on')

# Filling in the plots for the Liberal Arts categories
for sp in range(0,len(lib_arts_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+2)
    
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(lib_arts_cats[index])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(lib_arts_cats)-1:
        ax.text(2005, 55, 'Men')
        ax.text(2005, 40, 'Women')
        ax.tick_params(labelbottom='on')

# Filling in the plots for the Other categories
for sp in range(0,len(other_cats)*3,3):
    index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+3)
    
    ax.plot(women_degrees['Year'], women_degrees[other_cats[index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[index]], c=cb_orange, label='Men', linewidth=3)
    
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(other_cats[index])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    
    if index == 0:
        ax.text(2005, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif index == len(other_cats)-1:
        ax.text(2005, 65, 'Men')
        ax.text(2005, 30, 'Women')
        ax.tick_params(labelbottom='on')
    

plt.savefig('gender_degrees.png')    
plt.show()


# In[17]:


plt.get_backend()


# In[ ]:





# In[ ]:




