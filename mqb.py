import numpy as np

class Red():
    def __init__(self, entrada,nSalidas):
        self.inputt = entrada
        self.nSalidas  = nSalidas
        self.pesos = np.random.rand(len(entrada),nSalidas)
        self.b = np.random.rand(1,nSalidas)
        self.c = np.random.rand(1,len(entrada))
        self.h = 1
        self.vq = 1
        self.hq = 1

    def forward (self, x, y,b):
        ##activacion
        #self.outputv =1/(1+np.exp(-np.matmul(self.inputt,self.pesos))+self.b)
        #outputh = 1/(1+np.exp(-np.matmul(self.pesos,self.outputv))+self.c)
        return 1/(1+np.exp(-np.matmul(x,y))+b)

    def aprender (self):
        self.h = self.forward(self.inputt,self.pesos,self.b)
        self.vq = self.forward(self.pesos,self.h.T,self.c).T
        self.hq = self.forward(self.vq,self.pesos,self.b)

    def update(self, factor):
        self.pesos = self.pesos +factor*(np.matmul((self.h).T,inputt)-np.matmul((self.hq).T,vq)).T
        self.c = self.c +factor*(self.h-self.hq)
        self.b = self.b+factor*(self.inputt-self.vq)
