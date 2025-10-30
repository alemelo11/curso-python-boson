# Desvios condicionais em Python
# permitem ao programa **tomar decisões** com base em condições
#   lógicas avaliadas por expressões `if`.
#
#   Tipos principais de condicionais abordados:
#     1. Condicional simples     → utiliza apenas o `if`
#     2. Condicional composto    → utiliza `if` e `else`
#     3. Condicional encadeado   → utiliza `if`, `elif` e `else`
#     4. Condicional aninhado    → combina estruturas condicionais dentro de outras
#
#   O objetivo é compreender como essas estruturas funcionam e quando aplicá-las
#   de forma eficiente no fluxo de execução de um programa Python.

# Fluxogramas:
# losango → condição (teste lógico)
# seta   → fluxo de execução
# retângulo → ação (processamento)  
# oval → início/fim
# ---------------------------------------------------------------

# simples
n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))    
media = (n1 + n2) / 2

if media >= 7.0:
    print("Aluno aprovado!")
    print("Parabéns!")
elif media >= 5.0:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")
    
print(f'Aluno com média: {media:.1f}')

