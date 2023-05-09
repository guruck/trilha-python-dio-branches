''' aprendendo pandas '''
import pandas as pd

# , error_bad_lines=False (não existe ???)
df = pd.read_csv('de_para.csv', delimiter=';')
df = df.rename(columns={'depois': 'FABRICANTE'})

print(df.shape, '\n', df)
print('-' * 80, '\n', df.columns)
print('-' * 80, '\n', df.dtypes)
print('-' * 80, '\n', df.describe())
print('-' * 80, '\n', df['FABRICANTE'].unique())

cisco = df.loc[df['FABRICANTE'] == 'Cisco']
print('-' * 80, '\n', cisco)

print('-' * 80, '\n', df.groupby('campo')['FABRICANTE'].unique())  # groups
print('-' * 80, '\n', df.groupby('campo')['FABRICANTE'].nunique())  # count
print('-' * 80, '\n', df.groupby('campo')['qtd'].mean())  # media da quantidade
print('-' * 80, '\n', df.groupby('campo')['qtd'].sum())  # soma da quantidade
print('-' * 80, '\n', df['qtd'].sum())  # soma da quantidade total
