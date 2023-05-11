'''exemplo de multiThread'''
import time
from threading import Thread
from random import uniform


def carro(velocidade: float, piloto: str):
    '''carro '''
    trajeto = 0

    while trajeto <= 100:
        status = f'{piloto} em {trajeto:.2f} km vel: {velocidade:.2f} km/h'
        dado = uniform(-1, 2)
        trajeto += velocidade
        velocidade += dado
        if dado > 0:
            print(f'{status} aceleraaaa {dado:.2f}')
        elif dado < 0:
            print(f'{status} parando... {dado:.2f}')
        else:
            print(f'{status} conservou!')

        if velocidade < 0:
            velocidade = 0.5
        time.sleep(0.1)
    print(f'{piloto} CHEGOU !!!!')


t_carro1 = Thread(target=carro, args=[2.5, 'Zelão'])
t_carro2 = Thread(target=carro, args=[2.5, 'Jonas'])

t_carro2.start()
t_carro1.start()
