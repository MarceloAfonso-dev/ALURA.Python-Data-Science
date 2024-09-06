t1 = t2 = True
f1 = f2 = False

if t1 and f1:
    print("expressão verdadeira")
else:
    print("expressão falsa")

if t1 or f1:
    print("expressão verdadeira")
else:
    print("expressão falsa")

if not f1:
    print("expressão verdadeira")
else:
    print("expressão falsa")

lista = 'Mariana, João, Carla, José'
nome_1 = 'Mariana'
if nome_1 in lista:
    print(f'{nome_1} está na lista')
else:
    print(f'{nome_1} não está na lista')