
"""
=============================================================================
LAÇO DE REPETIÇÃO WHILE
=============================================================================

ESTRUTURAS DE CONTROLE DE REPETIÇÃO
- Usadas quando precisamos repetir blocos de comandos várias vezes
- Também chamados de Loops ou Laços de Repetição
- Executam código de forma automatizada quantas vezes forem necessárias
- Duas estruturas principais: while e for

-----------------------------------------------------------------------------
FUNCIONAMENTO DO WHILE
-----------------------------------------------------------------------------

Fluxo de execução:
1. Um teste lógico é realizado no início do loop
2. Se retornar VERDADEIRO → executa os comandos do bloco
3. Testa novamente automaticamente
4. Se retornar VERDADEIRO → executa novamente
5. Processo se repete até o teste retornar FALSO
6. Quando retorna FALSO → laço é interrompido e programa prossegue

Sintaxe básica:
    while condicao:
        # comandos a serem repetidos

-----------------------------------------------------------------------------
EXEMPLO 1: CONTAGEM DE 1 A 10
-----------------------------------------------------------------------------

numero = 1
while numero <= 10:
    print(numero)
    numero += 1  # Incremento - aumenta o valor em 1
print("Laço encerrado")

Explicação do incremento:
- numero += 1 é um operador de atribuição com incremento
- Pega o valor atual e acrescenta 1
- Pode incrementar por qualquer valor: += 2, += 3, += 10, etc.

IMPORTANTE: Evitar laços infinitos!
- Laço infinito ocorre quando a condição nunca se torna falsa
- Geralmente é um erro de lógica
- Às vezes é necessário (ex: servidores que ficam sempre rodando)

-----------------------------------------------------------------------------
EXEMPLO 2: PROGRAMA COM PARADA INDETERMINADA
-----------------------------------------------------------------------------

# Programa que recebe nomes até o usuário digitar 'x'
nome = None  # None significa "nada" - variável vazia

while True:  # Laço infinito intencional
    print("Digite seu nome, ou x para parar")
    nome = input()
    
    # Verifica condição de parada
    if nome == 'x' or nome == 'X':
        break  # Break finaliza imediatamente o laço
    
    print(f"Bem-vindo, {nome}")  # F-string para exibir mensagens

print("Até logo")

INSTRUÇÃO BREAK:
- Finaliza imediatamente o laço de repetição onde está inserida
- Não finaliza o if, apenas o laço
- Só é executada quando a condição do if é verdadeira

F-STRING:
- Forma de exibir mensagens com variáveis
- Sintaxe: f"texto {variavel} mais texto"
- A variável dentro das chaves é substituída por seu valor

-----------------------------------------------------------------------------
CONCEITOS IMPORTANTES
-----------------------------------------------------------------------------

1. INCREMENTO: Aumentar o valor de uma variável (geralmente += 1)

2. LAÇO INFINITO: 
   - Condição nunca se torna falsa
   - Pode ser erro ou intencional (while True)

3. CONDIÇÃO DE PARADA:
   - Essencial para evitar loops infinitos
   - Pode ser um valor específico ou uma instrução break

4. INDENTAÇÃO:
   - Comandos dentro do while devem estar indentados
   - Indica quais comandos pertencem ao laço

5. ENCADEAMENTO:
   - Pode ter if dentro de while
   - Pode ter while dentro de while (veremos futuramente)

6. OPERADOR OR:
   - Testa múltiplas condições
   - Retorna True se pelo menos uma for verdadeira
   - Útil para comparar maiúsculas e minúsculas

-----------------------------------------------------------------------------
RESUMO DA AULA
-----------------------------------------------------------------------------

✓ Estrutura de repetição while para executar código múltiplas vezes
✓ Fornecimento de valor para condição de parada
✓ Uso de break para sair de loop infinito
✓ Encadeamento de if dentro de while
✓ Introdução a F-strings para exibir mensagens
✓ Importância de balancear: teste lógico + forma de parada

=============================================================================
"""
# numero = 1
# while numero <= 10:
#     print(numero)
#     numero += 1  # Incremento --> aumenta o valor em 1
# print("Laço encerrado")

##############################################################################

# # Programa que pede nomes até o usuário digitar "x"
# nome = None  # None significa "nada" --> variável vazia
# while True:  # Laço infinito intencional
#     print("Digite seu nome, ou x para parar")
#     nome = input()
    
#     # Verifica condição de parada
#     if nome == 'x' or nome == 'X':
#         print("Até logo")
#         exit()  # Finaliza o programa
    
#     print(f"Bem-vindo, {nome}")  # F-string para exibir mensagens

##############################################################################

nome = None  # None significa "nada" - variável vazia

while True:  # Laço infinito intencional
    print("Digite seu nome, ou x para parar")
    nome = input()
    
    # Verifica condição de parada
    if nome == 'x' or nome == 'X':
        break  # Break finaliza imediatamente o laço
    
    print(f"Bem-vindo, {nome}")  # F-string para exibir mensagens

print("Até logo")