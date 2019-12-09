# -*- coding: utf-8 -*-
import numpy as np

class CortexOrbitoFrontal :
    def __init__(self,S,rew) :
        self.S = S
        self.rew = rew
        self.W = np.zeros(S.size)
        self.O = np.zeros(S.size)
        self.Oj = 0.
        self.E = 1.

    def calcul_somme_O(self) :
        self.Oj = 0
        #for i in range(self.O.size) :
            #self.Oj+=self.O[i]-(self.rew[0]*self.S[i])
        self.Oj = self.E-self.rew
            

    def poids_Wi(self,beta = 0.8) :
        #print("taille ", self.W.size)
        for i in range(self.W.size) :
            #self.W[i]+=beta*(self.S[i]*self.Oj)
            self.W[i]+= beta*(self.S[i]*(self.E-(self.rew[0])))
            if self.W[i] < 0 :
                self.W[i] = 0
            
            """
            print("E = ",self.E)
            print("rew = ",self.rew[0])
            print("W = ",self.W[i])
            """

    def maj_O(self):
        for i in range(self.O.size) :
            self.O[i] = self.S[i] * self.W[i]
            #print("O = ",self.O[i])

    def maj_E(self,E):
        self.E = E
            
    def pas_de_temps(self,S,rew) :
        self.S = S
        self.rew = rew
        #self.W.resize(S.size)
        #self.O.resize(S.size)
        self.calcul_somme_O()
        self.poids_Wi()
        self.maj_O()
