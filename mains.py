import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
    
data = pd.read_csv('titanic-passengers.csv', sep=';')

print(data)
print(data.head())
print(data.columns)
print(data.shape)
print(data.describe())
data = data.dropna(axis = 0)
print(data.shape)
print(data.describe())
print(data['Age'].value_counts())
data['Age'].value_counts().plot.hist()
print(data.shape)


data[['Age','Sex']].value_counts().plot.hist()


def plot_correlation_map( df ):

    corr = df.corr()

    s , ax = plt.subplots( figsize =( 12 , 10 ) )

    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )

    s = sns.heatmap(

        corr, 

        cmap = cmap,

        square=True, 

        cbar_kws={ 'shrink' : .9 }, 

        ax=ax, 

        annot = True, 

        annot_kws = { 'fontsize' : 12 }

        )
    
plot_correlation_map( data )
    
    
data.groupby(['Pclass','Survived']).mean().plot.bar()
    
print(data.groupby(['Pclass','Survived']).mean())

data = data.drop(['Name'],axis = 1)
print(data.columns)

data = data.set_index('Name')
print(data.head())































