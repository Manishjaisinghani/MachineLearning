import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
# print (tips.head())
################################################
#Dist plot
################################################
# sns.distplot(tips['total_bill'])
################################################
#Joint plot
################################################
# sns.jointplot(x='total_bill',y='tip',data=tips) # kinds can be kde, reg, hex. default = scatter
################################################
#Pair plot
################################################
# sns.pairplot(tips) # a hue parameter can be added that should be categorical, pallete parameter is used to change colors
################################################
#Rug plot
################################################
# sns.rugplot(tips['total_bill'])
# sns.plt.show()
################################################
#categorical plot
################################################
# sns.barplot(x = 'sex',y='total_bill',data=tips)
################################################
#count plot
################################################
# sns.countplot(x='sex',data = tips)
################################################
#box plot or quartile representation
################################################
# sns.boxplot(x='day',y='total_bill',data =tips,hue ='smoker')
################################################
#Violinplot
################################################
# sns.violinplot(x='day',y='total_bill',data=tips) #also has option to include hue and split = true to split the data
################################################
#strip plot
################################################
# sns.stripplot(x='day',y='total_bill',data=tips)#add jitter=True to seperate the points by assing some noise points,hue can also be added as an option
################################################
#swarm plot(combination of violin and strip plot)
################################################
# sns.swarmplot(x='day',y='total_bill',data=tips)
################################################
#create any plot by using below, just change the kind
################################################
# sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')
################################################
#Matrix plots or heat maps
################################################
flights = sns.load_dataset('flights')
tc = tips.corr()
# sns.heatmap(tc)#annotation as annot = True, cmap option can also be specifid
fp = flights.pivot_table(index='month',columns ='year',values ='passengers')
# sns.heatmap(fp,cmap='magma',linecolor='white',linewidth=1)
################################################
#cluster map(hierarchical clustering)
################################################
# sns.clustermap(fp,cmap='coolwarm',standard_scale=1)# standard_scale option to normalize the data
################################################
#Regression plots
################################################
# sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v']) #can change markers type by using option markers=['o','v'], size of markers can be changed by scatter_kws={'s':100}
# sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',aspect =0.6,size=4)
################################################
#Iris dataset
################################################
iris = sns.load_dataset('iris')
# sns.pairplot(iris)
# g = sns.PairGrid(iris)
# g.map(plt.scatter)
# g.map_diag(sns.distplot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot)
################################################
#facet grid
################################################
# g = sns.FacetGrid(data=tips, col='time',row='smoker')
# g.map(sns.distplot,'total_bill')#x axis represents total bill, rows = yes or no for smokers, left and right columns represent lunch and dinner
# g.map(plt.scatter, 'total_bill',tip) #plot types that need more than one arguments


################################################
#Style and color
################################################
# sns.set_style('white') #White background
# sns.set_style('ticks') #ticks on axes
# sns.set_style('darkgrid') #ticks on axes
# sns.set_style('whitegrid') #ticks on axes
# sns.despine() #Removes top and left spine
# sns.despine(left = True,bottom =True) #Removes all the spines
# sns.set_context('poster',font_scale=3)  #increases size of the figure
# sns.countplot(x='sex',data=tips)

################################################
# palletes and color
################################################
# sns.lmplot(x='total_bill',y='tip',data=tips,pallete='coolwarm')

################################################
# exercise
################################################
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
# sns.jointplot(x='fare',y='age',data=titanic)
# sns.distplot(titanic['fare'],kde=False,color='pink')
# sns.boxplot(x='class',y='age',data=titanic)
# sns.violinplot(x='class',y='age',data=titanic)
# sns.countplot(x='sex',data=titanic)
# tc1 = titanic.corr()
# sns.heatmap(tc1)
# print (tc1)

g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')


sns.plt.show()
