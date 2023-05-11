''' aprendendo pandas '''
import pandas as pd
import matplotlib.pyplot as plt


def pproperts(df: pd.DataFrame, n: int = 5):
    print('-' * 80, '\nTamanho:', df.shape, '\n', df.sample(n))


df1 = pd.read_excel('Aracaju.xlsx')
df2 = pd.read_excel('Fortaleza.xlsx')
df3 = pd.read_excel('Natal.xlsx')
df4 = pd.read_excel('Recife.xlsx')
df5 = pd.read_excel('Salvador.xlsx')

df = pd.concat([df1, df2, df3, df4, df5])
df['Data'] = pd.to_datetime(df['Data'])  # se tivesse como int
print(df.dtypes)

df['Receita'] = df['Vendas'].mul(df['Qtde'])
# <class 'pandas.core.series.Series'>
ds2 = df.groupby(df['Data'].dt.year)['Receita'].sum()
df2 = ds2.to_frame().reset_index().sort_values('Receita')
print('-' * 80, '\nTamanho:', ds2.shape, '\n')
print(df2)
ds2.plot.pie()  # grafico de PIZZA
plt.title('RECEITA por ANO')
# plt.show()
plt.savefig('01_grf_pizza.png')
plt.clf()

df['Ano'], df['mes'], df['dia'] = (df['Data'].dt.year,
                                   df['Data'].dt.month,
                                   df['Data'].dt.day)
pproperts(df)

# <class 'pandas.core.series.Series'>
ds2 = df.groupby('Cidade')['Receita'].sum()
df2 = ds2.to_frame().reset_index().sort_values('Receita')

'''Links que deram a letra
https://allwin-raju-12.medium.com/plotting-graphs-using-python-and-matplotlib-bcb8c721a520
https://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html
https://ourcodingclub.github.io/tutorials/pandas-python-intro/
https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
'''
# grafico de BARRAS
df2.plot.bar(x='Cidade', y='Receita', title='RECEITA por CIDADE', color='red')
# plt.show()
plt.savefig('02_grf_barra.png')
plt.clf()

pproperts(df['Cidade'].value_counts())

df['Cidade'].value_counts().plot.bar()
plt.title('Total de Vendas por CIDADE')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')
plt.style.use('ggplot')
# plt.show()
plt.savefig('03_grf_barras_default.png')
plt.clf()

df['Cidade'].value_counts().plot(marker='o')
plt.title('Total de Vendas por CIDADE')
plt.xlabel('Cidade')
plt.ylabel('Total de Vendas')
plt.style.use('ggplot')
# plt.show()
plt.savefig('04_grf_linhas.png')
plt.clf()

# histograma da quantidade de produtos
plt.hist(df['Qtde'])
# plt.show()
plt.savefig('05_grf_histograma.png')
plt.clf()

# dispersao entre dia da venda e receita
plt.scatter(x=df['dia'], y=df['Receita'])
# plt.show()
plt.savefig('06_grf_dispersao.png')
plt.clf()
