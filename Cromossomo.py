"""
    Código modificado do código base: https://github.com/itsmeale/algoritmos-geneticos/tree/master/ga-basico
"""

import math, random

class Cromossomo():

    def __init__(self, tamanho, limiteMaximo, limiteMinimo):

        self.tamanho = tamanho
        self.valorX = ""
        self.valorY = ""
        self.limiteMaximo = limiteMaximo
        self.limiteMinimo = limiteMinimo

    def set_valor(self, valorX, valorY):

        self.valorX = valorX
        self.valorY = valorY
    
    def get_bin(self, x, n):
        """
        Get the binary representation of x.

        Parameters
        ----------
        x : int
        n : int
            Minimum number of digits. If x needs less digits in binary, the rest
            is filled with zeros.

        Returns
        -------
        str
        """
        return format(x, 'b').zfill(n)

    def inicializar(self):
        for i in range(self.tamanho):
            for j in range(2):
                numX = random.randrange(self.limiteMinimo, self.limiteMaximo, 2)
                self.valorX = self.get_bin(numX, self.tamanho)
                numY = random.randrange(self.limiteMinimo, self.limiteMaximo, 2)
                self.valorY = self.get_bin(numY, self.tamanho)

    # TODO Valor minímo e máximo
    def crossover(self, outro_cromossomo, chance_crossover):
        split_index = int(random.random() * self.tamanho)
        novo_valorX = ""
        novo_valorY = ""
        if random.random() < chance_crossover:
            novo_valorX = self.valorX[0:split_index] + outro_cromossomo.valorX[split_index:len(outro_cromossomo.valorX)]
            novo_valorY = self.valorY[0:split_index] + outro_cromossomo.valorY[split_index:len(outro_cromossomo.valorY)]
        else:
            novo_valorX = outro_cromossomo.valorX[0:split_index] + self.valorX[split_index:len(outro_cromossomo.valorX)]
            novo_valorY = outro_cromossomo.valorY[0:split_index] + self.valorY[split_index:len(outro_cromossomo.valorY)]
        novo_cromossomo = Cromossomo(self.tamanho, self.limiteMaximo, self.limiteMinimo)
        
        if int(novo_valorX, 2) > self.limiteMaximo:
            novo_valorX = self.get_bin(self.limiteMaximo, self.tamanho)
            if int(novo_valorY) > self.limiteMaximo:
                novo_valorY = self.get_bin(self.limiteMaximo, self.tamanho)
            elif int(novo_valorY) < self.limiteMinimo:
                novo_valorY = self.get_bin(self.limiteMinimo, self.tamanho)
        elif int(novo_valorX) < self.limiteMinimo:
            novo_valorX = self.get_bin(self.limiteMinimo, self.tamanho)
            if int(novo_valorY) > self.limiteMaximo:
                novo_valorY = self.get_bin(self.limiteMaximo, self.tamanho)
            elif int(novo_valorY) < self.limiteMinimo:
                novo_valorY = self.get_bin(self.limiteMinimo, self.tamanho)

        novo_cromossomo.set_valor(novo_valorX, novo_valorY)
        
        return novo_cromossomo

    def mutacao(self, chance_mutacao):

        inicio, aux, fim = ['','','']
        novo_valorX = ""
        novo_valorY = ""
        for i in range(self.tamanho):
            if random.random() < chance_mutacao:
                inicio = self.valorX[0:i]
                fim = self.valorX[i+1:self.tamanho]
                aux = self.valorX[i]
                novo_valorX = inicio+aux+fim
        for i in range(self.tamanho):
            if random.random() < chance_mutacao:
                inicio = self.valorY[0:i]
                fim = self.valorY[i+1:self.tamanho]
                aux = self.valorY[i]
                novo_valorY = inicio+aux+fim
        
        self.set_valor(novo_valorX, novo_valorY)

    def avaliar(self):
        print("Valor X %d", self.valorX)
        print("Valor Y %d", self.valorY)
        x = int(self.valorX, 2)
        y = int(self.valorY, 2)

        self.avaliacao = (1-x)**2+100*(y-x**2)**2
        return self.avaliacao

    def __repr__(self):
        return "cromossomo: X[%s] Y[%s] fitness[%.2f] valor X[%d] valor Y[%d]" % (self.valorX, self.valorY, self.avaliacao, int(self.valorX, 2), int(self.valorY, 2))
        
