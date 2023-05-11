'''cliente TCP'''
import sys
import socket
from general import timeit


@timeit
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f'Falha na conexão\nError: {e}')
        sys.exit()
    print("socket criado com sucesso")

    host_alvo = input('Forneca o host ou IP a ser conectado: ')
    porta_alvo = input('Forneca a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Conexão efetuada com sucesso")
        s.shutdown(2)
    except socket.error as er:
        print(f'Falha na conexão\nError: {er}')
        sys.exit()


if __name__ == '__main__':
    main()
