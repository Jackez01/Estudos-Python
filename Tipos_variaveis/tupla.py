minha_tupla = (1, 2, 2, 6, 8, 9)

print("minha tupla:", minha_tupla)

print(minha_tupla[0])

#usando o -1 podemos acessar op ultimo elemento da tupla
print(minha_tupla[-1])

#metodo count (para saber a quantidade de vezes que um elemento aparece)
contagem = minha_tupla.count(2)
print("Quantidade de x que o elementos 2 aparece: ", contagem)

#Index (para saber em qual lugar da tupla o elemento está)
indice = minha_tupla.index(8)
print("O elemento 8 está na posição:", indice)