'''cliente UDP'''
import sys
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

    host_alvo = 'localhost'
    porta_alvo = 5432
    mensagem = 'Ola servidor'

    try:
        s.sendto(mensagem.encode(), (host_alvo, porta_alvo))
        dados, servidor = s.recvfrom(4096)
        dados = dados.decode()
        print(f'Cliente: {dados}')
        s.sendto('sair'.encode(), (host_alvo, porta_alvo))
        dados, servidor = s.recvfrom(4096)
        dados = dados.decode()
        print(f'Cliente: {dados}')
    except socket.error as er:
        print(f'Falha na conexão\nError: {er}')
        sys.exit()
    finally:
        print('Cliente: Finalizando a conexão')
        s.close()


if __name__ == '__main__':
    main()
