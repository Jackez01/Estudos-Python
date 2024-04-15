print("\nFor utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("\nFor utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "João", "idade": 30, "Cidade": "São Paulo"}
print("\nFor usando dicionários - chaves")
for chave in pessoa.keys():
   print(chave)
  
print("\nFor usando dicionários - valores")
for valor in pessoa.values():
   print(valor)

print("\nFor usando dicionários - items")
for chave, valor in pessoa.items():
   print(f"{chave}: {valor}")

# Range(): intervalo númerico
# [0,1,2,3,4,5,6,7,8,9]
print("\nUtilizando a função range()")
print(list(range(0, 10)))

for numero in range(5):
   print("Número:", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
   if indice == 3: 
      lista[indice] = 5
print(lista)

# enumerate()
print("\nUtilizando a função enumerate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
       print("indice 1")
