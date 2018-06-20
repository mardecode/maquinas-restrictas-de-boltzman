import numpy as np

class Red():
    def __init__(self, entrada,nSalidas):
        self.inputt = np.array(entrada)
        self.nSalidas  = np.array(nSalidas)
        self.pesos = np.random.rand(len(entrada),nSalidas)
        self.b = np.random.rand(1,nSalidas)
        self.c = np.random.rand(1,len(entrada))
        self.h = 1
        self.vq = 1
        self.hq = 1

    def forward (self, x, y,b):
        #print x.shape
        #print y.shape
        #print b.shape
        return 1/(1+np.exp(-np.matmul(x,y))+b)

    def aprender (self):
        self.h = self.forward(self.inputt,self.pesos,self.b)
        print "h" , self.h.shape
                                    #5X2  #2x1   #1x5
        self.vq = self.forward(self.pesos,self.h.T,self.c.T).T
        print "vq" , self.vq.shape

        self.hq = self.forward(self.vq,self.pesos,self.b)
        print "hq" , self.hq

    def update(self, factor):
        self.pesos = self.pesos +factor*(np.matmul((self.h).T,inputt)-np.matmul((self.hq).T,vq)).T
        self.c = self.c +factor*(self.h-self.hq)
        self.b = self.b+factor*(self.inputt-self.vq)
