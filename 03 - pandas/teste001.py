'''arquivo para testar a biblioteca Pandas e suas funcionalidades
'''
import re
import pandas as pd
import numpy as np
# from pathlib import Path


LINHAS = 13

series = pd.Series([7, 4, 2, np.nan, 6, 9])
# print(series)
datas = pd.date_range('20180101', periods=LINHAS, freq='D')
# print(datas)
# print(np.random.randn(LINHAS, 5))
df = pd.DataFrame(np.random.randn(LINHAS, 5),
                  index=datas, columns=list('ABCDE'))


def avaliar(valor: float) -> float:
    '''funcao para retornar um determinado valor quando existente'''
    # print(valor, type(valor))
    if valor is None:
        return 0.00
    return float(valor) * 10


def normalize_cisco(vendor: str) -> str:
    '''normaliza do dados do fabricante Cisco'''
    vendor = str(vendor).lower()
    if 'cisco' in vendor:
        return 'Cisco'
    return vendor


def normalize_vendor(vendor: str, de_para: dict) -> str:
    '''normalizacao para qualquer campo vendor de um Dataframe'''
    # print (f'keys: {de_para.keys()} ,val: {de_para.values()}')
    for key in de_para.keys():
        # print (f'key: {key} ,val: {de_para[key]}')
        vendor = str(vendor).lower()
        if key in vendor:
            return de_para[key]
    return vendor


def normalize(campo: str, de_para: pd.DataFrame, default: str = None) -> str:
    '''normalizacao generica para qualquer campo de um Dataframe'''
    for _, value in de_para.iterrows():
        # print (f'key: {key} ,val: {value.tipo}')
        campo = str(campo).lower()
        if value.tipo == 'association':
            if value.antes in campo:
                return value.depois
        elif value.tipo == 'regexp':
            if re.search(value.antes, campo):
                return value.depois
    return campo if default is None else default


def print_normalized(campo: str, de_para: pd.DataFrame, default: str = None):
    '''printa resultado normalizado'''
    print(campo, normalize(campo, de_para, default), sep=' => ')


df['calculo'] = df['E'].apply(avaliar)

fabricantes = ['cisco', 'F5', 'cisco Network', 'juniper Systems',
               'cisco Systems', 'f5', 'cisco', 'f5 Systems', '3Com',
               'cisco Network', 'Juniper', 'cisco Systems', 'Hp'
               ]
# df2 = pd.DataFrame(fabricantes, index=datas, columns=['FABRICANTE'])
frame = pd.DataFrame(pd.Series(fabricantes), columns=['FABRICANTE'])
# dados = {'cisco':'Cisco','juniper':'Juniper','f5':'F5','3com':'3COM',
# 'hp':'Hewlett-Packer'}
df_dados = pd.read_csv('de_para.csv', delimiter=';')
# df_dados = df_dados.query("campo == 'FABRICANTE'")
df_fabricante = df_dados.query("campo == 'FABRICANTE'")[['antes',
                                                         'depois', 'tipo']]
# print(f'\df_dados:\n{df_fabricante}')
# print_normalized('cisco sistemas',df_fabricante)
# df_modelo = df_dados.query("campo == 'MODELO'")[['antes','depois','tipo']]
# print(f'\df_dados:\n{df_modelo}')
# print_normalized('ACS 4300',df_modelo)
# print_normalized('ACS 4300',df_modelo,'')
# print_normalized('banana air-ct bananinha',df_modelo)
# print_normalized('40236 air-ct',df_modelo)
# print_normalized('402wlc023',df_modelo)

# dados = dict(df_dados.values)
# print(f'\nteste:\n{dados}')
# normalize_vendor('vendor',dados)
dados = {'cisco': 'Cisco', 'juniper': 'Juniper', 'f5': 'F5',
         '3com': '3COM', 'hp': 'Hewlett-Packer'}
frame['FABRICANTE_ANTES'] = frame['FABRICANTE']
# frame['FABRICANTE'] = frame['FABRICANTE'].apply(
# normalize_vendor, de_para=dados)
frame['FABRICANTE'] = frame['FABRICANTE'].apply(normalize,
                                                de_para=df_fabricante)
frame['STATUS'] = ['INSTALADO', 'EM CONFIGURACAO', 'INSTALADO', 'INSTALADO',
                   'INSTALADO', 'INSTALADO', 'EM CONFIGURACAO', 'INSTALADO',
                   'INSTALADO', 'INSTALADO', 'INSTALADO', 'EM CONFIGURACAO',
                   'INSTALADO']
frame['STATUS_OPERACIONAL'] = ['OPERACIONAL', 'EM MANUTENCAO', 'OPERACIONAL',
                               'EM MANUTENCAO', 'OPERACIONAL', 'OPERACIONAL',
                               'OPERACIONAL', 'OPERACIONAL', 'OPERACIONAL',
                               'EM MANUTENCAO', 'OPERACIONAL', 'OPERACIONAL',
                               'OPERACIONAL']
frame['ARQUITETURA'] = ['TELECOM', 'TELECOM', 'TELECOM', 'TELECOM', 'TELECOM',
                        'TELECOM', 'TELECOM', 'TELECOM', 'TELECOM', 'TELECOM',
                        'TELECOM', 'TELECOM', 'IBBA']
frame['ENDERECO_IP'] = ['0.0.0.0', '204.66.143.202', '237.208.50.217',
                        '243.119.181.168', '47.80.195.18', '193.21.124.206',
                        '158.175.184.48', '229.50.34.230', '146.55.148.72',
                        '21.22.45.162', '216.132.25.102', '107.47.152.34',
                        '0.0.0.0']
frame['GRUPO_SUPORTE'] = 'Operacao Telecom'

print(f'passo1:\n{frame}\n')

frame = frame.query(
    "STATUS == 'INSTALADO' & "
    "STATUS_OPERACIONAL == 'OPERACIONAL' & "
    "ARQUITETURA == 'TELECOM' & "
    "ENDERECO_IP != '' & "
    "GRUPO_SUPORTE == 'Operacao Telecom'"
)

print(f'passo2:\n{frame}\n')

vendor_list = ['Cisco', 'Juniper', 'F5']
vendor_query = " | ".join(f"FABRICANTE == '{vendor}'"
                          for vendor in vendor_list)
frame = frame.query(vendor_query)

print(f'passo3:\n{frame}\n')
