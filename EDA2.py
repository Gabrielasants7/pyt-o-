#!/usr/bin/env python
# coding: utf-8

# # Automation (EDA), with the Sweetviz Library¶

#                   Homicide rate, suicide rate and GDP
#  The Dataset is composed of ten columns, namely: country/region
# 
# 
# country	, iso3c, iso2c, year,	Intentional homicides (per 100,000 people)	,Suicide mortality rate (per 100,000 population),  GDP (current US$) GDP per capita, PPP (current international $)	, adminregion ,	incomeLevel .
# 
# 
# 
# Data source:https://data.worldbank.org/
# 

# # importing modules and loading the dataset
# 

# In[3]:


import pandas as pd
import plotly.express as px
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import sweetviz as sv
df_suicide= pd.read_csv("C:/Users/Marztec Tecnologia/Downloads/suicide homicide gdp.csv")
df_suicide.head()


#  # viewing the last rows of the dataset
# 

# In[5]:


df_suicide.tail()


# # Automating exploratory data analysis (EDA)

# In[38]:


my_report = sv.analyze(df_suicide)
my_report.show_notebook()


# # What are the ten countries with the highest homicide rates?

# In[12]:


df_mean_country =  df_suicide.groupby(["country","iso3c","incomeLevel"])["Intentional homicides (per 100,000 people)"].mean().reset_index()
top_ten_hom = df_mean_country.sort_values("Intentional homicides (per 100,000 people)", ascending=False).head(10)
top_ten_hom


# # graphically view the top ten countries with the highest homicide rates

# In[16]:


import matplotlib.pyplot as plt
plt.figure(figsize=(16,8), dpi=200)
plt.xticks(rotation=45, fontsize=14)
plt.ylabel("Suicide mortality rate", fontsize=16, weight = "bold")
plt.title("Top 10 countries with Homicides per 100,000 people", fontname="Impact", fontsize=25)
sns.barplot(data = top_ten_hom, y= "Intentional homicides (per 100,000 people)", x = "country", hue="incomeLevel", 
            dodge=False)
plt.legend(fontsize=14, title="Income Level")


# # What are the ten countries with the highest suicide rates?

# In[18]:


df_mean_country =  df_suicide.groupby(["country","iso3c", "incomeLevel"])["Suicide mortality rate (per 100,000 population)"].mean().reset_index()
top_ten_sui = df_mean_country.sort_values("Suicide mortality rate (per 100,000 population)", ascending=False).head(10)
top_ten_sui


# # graphically view the top ten countries with the highest suicide rates

# In[19]:


plt.figure(figsize=(16,8), dpi=200)
plt.xticks(rotation=45, fontsize=14)
plt.ylabel("Suicide mortality rate", fontsize=16, weight = "bold")
plt.title("Top 10 countries with suicide mortality rate", fontname="Impact", fontsize=25)
sns.barplot(data =top_ten_sui, y = "Suicide mortality rate (per 100,000 population)", 
            x ="country", hue="incomeLevel", dodge=False, palette="tab10")
plt.legend(fontsize=14, title="Income Level")


# # interactive data visualization using the plotly library

# In[31]:


df_homicides = df_suicide.copy()
df_homicides = df_homicides.dropna(subset=['Intentional homicides (per 100,000 people)'])
df_homicides.rename( columns={ 'Intentional homicides (per 100,000 people)' : 'IH' } ,inplace=True)
fig = px.choropleth(df_homicides, locations='iso3c', color='IH',
                           color_continuous_scale="Reds", hover_data = ['country', 'IH'],
                    projection = 'miller',
                            animation_frame="year",
                           range_color=(0, 12),
                    title = 'Suicide mortality rate')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# In[32]:


Admin_Ih = df_homicides.groupby(["year", "adminregion"])["IH"].mean().reset_index()


# In[33]:


fig = px.bar(Admin_Ih, x='IH', y='adminregion',
             title='Mean intentional homicides over the year',animation_frame="year", color = 'adminregion', text_auto='.2s')
fig.update_layout(showlegend=False)
fig.show()


# # In short : There is a clear negative connection between GDP per capita and homicides, and GDP per capita and suicides. That is to say the smaller the GDP per capita for a country, the more likely is that a citizen of that country will commit homicide or suicide. This connection is stronger for GDP per capita and homicides.

# In[ ]:




