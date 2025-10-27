# Operadores de comparação são usados para comparar valores e retornar um resultado booleano (True ou False).
# Abaixo está uma tabela com os operadores de comparação e suas respectivas operações:

# == : Igual a - Verifica se dois valores são iguais.
# != : Diferente de - Verifica se dois valores são diferentes.
# >  : Maior que - Verifica se o valor à esquerda é maior que o valor à direita.
# <  : Menor que - Verifica se o valor à esquerda é menor que o valor à direita.
# >= : Maior ou igual a - Verifica se o valor à esquerda é maior ou igual ao valor à direita.
# <= : Menor ou igual a - Verifica se o valor à esquerda é menor ou igual ao valor à direita.

# Exemplo de uso:
# a = 10
# b = 20

# print(a == b)  # Retorna False, pois 10 não é igual a 20.
# print(a != b)  # Retorna True, pois 10 é diferente de 20.
# print(a > b)   # Retorna False, pois 10 não é maior que 20.
# print(a < b)   # Retorna True, pois 10 é menor que 20.
# print(a >= b)  # Retorna False, pois 10 não é maior ou igual a 20.
# print(a <= b)  # Retorna True, pois 10 é menor ou igual a 20.
# print(b != a + 10)  # Retorna False, pois 20 é igual a 10 + 10.

x = y = z = False
n1 = n2 = 0

n1 = int((input("Digiteo um número: ")))
n2 = int((input("Digiteo outro número: ")))

x = n1 == n2
print("São iguais? ", x, '\n') # conctenando com \n para pular linha (juntar partes de str)

z = n1 > n2
print("n1 é maior que n2? ", z,)
print(n1, 'é maior que', n2,'?', z, '\n') # outra forma de concatenar


y = n1 != n2
print("São diferentes? " +  str(y)) # + é operador de concatenação; convertendo boolean em str com str()

