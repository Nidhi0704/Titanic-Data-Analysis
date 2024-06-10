#!/usr/bin/env python
# coding: utf-8

# # DATA  SCIENCE :-
# 
#                                      TRACE CODE :DS

# #  TASK - 2
# 
#                                                                                               PREPARAED BY :-
#                                                                                                NIDHI SHARMA

# ## Problem Statement:-  
#                                
#                                  Perform the data cleaning and Explorartory Data Analysis[EDA] on a dataset, explore the      relationship between the variables and identify patterns and trends in the data...

# ## Process has to be done:-
# 
# -- Loading the dataset
# 
# -- Understanding the dataset.
# 
# -- Claen the dataset.
# 
# -- Perform the Exploratory Data Analysis [EDA]
# 
# -- Identifying the patterns.
# 
# -- Draw the conclusions..

# # Importing the libraries:- 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_excel(r"C:\Users\Lenovo\Downloads\train2.xlsx")


# ## Understanding  the  datasets :-

# In[3]:


data.head()


# In[4]:


data.tail()


# In[60]:


data.sample(3)


# # Conclusion :-
# 
# ### The data is not biased...

# In[6]:


data.size


# In[7]:


data.shape


# In[8]:


data.isnull().sum()


# In[9]:


data.duplicated().sum()


# In[10]:


data.info()


# ## Data cleaning process :-

# ## Changing the data types:-

# In[19]:


data["Sex"] = data["Sex"].astype("category")
data["Ticket"] = data["Ticket"].astype("category")
data["Embarked"] = data["Embarked"].astype("category")
data["PassengerId"] = data["PassengerId"].astype("int16")
data["SibSp"] = data["SibSp"].astype("int16")
data["Parch"] = data["Parch"].astype("int16")
data["Fare"] = data["Fare"].astype("float32")
data["Survived"] = data["Survived"].astype("float16")
data["Name"] = data["Name"].astype("category")
data["Age"] = data["Age"].astype("int")


# ## Fill the missing values:-

# In[13]:


data["Embarked"].mode()


# In[14]:


data["Embarked"].fillna("S", inplace=True)


# In[15]:


data["Age"].mean()


# In[16]:


data["Age"].fillna("29", inplace=True)


# ## Drop the cabin column :- 

# In[17]:


data.drop(columns = ["Cabin"], inplace = True)


# In[20]:


data.info()


# ## Now, the data is cleaned and having no null values 
# 
# ## Ready to visualize :-

# # Identifying the columns :- categorical or numerical :-

# ## Categorical  Columns :-
# 
# --> Survived
# 
# --> PClass
# 
# --> Sex
# 
# --> SibSp
# 
# --> Parch
# 
# --> Embarked
# 
# ## Numerical Columns :-
# 
# --> Age
# 
# --> Fare
# 
# --> PassengerId
# 
# ## Mixed Columns :-
# 
# --> Name
# 
# --> Ticket
# 
# --> Cabin

# # Exploratory Data Analysis :-

# # Univariate Variable Analysis :-

# ## Categorical columns :- 

# In[21]:


## SURVIVED COLUMN :- 

sns.countplot(data["Survived"])

death_percent = round((data["Survived"].value_counts().values[0]/891)*100)
print("the death percent {} %".format(death_percent))


# In[22]:


## PCLASS COLUMN :-

sns.countplot(data["Pclass"])

travel_most = round((data["Pclass"].value_counts()/891)*100)
print(travel_most)


# In[23]:


## SEX COLUMN :- 

sns.countplot(data["Sex"])

per = round((data["Sex"].value_counts()/891)*100)
print(per)


# In[24]:


## SibSp COLUMN :-

sns.countplot(data["SibSp"])

pecent = round((data["SibSp"].value_counts()/891)*100)
print(pecent)


# In[26]:


### PARCH COLUMN :-

sns.countplot(data["Parch"])

percent_parch = round((data["Parch"].value_counts()/891)*100)
print(percent_parch)


# In[27]:


## EMBARKED COLUMN :-

sns.countplot(data["Embarked"])

embar_percent = round((data["Embarked"].value_counts()/891)*100)
print(embar_percent)


# ## Numerical columns:-  

# In[29]:


## AGE COLUMN :-

sns.distplot(data["Age"])

