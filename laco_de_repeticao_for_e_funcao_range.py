
"""
=============================================================================
LAÇO DE REPETIÇÃO FOR E FUNÇÃO RANGE
=============================================================================

O LAÇO FOR EM PYTHON
- Estrutura de repetição muito importante
- Permite construir loops para iteração em sequências de dados
- Funciona com: listas, tuplas, strings, conjuntos, dicionários, etc.
- Diferente do for na maioria das outras linguagens
- Funciona como um método iterador
- Executa comandos sobre cada item da sequência

Sintaxe básica:
    for item in sequencia:
        # instruções

Tradução: "para cada item em sequência, faça..."
- item: nome da variável (pode ser qualquer nome)
- in: operador de associação
- sequencia: conjunto de valores a processar

-----------------------------------------------------------------------------
EXEMPLO 1: ITERANDO SOBRE UMA LISTA
-----------------------------------------------------------------------------

# Lista: estrutura de dados criada com colchetes []
lista = [2, 6, 9, 40, 12, 3]

for item in lista:
    print(item)

# Saída: imprime cada número em uma linha
# 2
# 6
# 9
# 40
# 12
# 3

-----------------------------------------------------------------------------
EXEMPLO 2: ITERANDO SOBRE UMA STRING
-----------------------------------------------------------------------------

# Strings são sequências de caracteres
palavra = "bosom"

for letra in palavra:
    print(letra)

# Saída: uma letra por vez
# b
# o
# s
# o
# m

IMPORTANTE: O for pode iterar sobre qualquer tipo de sequência!

-----------------------------------------------------------------------------
FUNÇÃO RANGE - GERANDO SEQUÊNCIAS DE NÚMEROS
-----------------------------------------------------------------------------

A função range() gera faixas de valores e tem 3 formas de uso:

1. range(valor_final)
   - Gera de 0 até valor_final - 1
   
   for numero in range(10):
       print(numero)
   # Saída: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

2. range(valor_inicial, valor_final)
   - Gera de valor_inicial até valor_final - 1
   - O valor_final NÃO entra na sequência (sempre -1)
   
   for numero in range(1, 11):
       print(numero)
   # Saída: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

3. range(valor_inicial, valor_final, incremento)
   - Gera valores com passo customizado
   - Pode ser usado para pares, ímpares, ou qualquer sequência
   
   # Números pares de 2 a 20
   for x in range(2, 20, 2):
       print(x)
   # Saída: 2, 4, 6, 8, 10, 12, 14, 16, 18
   
   # Contagem de 3 em 3
   for x in range(2, 21, 3):
       print(x)
   # Saída: 2, 5, 8, 11, 14, 17, 20

DECREMENTO (contagem regressiva):
- Use incremento negativo para contar de trás pra frente

for x in range(20, 2, -2):
    print(x)
# Saída: 20, 18, 16, 14, 12, 10, 8, 6, 4

# Para incluir o valor final, use um número a menos:
for x in range(20, 1, -2):
    print(x)
# Agora inclui o 2

-----------------------------------------------------------------------------
EXEMPLO 3: REPETIR AÇÕES X VEZES
-----------------------------------------------------------------------------

# Imprimir nome 10 vezes com numeração
nome = input("Digite seu nome: ")

for x in range(10):
    print(f"{x + 1} {nome}")

# Saída exemplo (nome = "Fábio"):
# 1 Fábio
# 2 Fábio
# 3 Fábio
# ...
# 10 Fábio

OBSERVAÇÃO: x + 1 é usado porque range(10) gera 0-9
Para mostrar 1-10, somamos 1 na exibição

SACADA IMPORTANTE:
- Se range gera 10 valores, o loop executa 10 vezes
- Não é obrigatório usar a variável iteradora dentro do loop
- Útil quando só quer repetir comandos X vezes

-----------------------------------------------------------------------------
EXEMPLO 4: TUPLAS E INSTRUÇÃO CONTINUE
-----------------------------------------------------------------------------

# Tupla: estrutura de dados criada com parênteses ()
# Diferente de lista (veremos detalhes em aula específica)
pedras = ("Rubi", "Esmeralda", "Quartzo", "Safira", "Diamante", "Turmalina")

# Objetivo: imprimir todas as pedras EXCETO "Quartzo"
for pedra in pedras:
    if pedra == "Quartzo":
        continue  # Pula a iteração atual
    print(pedra)

# Saída:
# Rubi
# Esmeralda
# (Quartzo foi pulado)
# Safira
# Diamante
# Turmalina

-----------------------------------------------------------------------------
INSTRUÇÕES BREAK E CONTINUE
-----------------------------------------------------------------------------

CONTINUE:
- Encerra APENAS a iteração atual do laço
- O laço continua nas próximas iterações
- Não executa o código abaixo dele na iteração atual
- Funciona em for e while

BREAK:
- Finaliza IMEDIATAMENTE o laço inteiro
- Sai completamente do loop
- Não executa mais nenhuma iteração
- Funciona em for e while

Comparação:
for numero in range(1, 6):
    if numero == 3:
        continue  # Pula só o 3, continua com 4, 5
    print(numero)
# Saída: 1, 2, 4, 5

for numero in range(1, 6):
    if numero == 3:
        break  # Para tudo quando chega no 3
    print(numero)
# Saída: 1, 2

-----------------------------------------------------------------------------
COMBINANDO FOR COM RANGE
-----------------------------------------------------------------------------

Vantagem: O for com range se comporta como for em outras linguagens
- Permite executar código X vezes de forma controlada
- Útil quando você precisa de um contador
- Flexível para incrementos/decrementos customizados

Exemplo completo:
for i in range(1, 11):
    print(f"Executando pela {i}ª vez")
# Executa exatamente 10 vezes com contador

-----------------------------------------------------------------------------
CONCEITOS IMPORTANTES
-----------------------------------------------------------------------------

1. ITERAÇÃO: Processo de percorrer cada elemento de uma sequência

2. ITERADOR: Variável que assume o valor de cada elemento da sequência

3. SEQUÊNCIAS EM PYTHON:
   - Listas: [1, 2, 3]
   - Tuplas: (1, 2, 3)
   - Strings: "texto"
   - Conjuntos: {1, 2, 3}
   - Dicionários: {'chave': 'valor'}

4. F-STRING: Forma de formatar strings com variáveis
   f"{variavel} texto {outra_variavel}"

5. RANGE: Sempre gera valor_final - 1
   - range(10) → 0 a 9
   - range(1, 11) → 1 a 10
   - range(2, 20, 2) → 2, 4, 6, ..., 18

6. ESTRUTURAS DE DADOS:
   - Lista: [] - será estudada em aula específica
   - Tupla: () - será estudada em aula específica

-----------------------------------------------------------------------------
CASOS DE USO
-----------------------------------------------------------------------------

✓ Processar cada item de uma lista/tupla
✓ Iterar sobre caracteres de uma string
✓ Executar código X vezes (com range)
✓ Gerar sequências numéricas customizadas
✓ Contagens progressivas e regressivas
✓ Pular elementos específicos (continue)
✓ Parar em condição específica (break)

-----------------------------------------------------------------------------
RESUMO DA AULA
-----------------------------------------------------------------------------

✓ Laço for para iteração em sequências
✓ Sintaxe: for item in sequencia
✓ Função range() com 1, 2 ou 3 argumentos
✓ Range sempre para em valor_final - 1
✓ Continue pula iteração atual
✓ Break finaliza o laço completamente
✓ For funciona com listas, tuplas, strings e outras sequências
✓ Combinação for + range permite loops controlados
✓ Incremento positivo (progressivo) e negativo (regressivo)

PRÓXIMOS ASSUNTOS:
- Números aleatórios
- Imports
- Listas (detalhado)
- Tuplas (detalhado)
- Dicionários

=============================================================================
"""
