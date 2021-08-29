import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.tail())

# hoe gaan we om met NaN-data?
# uitzoeken
print(ufo.notnull().tail())

#zoek naar steden die missen
print(ufo[ufo.City.isnull()])

#laat een rij vallen wanneer tenminste één van de waarden mist
ufo.dropna(how='any')

#laat een rij vallen wanneer in elke cel van een rij
#NaN staat
ufo.dropna(how='all')

#check kolommen waarbij ik check op drop
ufo.dropna(subset=['City', 'Shape Reported'], how='any')

#value counts
print(ufo['Shape Reported'].value_counts())

#Missing values veranderen in een bepaalde waarde
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
print(ufo['Shape Reported'].value_counts(dropna=False))

#Selecteren van rijen 0 tot 2 en alle kolommen
print(ufo.loc[0:2, :])

#Selecteren van alle rijen en een beperkt aantal kolommen
print(ufo.loc[:, ['City', 'Time']])

#iloc statement
print(ufo.iloc[:, 0:2])

print(ufo.iloc[0:3, :])

#dummys aanmaken
train = pd.read_csv('http://bit.ly/kaggletrain')
print(train)
print(train.head())

x = pd.get_dummies(train.Sex)
print(x)

#samenvoegen
y = pd.concat([train, x], axis=1)
print(y.head())

#duplicaten verwijderen
user_cols = ['user_id', 'age', 'gender', 'occupation',
             'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|',
                      header=None, names=user_cols,
                      index_col='user_id')
print(users.head())

z = users.drop_duplicates(keep='first')
print(z.head())
