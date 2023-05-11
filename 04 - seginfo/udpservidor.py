'''servidor UDP'''
import sys
import time
import socket
from general import timeit


@timeit
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(f'Falha na conexão\nError: {e}')
        sys.exit()
    print("socket criado com sucesso")

    host = 'localhost'
    porta = 5432
    mensagem = '\nserver: OLAAAAAAAAAAAAAAAAAA'
    s.bind((host, porta))

    chat = True
    while chat:
        dados, end = s.recvfrom(4096)
        if dados == b'sair':
            s.sendto(dados + ('\nserver: ok, saio já!'.encode()), end)
            print('server: Saindo em 5 segundos')
            time.sleep(5)
            chat = False
        elif dados:
            print('server: Enviando mensagem')
            s.sendto(dados + (mensagem.encode()), end)
    s.close()


if __name__ == '__main__':
    main()
