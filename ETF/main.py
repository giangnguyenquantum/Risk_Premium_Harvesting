import pandas as pd

commondities_pd=pd.read_csv('commondities.csv')
print('list of suitable commondities ETFs:')
print(commondities_pd)

bonds_pd=pd.read_csv('bonds.csv')
print('list of suitable bonds ETFs:')
print(bonds_pd)

real_estate_pd=pd.read_csv('real_estate.csv')
print('list of suitable real estate ETFs:')
print(real_estate_pd)

equities_pd=pd.read_csv('equities.csv')
print('list of suitable equities ETFs:')
print(equities_pd)
