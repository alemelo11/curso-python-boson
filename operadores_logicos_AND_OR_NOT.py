# Operadores Lógicos em Python
# Também chamados de operadores booleanos, pois implementam a lógica booleana.
# Trabalham com os valores True e False.
# Permitem avaliar o resultado de dois operandos e retornar um valor booleano.
# Principais operadores:
# - AND: retorna True se ambos os operandos forem True.
# - OR: retorna True se pelo menos um dos operandos for True.
# - NOT: inverte o valor booleano, ou seja, transforma True em False e vice-versa.

# Tabela de Verdade do Operador Lógico AND
# O operador AND retorna True apenas quando ambas as condições são True.
# Veja os possíveis resultados:
# Condição A | Condição B | Resultado
#    False   |    False   |  False
#    True    |    False   |  False
#    False   |    True    |  False
#    True    |    True    |  True

# Tabela de Verdade do Operador Lógico OR
# O operador OR retorna True se pelo menos uma das condições for True.
# Veja os possíveis resultados:
# Condição A | Condição B | Resultado
#    False   |    False   |  False
#    True    |    False   |  True
#    False   |    True    |  True
#    True    |    True    |  True

# Tabela de Verdade do Operador Lógico NOT
# O operador NOT inverte o valor lógico da condição.
# Veja os possíveis resultados:
# Condição | Resultado
#   True   |  False
#   False  |  True

# idade = 15
# altura = 1.75

# resultado = (idade >= 18) and (altura >= 1.70)
# msg = "Pode participar do evento? " + str(resultado)
# print(msg)  

##############################################################################

# OR: programa de disparo de alarme
# porta = 'a'
# janela = 'f'

# alarme = (porta == 'a') or (janela == 'a')
# msg = "Alarme disparado? " + str(alarme)
# print(msg)

##############################################################################

# NOT: Verificação de acesso
usuario_autenticado = False # Usuário não autenticado

acesso_permitido = not usuario_autenticado
msg = "Acesso permitido? " + str(acesso_permitido) + "\n"
print(msg)

##############################################################################

have_money = False

msg2 = "Pode comprar? " + str( not have_money)
print(msg2)
