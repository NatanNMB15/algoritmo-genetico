"""
    Código modificado do código base: https://github.com/itsmeale/algoritmos-geneticos/tree/master/ga-basico
"""

import math, random

class Cromossomo():

    def __init__(self, tamanho, limiteMaximo, limiteMinimo):

        self.tamanho = tamanho
        self.valor = ""
        self.avaliacao = -1
        self.valorX = 0
        self.valorY = 0
        self.limiteMaximo = limiteMaximo
        self.limiteMinimo = limiteMinimo

    def set_valor(self, novo_valor):

        self.valor = novo_valor
    
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
        novo_valor = ""
        for i in range(self.tamanho):
            num = random.randrange(self.limiteMinimo, self.limiteMaximo, 2)
            novo_valor = self.get_bin(num, self.tamanho)
        self.set_valor(novo_valor)

    # TODO Valor minímo e máximo
    def crossover(self, outro_cromossomo, chance_crossover):
        split_index = int(random.random() * self.tamanho)
        novo_valor = ""
        if random.random() < chance_crossover:
            novo_valor = self.valor[0:split_index] + outro_cromossomo.valor[split_index:len(outro_cromossomo.valor)]
        else:
            novo_valor = outro_cromossomo.valor[0:split_index] + self.valor[split_index:len(outro_cromossomo.valor)]
        novo_cromossomo = Cromossomo(self.tamanho, self.limiteMaximo, self.limiteMinimo)
        if int(novo_valor) > self.limiteMaximo:
            novo_valor = self.get_bin(self.limiteMaximo, self.tamanho)
            novo_cromossomo.set_valor(novo_valor)
        elif int(novo_valor) < self.limiteMinimo:
            novo_valor = self.get_bin(self.limiteMinimo, self.tamanho)
            novo_cromossomo.set_valor(novo_valor)
        else:
            novo_cromossomo.set_valor(novo_valor)
        return novo_cromossomo

    def mutacao(self, chance_mutacao):

        inicio, aux, fim = ['','','']
        for i in range(self.tamanho):
            if random.random() < chance_mutacao:
                inicio = self.valor[0:i]
                fim = self.valor[i+1:self.tamanho]
                aux = self.valor[i]
                self.set_valor(inicio+aux+fim)

    def valor_real(self, inf = 0, sup = 100):

        return inf + (sup - inf)/(2**self.tamanho - 1)*int(self.valor, 2)

    def avaliar(self):

        self.valorX = random.randrange(self.limiteMinimo, self.limiteMaximo)
        self.valorY = random.randrange(self.limiteMinimo, self.limiteMaximo)

        x = self.valorX
        y = self.valorY

        self.avaliacao = (1-x)**2+100*(y-x**2)**2
        return self.avaliacao

    def __repr__(self):
        return "cromossomo:[%s] fitness[%.2f] valor[%d] X[%d] Y[%d]" % (self.valor, self.avaliacao, int(self.valor, 2), self.valorX, self.valorY)
        
