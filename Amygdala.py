# -*- coding: utf-8 -*-
import numpy as np

class Amygdala:
    def __init__(self,S,Th,rew) :
        self.S = S
        self.Th = Th
        self.rew = rew
        self.V = np.zeros(S.size+1)
        self.Aj = 0
        self.A = np.zeros(S.size+1)
        
    def calcul_somme_A(self):
        self.Aj = np.sum(self.A)

    def poids_Vi(self,alpha = 0.2) :
        for i in range(self.V.size-1) :
            self.V[i] += alpha*(self.S[i]*max(0,(self.rew-self.Aj)))
        self.V[-1] +=alpha*(self.Th*max(0,(self.rew-self.Aj)))

    def maj_A(self):
        for i in range(self.A.size-1):
            self.A[i] = self.S[i] * self.V[i]
        self.A[-1] = self.Th * self.V[-1]

    def pas_de_temps(self,S,Th,rew) :
        self.S = S
        self.Th = Th
        self.rew = rew
        self.V.resize(S.size+1)
        self.A.resize(S.size+1)
        self.calcul_somme_A()
        self.poids_Vi()
        self.maj_A()

    def calcul_E(self,O) :
        #print("O = ",self.O[i])
        return np.sum(self.A) - np.sum(O)-self.A[-1]
