''' aprendendo pandas '''
import pandas as pd


df1 = pd.read_excel('Aracaju.xlsx')
df2 = pd.read_excel('Fortaleza.xlsx')
df3 = pd.read_excel('Natal.xlsx')
df4 = pd.read_excel('Recife.xlsx')
df5 = pd.read_excel('Salvador.xlsx')

df = pd.concat([df1, df2, df3, df4, df5])

print('-' * 80, '\nSHAPES\n')
print('Aracaju: ', df1.shape)
print('Fortaleza: ', df2.shape)
print('Natal: ', df3.shape)
print('Recife: ', df4.shape)
print('Salvador: ', df5.shape)
print('TOTAL: ', df.shape)

print('-' * 80, '\n', df.sample(5))
print('-' * 80, '\n', df.dtypes)

df2 = df.copy()
df2['LojaID'] = df2['LojaID'].astype('object')
print('-' * 80, '\nALTERANDO TIPO de LojaID\n', df2.dtypes)
print('-' * 80, '\n', df.isnull().sum())  # verificando nulos

# substituir nulos pela media em MEMORIA
df['Vendas'].fillna(df['Vendas'].mean(), implace=True)
# substituir nulos por 0 em MEMORIA
df['Vendas'].fillna(0, implace=True)
# apagando linhas com valores nulos
df.dropna(implace=True)
# apagando linhas com valores nulos baseado na coluna Vendas
df.dropna(subset=['Vendas'], implace=True)
# apagando linhas com valores nulos em TODAS as colunas simultaneo
df.dropna(how='all', implace=True)
