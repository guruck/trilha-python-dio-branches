'''desenvolvido com a bibioteca para mais baixo nivel'''
import ctypes


attr_hide = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('hosts.txt', attr_hide)
if retorno:
    print('sucesso')
else:
    print('falhou')
