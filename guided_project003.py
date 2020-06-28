#!/usr/bin/env python
# coding: utf-8

# # Guided Project 3
# 
# The aim of this project is to clean the data and analyze the Ebay Car Sales Data from *eBay Kleinanzeigen*. 

# > begin with importing the libraries

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


autos = pd.read_csv('autos.csv', encoding='Latin-1')


# In[3]:


autos


# In[4]:


autos.info()
autos.head()


# The dataset contains 20 columns with 5000 entries. 5 columns contain null values

# # Converting column names from camelcase to snakecase

# In[5]:


autos.columns


# - Updating the column names to be read in snakecase

# In[6]:


autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']


# In[7]:


autos.head()


# # Data Exploration

# Need to look for:
# - text columns where all or almost all values are the same, which can often be dropped as they don't have useful information for analysis
# - examples of numeric data stored as text which can be cleaned and converted
# 
# The following methods will be used:
# - `DataFrame.describe`(with `include=all` to get both categorical and numeric columns)
# - `Series.value_counts()`
# - `Series.head()`

# In[8]:


autos.describe(include='all')


# > `seller` and `offer_type` are candidates to be excluded: in 50k rows, the same value shows up 49999 times
# 
# > `num_photos` is a strange one since its value appears to be 0

# In[9]:


autos["num_photos"].value_counts()


# - removing the non-numeric characters from `price` and `odometer` columns;
# - converting to numeric dtype

# In[10]:


autos = autos.drop(["seller", "offer_type", "num_photos"], axis=1)


# In[11]:


autos["price"] = (autos["price"]
                  .str.replace("$", "")
                  .str.replace(",", "")
                  .astype(int)
                 )
autos["odometer"] = (autos["odometer"]
                   .str.replace("km", "")
                   .str.replace(",", "")
                   .astype(int)
                   )
                                    


# In[12]:


autos.head()


# In[13]:


autos.rename(columns={'odometer': 'odometer_km'}, inplace=True)


# # Explore odometer_km and price columns
# > `odometer_km` column

# In[14]:


print(autos["odometer_km"].unique().shape)
autos["odometer_km"].describe()


# In[15]:


autos["odometer_km"].value_counts().sort_index(ascending=True)


# In[16]:


autos["odometer_km"].head()


# > values on odometer_km seem fine (no outliear) therefore nothing will be removed

# In[17]:


print(autos["price"].unique().shape)
print(autos["price"].describe())


# In[18]:


autos["price"].value_counts().sort_index(ascending=True).head(20)


# There are 1421 entries with price=0, which is does not seem realistic. This could be a value to be taken out.

# In[19]:


autos["price"].value_counts().sort_index(ascending=False).head(20)


#  There are also several cars with a 1M USD price, which is highly unliked that these are realistic bids (could be input errors).

# In[20]:


autos[autos["price"] > 350000].shape


# Setting a limit of 350k there are 14 cars with prices above this threshold. These could be candidates to be removed.

# In[21]:


autos.loc[autos["price"].between(1,350000),"price"].describe()


# In[22]:


autos = autos[autos["price"].between(1,350000)]


# # Exploring the date columns

# In[23]:


autos.loc[:,['date_crawled', 'ad_created', 'last_seen']].head()


# In[24]:


(autos['date_crawled'].str[:10]
 .value_counts(normalize=True, dropna=False)
 .sort_index(ascending=True)
)


# In[25]:


(autos['ad_created'].str[:10]
 .value_counts(normalize=True, dropna=False)
 .sort_index(ascending=True)
)


# In[26]:


(autos['last_seen'].str[:10]
 .value_counts(normalize=True, dropna=False)
 .sort_index(ascending=True)
)


# The more recent dates show an higher percentage of viewers, this may be due to the listing still be open when the crawler that collected the data stopped.

# In[27]:


autos['registration_year'].describe()


# The max value and min value do not make sense, since there were no cars registered on the year 1000, and we haven't reached the year 9999 (doubt there will be any cars around, at least like those of today).

# # Cleaning the registration_year column
# - cars with registration year after 2016 are not valied since the data collection stopped in 2016
# - only registration years ranging 1900-2016 are considered valid

# To determine the percentage of cars that lie outside the proposed range:

# In[28]:


not_valid_pct = ((~autos['registration_year'].between(1900,2016)).sum()/autos.shape[0])*100
print("{:0.2f}% lie outside of the chosen range".format(not_valid_pct))


# In[29]:


autos = autos[autos["registration_year"].between(1900,2016)]
autos["registration_year"].describe()


# In[30]:


#autos["registration_year"].value_counts(normalize=True).sort_index(ascending=True).head(10)
autos["registration_year"].value_counts(normalize=True).head(10)


# # Exploring the brand column

# In[31]:


autos["brand"].value_counts(normalize=True).head(20)


# Going to use the brands with a representation >5%

# In[32]:


brands_count = autos["brand"].value_counts(normalize=True)
top_5_pct = brands_count[brands_count > 0.05].index


# In[33]:


brand_mean_price = {}

for b in top_5_pct:
    brand_name = autos[autos["brand"]==b]    
    brand_mean_price[b] = int(brand_name["price"].mean())
    
brand_mean_price


# As expected, Audi, Mercedes and BMW are the most expensive brands. Opel being the cheapest.

# # Exploring average milage
# - check the milage for the brans mentioned before
# - understand if the milage has any relation to the price when choosing the car.
# 
# Note: the most popular brand is Volkswagen. In terms of price, it lies in the middle range

# > Mean Mileage

# In[34]:


bmp_series = pd.Series(brand_mean_price)
pd.DataFrame(bmp_series, columns=["mean_price"])


# In[36]:


brand_mean_mileage = {}

for b in top_5_pct:
    brand_name = autos[autos["brand"]==b]
    brand_mean_mileage[b] = int(brand_name["odometer_km"].mean())
    


# In[39]:


mean_mileage = pd.Series(brand_mean_mileage)
mean_price = pd.Series(brand_mean_price)


# In[43]:


brand_info = pd.DataFrame(mean_mileage, columns=['mean_mileage'])
brand_info['mean_price'] = mean_price
brand_info


# It is not observed a link between the mileage and the price of the car. The mileage does not vary much.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




