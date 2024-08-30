texto = '  Geovana Alessandra dias Sanyos '

print(texto.upper()) #lower() para minúsculas

print(texto.strip()) #Retira espaços em branco

print(texto.replace('y','t')) #Substitui caracteres

texto = texto.strip().replace('y','t').upper()
print(texto)

print(chr(64)) #Retorna o caractere correspondente ao código ASCII

print(ord('A')) #Retorna o código ASCII do caractere

print(chr(79) + chr(108) + chr(225)) #Concatenação de caracteres