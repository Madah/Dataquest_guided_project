#!/usr/bin/env python
# coding: utf-8

# # Profitable App Profiles for the App Store and Google Play Markets
# 
# - Performe an analysis on the data from the built apps. These are free to download and install, hence the source of revenue consists of in-app ads.
# - the goal of this project is to analyze data and retrieve useful information to allow developers to create new apps that are likely to attract more users.

# In[2]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')
    
    if rows_and_columns:
        print('Number of rows: ', len(dataset))
        print('Number of columns: ', len(dataset[0]))
        


# In[3]:


from csv import reader

#opened_apple = open('/home/madaleno/Documents/Dataquest/my_datasets/AppleStore.csv');
#opened_google = open('/home/madaleno/Documents/Dataquest/my_datasets/googleplaystore.csv');
opened_apple = open('AppleStore.csv');
opened_google = open('googleplaystore.csv');


apple_data = list(reader(opened_apple))
google_data = list(reader(opened_google))


# In[4]:


explore_data(apple_data,0,5,True)


# In[5]:


explore_data(google_data,0,5,True)


# In[6]:


explore_data(google_data,0,1)
explore_data(google_data,10473,10474)
print(google_data[10473])


# # Delete data
# 
# Delete data that is wrong. In this case the rating is wrong

# In[7]:


del google_data[10473]


# In[8]:


explore_data(google_data,0,2,True)


# # Duplicate entries
# 
# If you explore the Google Play data set long enough, you'll notice some apps have duplicate entries.

# In[9]:


# Google data without the header:
android = google_data[1:]
# header on a separate variable
android_header = google_data[0]

print(android_header)
print('\n')
print(android[0])
print('\n')

# Apple Store data without the header
ios = apple_data[1:]
# header on a separate variable
ios_header = apple_data[0]


# In[10]:


for app in android:
    name = app[0]
    if name == 'Instagram':
        print(name)


# Now I will count the number of duplicates. This can be achieved by:
# - creating a list for the unique values
# - creating a second list for the duplicate values
# - show the length (len() command) of the list containing the duplicate values

# In[11]:


duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
        
print('Number of duplicate apps in android dataset: ', len(duplicate_apps))
print('\n')
print('Number of unique apps in android dataset: ', len(unique_apps))


# To prevent removing apps randomly I am setting a criteria, which in this case will be the number of reviews. The one row with the highest number of reviews will be kept in the data. All others will be deleted. 
# This can be achieved by:
# - creating a dictionary where the key is the individual app name, the value is the highest number of reviews;
# - from the dictionary, a new dataset will be created with a single entry per app (corresponding to the one with highest number of reviews).

# In[12]:


print('Expected length: ', len(android) - 1181)


# > The following is an example to test the  `not in`  operator

# In[13]:


print('z' in ['a','b','c'])
print('z' not in ['a','b','c'])


# > yet another example:

# In[14]:


name_and_reviews = {'Instagram': 66577313, 'Facebook': 78158306}
print('LinkedIn' not in name_and_reviews)
print('Instagram' not in name_and_reviews)


# > NOW TO START THE EXERCISE:

# In[15]:


print(android_header)


# In[16]:


reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max:
        reviews_max[name] = n_reviews
    


# In[17]:


print(len(reviews_max))


# In[18]:


print(reviews_max['Instagram'])


# - now to remove the duplicate entries:

# In[19]:


android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if n_reviews == reviews_max[name] and name not in already_added:
        android_clean.append(app)
        already_added.append(name)


# In[20]:


explore_data(android_clean,0,3,True)


# --- 

# # Detecting English characters
# 
# Now to check if the apps are developed in English

# In[21]:


print(ios[813][1])
print(ios[6731][1])
print('\n')
print(android_clean[4412][0])
print(android_clean[7940][0])


# In[22]:


print(ord('a'))
print(ord('爱'))


# > The numbers corresponding to the characters commonly used in an English text are all in the range of 0 to 127
# If the number is qual to or less than 127, then teh character belongs to the set o common English characters

# In[23]:


def is_english(string):
    for char in string:
        if ord(char) > 127:
            return False
    return True


# In[24]:


print(is_english('Instagram'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))


# In[25]:


print(ord('😜'))


# > Now to correct the function to identified charaters like `😜` and `™`
# 

# In[26]:


print(ord('😜'))
print(ord('™'))


# > Editing the function created above

# In[27]:


def is_english(string):
    count = 0
    for char in string:
        if ord(char) > 127:
            count += 1
        if count > 3:
            return False
    return True


# In[28]:


print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))


# In[29]:


print(android_clean[0])


# In[30]:


print(ios[0])


# In[31]:


android_eng = []
ios_eng = []

for app in android_clean:
    if is_english(app[0]):
        android_eng.append(app)
        
for app in ios:
    if is_english(app[1]):
        ios_eng.append(app)


# In[32]:


explore_data(android_eng,0,3,True)
print('\n')
explore_data(ios_eng,0,3,True)


# # Isolating free apps

