'''modulo para efetuar pings'''
import os
import time
from .general import timeit


@timeit
def main():
    '''principal'''
    with open('hosts.txt', encoding='utf-8') as file:
        dump = file.read()
        dump = dump.splitlines()

        for ip in dump:
            print('-' * 80, f'\npingando em {ip}')
            os.system(f'ping -n 2 {ip}')
            time.sleep(2)
    print('-' * 80)


if __name__ == '__main__':
    main()
