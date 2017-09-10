import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('/Users/manish/Documents/UniversityofMissouri/Udemy/DataScience/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Visualization/Pandas Built-in Data Viz/df1',index_col=0)
# print (df1.head())
df2 = pd.read_csv('/Users/manish/Documents/UniversityofMissouri/Udemy/DataScience/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Visualization/Pandas Built-in Data Viz/df2')
# print (df2.head())
# df1['A'].hist()
# df1['A'].plot(kind ='hist', bins =30)
# df2.plot.area(alpha =0.4)
# df2.plot.bar(stacked=True)
# df1.plot.line(x=df1.index,y='B')
# df1.plot.scatter(x='A',y='B',c='C')
# df1.plot.scatter(x='A',y='B',s=df1['C']*100) # modify the size of points
# df2.plot.box() # Box plot
# df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
# df.plot.hexbin(x='a',y='b',gridsize =25)
# df2['a'].plot.kde() # kernal density plot
# df2.plot.kde()  # kernal density plot for entire dataframe
################################################
#Exercise
################################################
df3 = pd.read_csv('/Users/manish/Documents/UniversityofMissouri/Udemy/DataScience/Python-Data-Science-and-Machine-Learning-Bootcamp/Python-for-Data-Visualization/Pandas Built-in Data Viz/df3')
# df3.plot.scatter(x='a',y='b',figsize=(12,3))
# plt.style.use('ggplot')
# df3['a'].hist(bins=20)
# df3[['a','b']].plot.box()
# df2['d'].plot.kde(ls='--')
df3.ix[0:30].plot.area()
plt.legend(loc='center left', bbox_to_anchor=(1,.5))
plt.show()