# In[33]:


print(android_header)
print('\n')
print(ios_header)


# In[34]:


android_free = []
ios_free = []

for app in android_eng:
    if app[7] == '0':
        android_free.append(app)
        
for app in ios_eng:
    if app[4] == '0.0':
        ios_free.append(app)
        


# In[35]:


explore_data(android_free,0,2,True)
print('\n')
explore_data(ios_free,0,2,True)


# # Validation Strategy
# 
# 1. build a minimal Android version of the app, and add it to Google Play
# 2. if the app has good responde from users, we develop it further
# 3. if the app is profitable after six months, we build an iOS version fo the app and add it to the App Store.
# 
# It is necessary to find the app profile that is succsessful on both markets.
# To achieve this, I will build a frequency table 

# > - one function to generate frequency tables that show percentages
# - another function to display the percentages in descending order

# to sort hte lists/dictionaries/... the function `sorted()` will be used.
# 
# ex:

# In[36]:


a_list = [50, 20, 100]
print(sorted(a_list))
print(sorted(a_list, reverse = True))


# In[37]:


freq_table = {'Genre_1': 50, 'Genre_3': 20, 'Genre_2': 100}
sorted(freq_table)


# In[38]:


freq_table = {'Genre_1': 50, 'Genre_3': 20, 'Genre_2': 100}
freq_table_as_tuple = [(50, 'Genre_1'), (20, 'Genre_3'), (100, 'Genre_2')]
sorted(freq_table_as_tuple)


# > Starting with the `freq_table()` function

# In[39]:


def freq_table(dataset, index):
    freq = {}
    total = 0
    
    for app in dataset:
        col = app[index]
        if col in freq:
            freq[col] += 1
        else:
            freq[col] = 1
        total += 1
    
    freq_percent = {}
    for key in freq:        
        freq_percent[key] = (freq[key] / total) * 100
            
    return freq_percent

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key],key)
        table_display.append(key_val_as_tuple)
    
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])

            
                


# In[40]:


print(android_header)
print('\n')
print(ios_header)


# In[41]:


display_table(ios_free, -5) #Genre (iOS)


# In[42]:


display_table(android_free, -4) #Genre (Android)


# In[43]:


display_table(android_free, 1) #Category (Android)


# # Analysis
# 
# > - most common genre on android: tools and enternainment
# - most common catergory on android: family and game
# - most common genre on iOS: games and entertainment
# 
# Education is also a common genre. On android there are several categories for education, maybe they can be set as a single one on iOS the majority is games and entertainment. On android the number of genres is more varied, although there could be too many similar ones. The category may be a better indicator of the most commons genres on android

# # Finding the most popular genres
# 
# - Android: use the number of installations `Installs`
# - iOS: use the number of user ratings as proxy `rating_count_tot`
# 
# > - isolate the apps of each genre
# - sum up the number user ratings for the apps of that genre
# - divide the sum by the number of apps belonging to that genre (not by the total number of apps)

# In[44]:


some_strings = ['FIRST', 'SECOND']
some_integers = [1, 2, 3, 4, 5]

for string in some_strings:
    print(string)
    for integer in some_integers:
        print(integer)


# In[45]:


genre_ios = freq_table(ios_free, -5) #column prime_genre

for genre in genre_ios:
    total = 0 #store the sum of user ratings specific for each genre
    len_genre = 0 #store the number of apps specific for each genre
    
    for app in ios_free: #nested loop        
        genre_app = app[-5]
        if genre_app == genre:
            total += float(app[5]) #app[5] corresondes do the user rating
            len_genre += 1
    avg_usr_rating = total / len_genre
    print(genre, ':', avg_usr_rating)
    


# In[46]:


genre_ios = freq_table(ios_free, -5) #column prime_genre
print(genre_ios['Social Networking'])


# In[47]:


print(ios_free[0])


# > Now to look at the number of installs for the Google Play market

# In[48]:


display_table(android_free, 5) # the Installs column 


# > It is necessary to remove the commas and the plus characters

# In[49]:


n_installs = '100,000+'
print(n_installs.replace('+', 'plus'))
print(n_installs.replace('1', 'one'))
print(n_installs.replace('&', 'ampersand')) # no change


# In[50]:


n_installs = '100,000+'
print(n_installs.replace('+',''))


# In[51]:


n_installs = '100,000+'
n_installs = n_installs.replace('+','')
print(n_installs)
n_installs = n_installs.replace(',','')
print(n_installs)


# In[57]:


cat_android = freq_table(android_free, 1)

for category in cat_android:
    total = 0
    len_category = 0
    
    for app in android_free:
        if app[1] == category: #checks if the genre is the same
            n_installs = app[5] #gets the humber of installations for the given genre
            n_installs = n_installs.replace('+','')
            n_installs = n_installs.replace(',','')
            total += float(n_installs)
            len_genre += 1
    avg_installs = total / len_genre
    print(category, ':', avg_installs)
    
            


# In[53]:


print(cat_android)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