print("Skewness :- " , data["Age"].skew())
print("Kurtos :- " , data["Age"].kurt())


# In[56]:


sns.boxplot(data["Age"])


# In[61]:


print("The age between the 55 to 65 ", data[(data["Age"] >55) & (data["Age"]<65)].shape[0])
print("The age between the 65 to 70 ", data[(data["Age"] >65) & (data["Age"]<70)].shape[0])
print("The age between the 70 to 80 ", data[(data["Age"] >70) & (data["Age"]<80)].shape[0])


# ### The data is treated as Normal Distribution.
# 
# ### The data has much more outliers.

# In[47]:


## Fare COLUMN :- 

sns.distplot(data["Fare"])


# In[62]:


print(data["Fare"].skew())

print(data["Fare"].kurt())


# ### The data is right-skewed.
# 
# ### the data has outliers..

# In[45]:


sns.boxplot(data["Fare"])


# In[71]:


print("People with fare in between $200 and $300  :- ", data[(data["Fare"]>200) & (data["Fare"]<300)].shape[0])
print("People with fare in between $300 and $400  :- ", data[(data["Fare"]>300) & (data["Fare"]<400)].shape[0])
print("People with fare in between $400 and $500  :- ", data[(data["Fare"]>400) & (data["Fare"]<500)].shape[0])
print("People with fare greater than $500  :- ", data[data["Fare"]>500].shape[0])


# # Bivariate Analysis :-

# ## Categorical - Numerical columns :-

# In[27]:


plt.figure(figsize = (7,15))
plt.subplots_adjust()

plt.subplot(2,1,1)
sns.barplot(data["Sex"], data["Survived"], ci=False)

plt.subplot(2,1,2)
sns.barplot(data["Embarked"], data["Survived"], ci=False)


# In[31]:


## PCLASS WITH EMBARKED AND SEX:-

plt.figure(figsize=(7,12))
plt.subplots_adjust()

plt.subplot(2,1,1)
sns.barplot(data["Sex"], data["Pclass"], ci=False)

plt.subplot(2,1,2)
sns.barplot(data["Embarked"], data["Pclass"], ci=False)


# In[37]:


plt.figure(figsize=(7,15))
plt.subplots_adjust()

plt.subplot(2,1,1)
sns.barplot(data["Sex"], data["Fare"], ci=False)

plt.subplot(2,1,2)
sns.barplot(data["Embarked"], data["Fare"], ci=False)


# # Numerical - Numerical analysis :-

# In[49]:


## Survived with Pclass :-

sns.countplot(data["Survived"], hue=data["Pclass"])

pd.crosstab(data["Survived"], data["Pclass"]).apply(lambda r : round((r/r.sum())*100,1),axis=1)


# In[54]:


## Survived with Sex :-

sns.countplot(data["Survived"], hue=data["Sex"])

pd.crosstab(data["Survived"], data["Sex"]).apply(lambda r : round((r/r.sum())*100,1),axis=1)


# In[55]:


## Survived with age :-

plt.figure(figsize=(15,7))
sns.distplot(data[data["Survived"]==0]["Age"])
sns.distplot(data[data["Survived"]==1]["Age"])


# In[56]:


## Survived with Fare:-

plt.figure(figsize=(15,7))
sns.distplot(data[data["Survived"]==0]["Fare"])
sns.distplot(data[data["Survived"]==1]["Fare"])


# # Multivariate Analysis :- 

# In[57]:


sns.pairplot(data)


# In[59]:


sns.heatmap(data.corr())


# In[61]:


data.corr()


# # Conclusion :-
# 
# --> 62% PEOPLE WERE DEAD.
# 
# --> 3rd class(55%) > 2nd class > 1st class -- people 's travel
# 
# --> most people travelled alone(78%) as well as start their journey from Southampton(73%)
# 
# --> mostly the 25-40 age people travel in titanic.
# 
# --> mostly the people pay less than $100
# 
# --> Mostly the females and Cherboug people survived more
# 
# --> Mostly the Males and Queenstown people travelled in 3rd class.
# 
# --> Most of the fare were paid by the Females and chebourg people.
# 
# --> Mostly 1st class people were survived the most..
# 
# --> The 20 -30 years people were died most and the people who pay less than $50 were died the most..

# 
# 
# 
# ## THANK YOU !!!
#  BY:- NIDHI SHARMA
