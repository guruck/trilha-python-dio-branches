'''Treinamento a PEP 8
    Comentario sempre iniciar com letra maiuscula
'''
from typing import List

CONSTANTE_MAX = 100  # Constantes sempre em caixa alta


class JuridicPerson:  # Nomes de classes não sepeara com underscore _
    '''Classe comeca com letras maiusculas
        Comentario sempre iniciar com letra maiuscula
    '''
    def __init__(self, message: str) -> None:
        '''inicializado da classe'''
        self._message = message

    def return_arguments(self, arg_one,
                         arg_two, arg_three, arg_four) -> List():
        '''essa funcao retorna os argumentos no formato de lista'''
        # Apenas metodos, parametros e variaveis divide com underscore
        variavel_one = self._message
        return List(variavel_one, arg_one, arg_two, arg_three, arg_four)

    def segunda_funcao(self) -> None:
        '''apenas para adequar a PEP8'''


def print_hi(name: str) -> None:
    '''Essa é a "Docstring" do metodo print_hi (pep257). Este metodo tem por
    objetivo exibir um nome na tela com a devida saudacao "Hi".

    Keyword arguments:
    name -- um nome qualquer do tipo string
    '''
    print(f'Hi, {name}!')


def variables():
    '''nao sei por que raios o flake acusa a variavel como constante'''
    # Variavel sempre em caixa baixa, se necessario serapada por underscore
    number_string = 2  # Para comentar 2 espacos
    if number_string == 2:
        number_string = 'atribuicao deve ter espaco antes e depois'


if __name__ == '__main__':
    print_hi('PyCharm')  # apontando o mouse sobre a funcao exibe a Docstring
