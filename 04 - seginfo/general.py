'''modulo para funcoes gerais'''
import functools
import time
import random
import string
import hashlib
import itertools
from typing import List


def timeit(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value

    return wrapper_timer


def gerador_senha(tamanho_senha: int, numero_de_senhas: int = 1) -> List:
    '''gerador de senha'''
    if tamanho_senha <= 0 or numero_de_senhas <= 0:
        return []
    chrs = string.ascii_letters + string.digits + '#$%&*'
    chrs2 = string.ascii_uppercase + string.digits + '#$%&*'
    chrs3 = string.ascii_lowercase + string.digits + '#$%&*'
    chrs4 = string.digits + '#$%&*'
    chrs5 = string.ascii_letters + '#$%&*'
    chrs0 = string.ascii_lowercase + string.digits
    rndm = random.SystemRandom()
    secrets = []
    for _q in range(numero_de_senhas):
        senha = ''
        for i in range(tamanho_senha):
            if senha == '':
                senha += rndm.choice(chrs)
            elif senha[-1] in string.ascii_lowercase:
                senha += rndm.choice(chrs2)
            elif senha[-1] in string.ascii_uppercase:
                senha += rndm.choice(chrs3)
            elif senha[-1] in string.digits:
                senha += rndm.choice(chrs5)
            elif i % 5 == 0:
                senha += rndm.choice(chrs4)
            else:
                senha += rndm.choice(chrs0)

        secrets.append(senha)
    return secrets


def hash_comparator(arquivo0: str, arquivo1: str) -> bool:
    '''comparacao simples'''
    # hash0 = hashlib.new('ripemd160')
    # hash0.update(open(arquivo0, 'rb').read())

    # hash1 = hashlib.new('ripemd160')
    # hash1.update(open(arquivo1, 'rb').read())

    hash0 = hashlib.sha256(open(arquivo0, 'rb').read())
    hash1 = hashlib.sha256(open(arquivo1, 'rb').read())
    print(hash0.hexdigest(), '=>', hash1.hexdigest())

    return hash0.digest() == hash1.digest()


def gerador_hashs(valor: str, tipo: str = 'sha256') -> str:
    '''gera uma string do tipo hash com valor recebido

    Arguments:
        valor: string para calculo hash
        tipo: algoritmo que fara o calculo do hash, default 'sha256'
        suportados 'md5';'sha1';'sha256','sha512'
    '''
    if valor.strip() == '' or valor is None:
        return 'Valor invalido ou nao fornecido'

    if tipo == 'md5':
        return hashlib.md5(valor.encode('utf-8')).hexdigest()
    elif tipo == 'sha1':
        return hashlib.sha1(valor.encode('utf-8')).hexdigest()
    elif tipo == 'sha256':
        return hashlib.sha256(valor.encode('utf-8')).hexdigest()
    elif tipo == 'sha512':
        return hashlib.sha512(valor.encode('utf-8')).hexdigest()
    else:
        return f'Tipo {tipo} ainda nao suportado'


def gerador_word_list(valor: str, quantidade: int = 1) -> List:
    '''permutacoes?? '''
    retorno = []
    resultado = itertools.permutations(valor, quantidade)
    for i in resultado:
        # print(''.join(i))
        retorno.append(i)
    return retorno


# print(gerador_senha(8), gerador_senha(8, 10))
# print(hash_comparator('udpclient.py', 'udpservidor.py'))
# print(hash_comparator('udpclient.py', 'udpclient.py'))
# print(gerador_hashs('teste'))
# print(gerador_word_list('teste', 2))
