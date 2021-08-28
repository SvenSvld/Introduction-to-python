#package data analysis
import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)


#importeer data
movies = pd.read_csv('http://bit.ly/imdbratings')

#check eerste vijf rijen
print(movies.head())

#check beschrijvende statistieken
print(movies.describe())

#check aantal rijen, kolommen
print(movies.shape)

#check datatype == dataframe
print(movies.dtypes)

#check datatype == dataframe
print(type(movies))

#alleen waarden met die geen string zijn
print(movies.describe(include =['object']))

#kolommen hernoemen van star-rating > naar 'aantal_sterren', en 'title' > 'titel'
movies.rename(columns= {'star_rating': 'aantal_sterren',
                        'title': 'titel'}, inplace=True)
print(movies.columns)

#alle namen van de kolommen in één keer doen
movies_colmns = ['aantal sterren', 'naam film', 'content rating', 'type genre', 'lengte', 'actors list']
movies.columns = movies_colmns
print(movies.columns)

#alle namen van de kolommen met een spatie veranderen met een _ teken
movies.columns = movies.columns.str.replace(' ', '_')
print(movies.columns)

#verwijderen van één kolom
movies.drop('aantal_sterren', axis=1, inplace=True)
print(movies.columns)

#verwijderen van twee of meer kolommen
movies.drop(['naam_film', 'content_rating'], axis=1, inplace=True)
print(movies.columns)

#verwijderen van rijen (in dit geval 1 tot/en 2)
print(movies)
movies.drop([1,2], axis=0, inplace=True)
print(movies)

#sorteren van de data by lengte
print(movies.sort_values('type_genre'))
#sorteren met behoud...
movies.sort_values('type_genre', inplace=True)
print(movies)

#filteren van dataset waarbij alleen cases met tenminste een lengte van 200 kunnen worden waargenomen
#met behoud van de oude dataset
filter = movies.lengte >= 200
print(movies[filter])
print(movies)
#zonder behoud van de oude dataset
filter = movies.lengte >= 200
movies = movies[filter]
print(movies)


#Inladen vliegdata
df = pd.read_csv("https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv", usecols=range(1,17))
print(df)

#Select flights details of JetBlue Airways uit month == 1 en dest == IAH
newdf = df[(df.month == 1) & (df.dest == 'IAH')]
print(newdf)

#Select flights details of JetBlue Airways uit month == 1, month == 3 en dest == IAH
newdf_1 = df[(df.month >= 1) & (df.month <= 3) & (df.dest == 'IAH')]
print(newdf_1)

#group_by variable
print(df)
print(df.groupby('dest').dep_delay.agg(['count', 'min', 'max', 'mean']))
print(df.groupby('dest').dep_delay.mean())
