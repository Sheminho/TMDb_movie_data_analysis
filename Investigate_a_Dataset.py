#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset - [Database_TMDb_movie_data]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > I have selected the **Database_TMDb_movie_data** to investigate it and explore the correlations between the varies things on it like the popularity and the budget, if the budget bigger is that mean that the popularity will be big, is the profit is an indecator for the popularity of the movie and is there a corelation between the popularity and votes and who are the top rated directors and actors and so on
# 
# 
# #### Question(s) for Analysis
# <ul>
# <li>First question after importing and wrangling the data is what is the profit of every film to use it to find the correlations in the coming questions and you will see it <a href="#Q1">here</a></li>
# <li>Also it is important for me to know the most popular and top rated directors and actors and you will find it <a href="#Q2">here</a> and <a href="#Q5">here</a></li>
# <li>Finally it is important to know the difference between the film production before the 2000s and after 2000s in some questions like <a href="#Q3">here</a></li> and <a href="#Q4">here</a></li>
# </ul>

# ### importing Liberaries and DataFrame
# >This section is to import the necessary liberaries and DataFrame

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('Database_TMDb_movie_data/tmdb-movies.csv')


# <a id='wrangling'></a>
# ## Data Wrangling section
# > In this section we will do some gathering, assessing and cleaning to the data to be more suatable and easy to analyse

# In[3]:


df.shape


# Now we know that the data has more than 10K observations and 21 column.
# 
# Lets look at the first 5 observations.

# In[4]:


df.head()


# lets take look at the columns names and data types and the number of the missing data on each one

# In[5]:


df.info()


# 
# ### Data Cleaning
# > After gathering the data seems that we have a many missing data on the 'tagline', 'homepage','Keywords' and 'production_companies' columns and we will not use them on our investigation so lets drop then

# In[6]:


df.drop(['homepage', 'tagline', 'keywords', 'production_companies'], axis=1, inplace=True)


# Now we can drop all Null values from the dataframe

# In[7]:


df.dropna(inplace=True)


# Finally for cleaning the data let's take look at the number of duplicated values and drop them

# In[8]:


df.duplicated().sum()


# In[9]:


df.drop_duplicates(inplace=True)


# In[22]:


df.info()


# Now we have cleaned data without missing or duplicated values and ready to be explored

# <a id='eda'></a>
# ## Exploring Data Section
# > After wrangling the data, In this section we will answer some questions by analysing the data to create some Conclusions about the dataframe.
# > All these questions is from my deep mind and of course you may have different questions so don't be restricted by this questions.
# 
# <a id='Q1'></a>
# #### Q1: What is the profit for every film?

# In[11]:


#Creating new column named 'profit' equals the difference between the budget and the revenue of every film
df['profit'] = df['revenue'] - df['budget']


# In[12]:


df.head(13)


# Now we have a profit column for each film

# In[14]:


df[df['revenue']==df['revenue'].max()]['original_title']


# The name of the film with the biggest revenue ever is **Avatar**

# #### Q3: What is the film with the biggest budget in a 2007?

# In[15]:


df[df['budget'] == df[df['release_year'] == 2007]['budget'].max()]


# The film with the biggest budget in a 2007 was **Pirates of the Caribbean: At World's End** with budget 300M $

# #### Q4: what is the correlation between the budget and the popularity?
# *i.e. is the film with bigger budget means that it have bigger popularity?*

# In[16]:


df[['budget','popularity']].corr()


# Now let's figure it out as plot but before that let's create a function to do our plot quickly.

# In[17]:


def sctr_plt(df, X, Y):
    plt.scatter(x = df[X], y = df[Y], s = 5)
    plt.title('correlation between {} & {}'.format(X,Y).title(), fontsize = 15)
    plt.xlabel(X.title(), fontsize = 15)
    plt.ylabel(Y.title(), fontsize = 15)


# In[18]:


sctr_plt(df, 'budget', 'popularity')


# Seems it does have weak correlation so if a film have big budget it has small chance to has big popularity.

# <a id = 'Q5'></a>
# #### Q5: what is the top rated action movie?
# That want some works on it because we have the genres colomn as string so we have to create a fuction to extract the wanted word from a given string.

# ## That is a function to avoid repetitive code.
# #### and it's used twice, the first one in this question and the second one on Q7

# In[40]:


def cont(word ,string):
    if word in string.lower():
        return True
    else:
        return False


# Then create new dataframe and stor the dataframe after selecting the action word fron the genre.

# In[41]:


df1 = df[df['genres'].apply(lambda x: cont('action',x))]


# Finally we select the movie/s with the maximum vote.

# In[42]:


df1[df1['vote_average'] == df1['vote_average'].max()]


