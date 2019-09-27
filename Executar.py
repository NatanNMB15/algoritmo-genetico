"""
    Autor: Natan Barbosa

    Código modificado do código base: https://github.com/itsmeale/algoritmos-geneticos/tree/master/ga-basico
"""

from GABasico import GABasico

# Parte inicial do código de execução
selecaoRoleta = False
selecaoTorneio = False

tamanho_populacao = int(input("Digite o tamanho da população: "))
geracoes = int(input("Digite o número de gerações: "))

print("""
Escolha o tipo de seleção:
1 - Roleta
2 - Torneio
""")
selecao = int(input())

if(selecao == 1):
    selecaoRoleta = True
elif(selecao == 2):
    selecaoTorneio = True

limiteBits = int(input("Digite o limite máximo de Bits: "))
verificarBits = ""
i = 0
while i < limiteBits:
    verificarBits += '1'
    i += 1
limiteNBits = int(verificarBits, 2)
limiteMaximo = int(input("Digite o limite de valor máximo: "))
if limiteMaximo % 2 != 0:
    print("Digite um valor divisível por 2")
    exit(-1)
elif limiteMaximo > limiteNBits:
    print("Valor maior que o número de casas dos Bits, que é: ", limiteNBits)
    exit(-1)
limiteMinimo = int(input("Digite o limite de valor mínimo: "))
if limiteMinimo % 2 != 0:
    print("Digite um valor divisível por 2")
    exit(-1)
elif limiteMinimo < (limiteNBits * (-1)):
    print("Valor menor que o número de casas dos Bits negativos, que é: ", (limiteNBits * (-1)))
    exit(-1)
print("""
Escolha se é maximização ou minimização:
1 - Maximização
2 - Minimização
""")
operacao = int(input())
minimizacao = 1
if operacao == 1:
    minimizacao = 0

chanceCrossover = float(input("Digite a taxa probabilidade de cruzamento: "))
chanceMutacao = float(input("Digite a taxa probabilidade de mutação: "))

ga = GABasico(tamanho_populacao, geracoes, limiteMinimo, limiteMaximo, limiteBits, 
                chanceCrossover, chanceMutacao, minimizacao,
                selecaoRoleta, selecaoTorneio)
ga.executar()