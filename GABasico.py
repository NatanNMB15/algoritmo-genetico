"""
    Autor: Natan Barbosa

    Código modificado do código base: https://github.com/itsmeale/algoritmos-geneticos/tree/master/ga-basico
"""

from Cromossomo import Cromossomo
import random, time, numpy
import matplotlib.pyplot

class GABasico():
    def __init__(self, tamanho_populacao, geracoes, limiteMinimo, limiteMaximo, 
                limiteBits, chanceCrossover, chanceMutacao, minimizacao,
                roleta, torneio):

        self.populacao = []
        self.tam_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.soma_avaliacoes = 0
        self.limiteMinimo = limiteMinimo
        self.limiteMaximo = limiteMaximo
        self.limiteBits = limiteBits
        self.chanceCrossover = chanceCrossover
        self.chanceMutacao = chanceMutacao
        self.minimizacao = minimizacao
        self.selecaoRoleta = roleta
        self.selecaoTorneio = torneio

    def inicializar_populacao(self):

        for i in range(self.tam_populacao):
            self.populacao.append(Cromossomo(self.limiteBits, self.limiteMaximo, self.limiteMinimo))
        for cromossomo in self.populacao: cromossomo.inicializar()

    def avaliar_populacao(self):

        self.soma_avaliacoes = 0
        for cromossomo in self.populacao:
            # Se for maximização
            if self.minimizacao == 0:
                self.soma_avaliacoes += cromossomo.avaliar()
            # Se for minimização
            else:
                self.soma_avaliacoes -= cromossomo.avaliar()
        

    def roleta(self):
        self.avaliar_populacao()
        fs = [cromossomo.avaliar() for cromossomo in self.populacao]
        max_fs = max(fs)
        min_fs = min(fs)
        t = max_fs + min_fs
        limite = random.random() * self.soma_avaliacoes
        i, aux = [0, 0]
        random.shuffle(self.populacao)
        while aux < limite and i < self.tam_populacao:
            if self.minimizacao == 0:
                aux += self.populacao[i].avaliacao
            else:
                aux += (t - self.populacao[i].avaliacao)
            i += 1
        i -= 1
        return i

    def torneio(self):
        melhor = -1
        for i in range(self.tam_populacao):
            if self.minimizacao == 0:
                if melhor == -1 or self.populacao[i].avaliar() > self.populacao[melhor].avaliar():
                    melhor = i
            else:
                if melhor == -1 or self.populacao[i].avaliar() < self.populacao[melhor].avaliar():
                    melhor = i
        return melhor

    def nova_geracao(self):
        nova_populacao = []
        for i in range(self.tam_populacao):
            if(self.selecaoRoleta == True):
                pai1 = self.populacao[self.roleta()]
                pai2 = self.populacao[self.roleta()]
            elif(self.selecaoTorneio == True):
                pai1 = self.populacao[self.torneio()]
                pai2 = self.populacao[self.torneio()]
            filho = pai1.crossover(pai2, self.chanceCrossover)
            filho.mutacao(self.chanceMutacao)
            nova_populacao.append(filho)
        return nova_populacao

    def executar(self):
        best_outputs = []
        print("\n\nInicializando execucao do algorimo genético:...\n\n")
        self.inicializar_populacao()
        self.avaliar_populacao()
        # Se for maximização
        if self.minimizacao == 0:
            ordenado = sorted(self.populacao, key = lambda x: x.avaliacao, reverse = True)
        else:
            ordenado = sorted(self.populacao, key = lambda x: x.avaliacao, reverse = False)
        valorFitness = self.soma_avaliacoes
        best_outputs.append(valorFitness)
        for i in range(self.geracoes):
            pop1 = self.populacao[0]
            pop2 = self.populacao[1]
            pop3 = self.populacao[2]
            pop4 = self.populacao[3]
            pop5 = self.populacao[4]
            print("5 cromossomos da geração %d:\n%s\n%s\n%s\n%s\n%s\n\n" % (i + 1, pop1, pop2, pop3, pop4, pop5), end="", flush = True)
            
            top1 = ordenado[0]
            print("Melhor cromossomo da geração %d:\n%s\n\n" % (i + 1, top1), end="", flush = True)
            print("Fitness da geração %d:\n%s\n\n" % (i + 1, valorFitness), end="", flush = True)

            time.sleep(.5)
            
            self.populacao = self.nova_geracao()
            self.avaliar_populacao()
            if self.minimizacao == 0:
                ordenado = sorted(self.populacao, key = lambda x: x.avaliacao, reverse = True)
            else:
                ordenado = sorted(self.populacao, key = lambda x: x.avaliacao, reverse = False)
            valorFitness = self.soma_avaliacoes
            best_outputs.append(valorFitness)
        matplotlib.pyplot.plot(best_outputs)
        matplotlib.pyplot.xlabel("Geração")
        matplotlib.pyplot.ylabel("Fitness")
        matplotlib.pyplot.show()