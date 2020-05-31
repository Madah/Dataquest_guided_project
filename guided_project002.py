#!/usr/bin/env python
# coding: utf-8

# # Summary of this curse
# 
# - how to work with strings
# - object-oriented programming
# - dates and times

# We are interested in titles begining with:
# - Ask HN
# - Show HN
# 
# Let's compare these types of posts to determine:
# - which receives more comments on average
# - at which time do posts receive more comments on average
# 

# # Importing the libraries needed and reading the dataset

# In[1]:


from csv import reader
hn = list(reader(open('hacker_news.csv')))


# In[2]:


#print(hn[:4])
print(hn[0])
print('\n')
print(hn[1])
print('\n')
print(hn[2])
print('\n')
print(hn[3])
print('\n')
print(hn[4])


# In[3]:


# extracting the header
headers = hn[0]


# In[4]:


# removing the header from the dataset
hn = hn[1:]


# In[5]:


print(headers)
print('\n')
print(hn[0])
print('\n')
print(hn[1])
print('\n')
print(hn[2])
print('\n')
print(hn[3])


# # Moving to filter out the data
# 
# Now to clean the data and keep just the posts that start with:
# - Ask HN
# - Show HN

# In[9]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1] #assigning the title to a variable
    
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# In[10]:


print(ask_posts[:3])
print(show_posts[:3])
print(other_posts[:3])


# > To find the total number of comments in ask posts:

# In[13]:


total_ask_comments = 0

for row in ask_posts:
    total_ask_comments += int(row[4])

avg_ask_comments = total_ask_comments/len(ask_posts)
print(avg_ask_comments)


# In[14]:


total_show_comments = 0

for row in show_posts:
    total_show_comments += int(row[4])
    
avg_show_comments = total_show_comments/len(show_posts)
print(avg_show_comments)


# On average 'Ask Posts' have an higher number os posts. Since ask posts receive more comments than show posts, the remaining analysis will focus on 'Ask Posts'

# # Ask Posts analysis

# It will be determined if there is a specific time that attracts more comments.
# 
# To do this:
# 1. Calculate the amount of ask posts created in each hour of the day, along with the number of comments received
# 2. Calculate the average number of comments ask posts receive by hour created 
# 

# In[15]:


import datetime as dt


# In[29]:


result_list = [] #this will be a list of lists

for row in ask_posts:
    #1st element is the 'created at', 2nd element is the number of comments
    result_list.append(
        [row[6], int(row[4])] 
    )
    
counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for row in result_list:
    hour = row[0]
    comment = row[1]
    
    objt_time = dt.datetime.strptime(hour, date_format) #convert to object datetime
    time = objt_time.strftime("%H") #extracts the hour and converts to string
    
    if time not in counts_by_hour:
        counts_by_hour[time] = 1
        comments_by_hour[time] = comment
    else:
        counts_by_hour[time] += 1
        comments_by_hour[time] += comment
        
counts_by_hour


# > PROGRESS SO FAR:
# 
# Created two dictionaries:
# - `counts_by_hour`: contains the number of ask posts created during each hour of the day
# - `comments_by_hour`: contains the corresponding number of comments ask posts created at each hour recieved

# > calculated the average number of comments per post for posts created during each hour of the day:

# In[31]:


avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour]/counts_by_hour[hour]])
    
avg_by_hour


# # Sorting the list
# 
# And print the five highest values in a format easier to read

# In[36]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap


# In[56]:


print("Top 5 Hours for Ask Posts Comments")
print("[converted from ET to GMT+1 (Summer Time)]")

for avg, hour in sorted_swap[:5]:
    
    lisbon_time = dt.datetime.strptime(hour, "%H") + dt.timedelta(hours=5)
    print(
        "{}: {:.2f} average comments per post".format(lisbon_time.strftime("%H:%M"), avg
        )

    )


# In[52]:


# Just a few tests to convert to Lisbon time (GMT+1 since it's Summer Time)

tempo = dt.datetime.strptime(sorted_swap[0][1], "%H")
gmt_tempo = tempo + dt.timedelta(hours=5)

print(gmt_tempo)

str_tempo = gmt_tempo.strftime("%H:%M")

str_tempo


# # Conclusions
# 
# > on average, there are more comments between 3pm-4pm ET (or 20h-21h GMT+1 - Lisbon Summer time)
# 
# However posts without comments were not included, therefore this conclusion applies to posts which were commented 

# In[ ]:





# In[ ]:




