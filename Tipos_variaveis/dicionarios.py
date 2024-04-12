#criando um dicionario
pessoa = {"nome" : "João", "idade" : 30, "cidade" : "São Paulo"}

print("Meu dicionário de exemplo:", pessoa)

# Acessando os valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Atribuir valores ao dicionario
pessoa["sobrenome"] = "Silva"
print("sobrenome:", pessoa["sobrenome"])
print ("Meu dicionário de exemplo:", pessoa)

# Removendo um par de chave-valor
del pessoa["sobrenome"]
print ("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Values() também podemos transforma-lo para lista, como exemplificado acima, para acessar os valores individualmente
valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valordo dicionário:", valores[0])

# Items() (mostra a chave e valor de cada item do dicionário transformando eles em tuplas)
itens = list(pessoa.items())
print("Pares chave-valor do dicionário", itens)
print("primeiro valor:", itens[0] [1])
print("primeira chave-valor: %s = %s" % (itens[0] [0],itens[0] [1]))

