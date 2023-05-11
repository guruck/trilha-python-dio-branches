''' aprendendo pandas '''
import pandas as pd
import matplotlib.pyplot as plt


def pproperts(df: pd.DataFrame, n: int = 5, msg=''):
    rows = n if n < len(df) else len(df)
    print('-' * 80, '\nTamanho:', df.shape, f'{msg}\n', df.sample(rows))


# configuracao de ponto flutuante
pd.options.display.float_format = '{:15,.2f}'.format


df = pd.read_excel('AdventureWorks.xlsx')
pproperts(df, msg='---AdventureWorks.xlsx---')
print('Tipo de dados da Tabela:')
print(df.dtypes)
print('\nVerificando nulos:')
print(df.isnull().sum())
print('-' * 80)

# Qual foi a Receita Total?
print(f"Receita Total: {df['Valor Venda'].sum():18,.2f}")

# Qual foi o Custo Total?
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])
print(f"Custo Total  : {df['Custo'].sum():18,.2f}")

# Qual foi o Lucro Total?
df['Lucro'] = df['Valor Venda'] - df['Custo']
print(f"Lucro Total  : {df['Lucro'].sum():18,.2f}")

# Qual tempo que demorou para encaminhar o Produto?
df['Tempo_envio'] = (df['Data Envio'] - df['Data Venda']).dt.days
# print(df['Tempo_envio'].dtype)  # int64

# Qual tempo medio por Marca que demorou para encaminhar o Produto?
ds = df.groupby('Marca')['Tempo_envio'].mean()
print('-' * 80, '\nTamanho:', ds.shape,
      ': Tempo Medio por Marca:\n', ds)

# Qual Lucro obtido por Ano e Marca?
df_ano = df.groupby([df['Data Venda'].dt.year,
                    'Marca'])['Lucro'].sum().reset_index()
pproperts(df_ano, 10, ': Lucro obtido por Ano e Marca:')

# Qual TOTAL de produtos vendidos?
ds = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
pproperts(ds.reset_index(), msg=': TOTAL de produtos vendidos: ')

# grafico de BARRAS HORIZONTAL
ds.reset_index().plot(kind='barh', x='Produto', y='Quantidade',
                           title='TOTAL de produtos vendidos')
plt.style.use('ggplot')
# plt.show()
plt.savefig('01_grfAW_barra_horizontal.png')
plt.clf()

# Qual Lucro obtido por ano?
ds = df.groupby(df['Data Venda'].dt.year)['Lucro'].sum()
pproperts(ds.reset_index(), msg=': Lucro obtido por ano: ')
# grafico de BARRAS
ds.plot.bar(title='TOTAL de produtos vendidos')
plt.xlabel('Ano')
plt.ylabel('Lucro (Milhões)')
# plt.show()
plt.savefig('02_grfAW_barra.png')
plt.clf()

# Quais vendas do ano 2009?
df_2009 = df[df['Data Venda'].dt.year == 2009]
pproperts(df_2009)

# Qual Lucro obtido em 2009 por mes?
ds = df_2009.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum()
pproperts(ds.reset_index(), msg=': Lucro obtido por mês 2009: ')
# grafico de Linhas
ds.plot(title='Lucro obtido por mês 2009')
plt.xlabel('Mes')
plt.ylabel('Lucro')
# plt.show()
plt.savefig('03_grfAW_linha.png')
plt.clf()

# Qual Lucro obtido por  Marca?
df_lucro = df_2009.groupby('Marca')['Lucro'].sum()
pproperts(df_lucro.reset_index(), 10, ': Lucro obtido por Marca:')
# grafico de BARRAS
df_lucro.plot.bar(title='Lucro obtido por Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro (Milhões)')
plt.xticks(rotation='horizontal')
# plt.show()
plt.savefig('04_grfAW_barra.png')
plt.clf()

# Qual Lucro obtido por  Classe?
df_lucro = df_2009.groupby('Classe')['Lucro'].sum()
pproperts(df_lucro.reset_index(), 10, ': Lucro obtido por Classe:')
# grafico de BARRAS
df_lucro.plot.bar(title='Lucro obtido por Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro (Milhões)')
plt.xticks(rotation='horizontal')
# plt.show()
plt.savefig('05_grfAW_barra.png')
plt.clf()

pproperts(df['Tempo_envio'].describe(), 10, ': Desvios de Tempo Envio:')
plt.boxplot(df['Tempo_envio'])
# plt.show()
plt.savefig('06_grfAW_boxplot.png')
plt.clf()

# histograma da quantidade de produtos
plt.hist(df['Tempo_envio'])
# plt.show()
plt.savefig('07_grfAW_histograma.png')
plt.clf()

print('Tempo de envio Maximo: ', df['Tempo_envio'].max())
print('Tempo de envio Minimo Receita: ', df['Tempo_envio'].min())
print('TOP5 maiores', df.nlargest(5, 'Tempo_envio')[['Data Venda',
                                                     'Data Envio',
                                                     'Tempo_envio',
                                                     'ID Loja',
                                                     'ID Produto']])
print('TOP5 menores', df.nsmallest(5, 'Tempo_envio')[['Data Venda',
                                                      'Data Envio',
                                                      'Tempo_envio',
                                                      'ID Loja',
                                                      'ID Produto']])

df.to_csv('df_vendas_novo.csv', index=False, sep=';')