# We have two films **The Dark Knight** in 2008 and **Kill Bill: The Whole Bloody Affair** in 2011 with the same rating **8.1**.

# #### Q6: What is the number of films that was directed by Robert Schwentke?
# Here we can use the query() method to select all films that directed by Robert Schwentke.

# In[43]:


df.query('director == "Robert Schwentke"').count()[0]


# #### Q7: What is the active years of the actor vin diesel?
# Here we can use the lambda function to use the function that we have created in <a href = '#Q5'>Q5</a> to find the films with the actor in its cast.

# In[44]:


df[df['cast'].apply(lambda x: cont('vin diesel',x))]['release_year'].value_counts().sort_index()


# #### Q8: What is the top rated movie in 70s?
# We can use the query method to select films with release year between 1970 and 1980

# In[45]:


df2 = df.query('release_year >= 1970' and 'release_year < 1980')
df2[df2['vote_average'] == df2['vote_average'].max()]


# The top rated movie in 70s is *The Godfather* with *8.3* average votes and was released in *1972*

# <a id = 'Q2'></a>
# #### Q9: Who is the most popular director?
# Here we can use the groupby() method to group the data frame by the directors name then selects the director with the biggest summation of popularity.

# In[46]:


dfmax = df.groupby('director').sum()
dfmax[dfmax['popularity'] == dfmax['popularity'].max()]


# Christopher Nolan is the most popular director with summation of popularity equals almost 62.

# #### Q10: What is the correlation between the popularity and the profit?

# In[47]:


df[['profit','popularity']].corr()


# In[48]:


sctr_plt(df, 'profit', 'popularity')


# Seems it has a bit strong correlation.

# #### Q11: What is the correlation between the popularity and votes?

# In[49]:


df[['vote_average','popularity']].corr()


# In[50]:


sctr_plt(df, 'vote_average', 'popularity')


# The corelation is very weak.

# #### Q12: State a diagram between the revenue from 2015 until now
# First we will create an temporary df and store the summation of the revenue on each year on it

# In[51]:


df_temp = df.query('release_year >= 2010')[['revenue', 'release_year']].groupby('release_year').sum()
df_temp


# Then state the histogram based on the temporary df

# In[53]:


years = ['2010', '2011', '2012', '2013', '2014', '2015']
plt.bar(years, df_temp['revenue'])
plt.title('The revenues from 2015 until now', fontsize = 15)
plt.xlabel('Years', fontsize = 15)
plt.ylabel('Total Revenue', fontsize = 15)


# <a id = 'Q3'></a>
# #### Q13: What is the profit difference before 2000 and after 2000?

# In[54]:


df.query('release_year >= 2000')['profit'].sum() - df.query('release_year < 2000')['profit'].sum()


# <a id = 'Q4'></a>
# #### Q14: What is the difference in movies length before 2000s and after 2000s?

# In[55]:


mean_af = df.query('release_year >= 2000')['runtime'].mean()
mean_be = df.query('release_year < 2000')['runtime'].mean()
print('The average of movies length before 2000s was {} \nThe average of movies length after 2000s is {}'.format(mean_be, mean_af))


# Seems that the movies has been limited after 2000s by about 6.5 minutes.

# <a id='conclusions'></a>
# ## Conclusions
# > **After investigating the data frame we knew the following:**
#     <ul>
#         <li>The correlation between the budget and the popularity is 0.54 means if the budget is high that does mean that the movie has chance to be popular.</li>
#         <li>The voting results does not return the popularity, because the correlation between them is weak 0.2</li>
#         <li>The correlation between the profit and the popularity is a bit strong 0.62 means that the profit shows the popularity.</li>
#         <li>**Avatar** movie makes the biggest revenue ever with 2.7 Billion Dollars.</li>
#         <li>**The Dark Knight** has the highest voting rate as action movie.</li>
#         <li>**Robert Schwentke** has directed 5 movies.</li>
#         <li>**vin diesel** was active every year from 1999 until 2015 except 2007, 2010 and 2012.</li>
#         <li>**The Godfather** is the top rated movie in 70s with 8.3 vote rating.</li>
#         <li>**Christopher Nolan** is the most popular director ever.</li>
#         <li>movies revenue had a drop in 2014 but returns stronger in 2015.</li>
#         <li>the movies profits has increases after 2000s by about **14M $**.</li>
#         <li>the movies has limited its length by about **6.8** minutes.</li>
#     </ul>
# > ### DataFrame limitations
# - Of course there's some limitations on this data frame that limited our investigate like the missing data in the production companies column, If this column was clear of missing data we would uses it to investigate more and more in the data frame.
# - Also the big amount of 0 values in the budget and revenue columns also affected on our results but generally i think we did great job on this data frame under these limitations.
