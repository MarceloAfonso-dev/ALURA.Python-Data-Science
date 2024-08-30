texto = '  Geovana Alessandra dias Sanyos '

print(texto.upper()) #lower() para minúsculas

print(texto.strip()) #Retira espaços em branco

print(texto.replace('y','t')) #Substitui caracteres

texto = texto.strip().replace('y','t').upper()
print(texto)