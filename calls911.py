import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')
df.info()
print(df.head())

# BASIC QUESTIONS

# 1. What are the top 5 zipcodes for 911 calls?
top5zipcodes = df['zip'].value_counts().head(5)
print(top5zipcodes)


# 2.What are the top 5 townships (twp) for 911 calls?

top5townships = df['twp'].value_counts().head(5)
print(top5townships)



# 3. Take a look at the 'title' column, how many unique title codes are there?
uniqueTitles = df['title'].nunique()
print(uniqueTitles)


# CREATING NEW FEATURES
# In the titles column there are "Reasons/Departments" specified before
# the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom
# lambda expression to create a new column called "Reason" that contains
# this string value.nFor example, if the title column value is
# EMS: BACK PAINS/INJURY , the Reason column value would be EMS.

# 5. What is the most common Reason for a 911 call based off of this new column?
df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
mostReason = df['Reason'].value_counts().head()
print(mostReason)


# USING OF SEABORN
sns.countplot(x = 'Reason', data=df)
plt.title("911 Count Calls By Reason")
plt.show()

# 6. Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
dataTypes = df['timeStamp'].dtype
print(dataTypes)

# 7. Now that the timestamp column are actually DateTime objects,
# use .apply() to create 3 new columns called Hour, Month, and Day of Week.
# You will create these columns based off of the timeStamp column

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
print(df[['timeStamp','Hour','Month','Day of Week']].head())

# 8. Notice how the Day of Week is an integer 0-6. Use the .map()
# with this dictionary to map the actual string names to the day of the week:
# Now use seaborn to create a countplot of the Day of Week
# column with the hue based off of the Reason column.

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

sns.countplot(x='Day of Week',data=df, hue='Reason')
plt.legend(title='Reason', loc = 'best')  # μπορείς να αλλάξεις το loc
plt.show()

# 9. Now use seaborn to create a countplot of the Month
#column with the hue based off of the Reason column.
sns.countplot(x='Month',data=df, hue='Reason')
plt.legend(title='Reason', loc = 'best')  # μπορείς να αλλάξεις το loc
plt.show()

byMonth = df.groupby('Month').count()
print(byMonth.head())

# 10. Now create a simple plot off of the dataframe indicating the count of calls per month.
byMonth['lat'].plot()
plt.show()

# 11.  Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month.
# Keep in mind you may need to reset the index to a column.
sns.lmplot(x='Month', y= 'twp', data=byMonth.reset_index())
plt.show()


# 12. Create a new column called 'Date' that contains the date from the timeStamp column.
# You'll need to use apply along with the .date() method.
df['Date'] = df['timeStamp'].apply(lambda x: x.date())

# 13.Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
# byDate = df.groupby('Date').count()
# byDate['lat'].plot()
# plt.show()

# 14. Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
df[df['Reason'] == 'Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.show()

df[df['Reason'] == 'EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.show()

df[df['Reason'] == 'Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.show()

# CREATING HEATMAPS
# 15. Now let's move on to creating  heatmaps with seaborn and our data.
# We'll first need to restructure the dataframe so that the columns become
# the Hours and the Index becomes the Day of the Week.
dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()

# 16. Create HeatMap Using the new DataFrame
sns.heatmap(dayHour,cmap='viridis')
plt.show()

# 17. Create a clustermap using this DataFrame
sns.clustermap(dayHour, cmap='viridis')
plt.show()

# 18.  Now repeat these same plots and operations, for a DataFrame that shows the Month as the column.
dayMonth = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()
sns.heatmap(dayMonth,cmap='viridis')
plt.show()

sns.clustermap(dayMonth, cmap='viridis')
plt.show()