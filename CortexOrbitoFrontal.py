# -*- coding: utf-8 -*-
import numpy as np

class CortexOrbitoFrontal :
    def __init__(self,S,rew) :
        self.S = S
        self.rew = rew
        self.W = np.zeros(S.size)
        self.O = np.zeros(S.size)
        self.Oj = 0

    def calcul_somme_O(self) :
        self.Oj = 0
        for i in range(self.O.size) :
            self.Oj+=self.O[i]-self.rew

    def poids_Wi(self,beta = 0.8) :
        for i in range(self.W.size) :
            self.W[i]=beta*(self.S[i]*self.Oj)

    def maj_O(self):
        for i in range(self.O.size) :
            self.O[i] = self.S[i] * self.W[i]
            
    def pas_de_temps(self,S,rew) :
        self.S = S
        self.rew = rew
        self.W.resize(S.size)
        self.O.resize(S.size)
        self.calcul_somme_O()
        self.poids_Wi()
        self.maj_O()
