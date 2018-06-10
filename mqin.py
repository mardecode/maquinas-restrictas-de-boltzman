import numpy as np

class Red():
    def __init__(self, entrada,nSalidas):
        self.input = entrada
        self.nSalidas  = nSalidas
        self.pesos = np.random.rand(len(entrada),nSalidas)
        self.b = np.random.rand(1,nSalidas)
        self.c = np.random.rand(1,len(entrada))
        self.output

    def forward (self):
        ##activacion
        self.output =1/(1+np.exp(-np.matmul(self.input,self.pesos))+b)
    def backward(self):
        s =1/(1+np.exp(-np.matmul(self.pesos,self.output))+c)
