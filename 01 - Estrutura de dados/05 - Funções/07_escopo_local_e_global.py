salario = 2000


def salario_bonus(bonus,lista):
    lista.append(2) #isso altera a lista tanto internamente quanto externa
    lista_aux=lista.copy()
    lista_aux.append(3)
    print(lista_aux)
    global salario
    salario += bonus
    return salario

lista=[1] # como a lista eh um objeto mutavel deve tomar o cuidado ao altera-la na funcao
print(lista)
salario_bonus(500,lista)  # 2500
print(salario)  # 2500
print(lista)

def funcao(*args, **kw):
    print(args)
    print(kw)

funcao("python", 2022, curso="dio")