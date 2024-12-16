i = 1
lista = ['Ricardo Vieira', 'Marcelo Afonso']

while i < len(lista):
    print(f'Olá {lista[i]}')
    salario = float(input('Digite o seu salário: R$'))

    if salario <= 1000:
        print('Você é zoado')
    elif salario > 1000 and salario <= 5000:
        print('Você é normal')
    else:
        print('Você é rico')
    i += 1

print(f'E além disso, você ganha R$ {12*salario:.2f}')