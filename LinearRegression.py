import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/manish/Documents/UniversityofMissouri/Udemy/DataScience/Python-Data-Science-and-Machine-Learning-Bootcamp/Machine Learning Sections/Linear-Regression/USA_Housing.csv')
# print (df.head())

# sns.pairplot(df)
# sns.distplot(df['Price'])
# sns.heatmap(df.corr(),annot = True)
# plt.tight_layout()
# plt.show()

print(df.columns)

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
Y = df['Price']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,Y,train_size = .4,random_state = 101)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train,y_train)

print(lm.intercept_)

lm.coef_

X_train.columns

cdf = pd.DataFrame(lm.coef_,X.columns,columns = ['coeff'])

print (cdf)

predictions = lm.predict(X_test)

# plt.scatter(y_test,predictions)
# sns.distplot((y_test-predictions))

from sklearn import metrics

metrics.mean_absolute_error(y_test,predictions)
metrics.mean_squared_error(y_test,predictions)
np.sqrt(metrics.mean_squared_error(y_test,predictions))
plt.show()
