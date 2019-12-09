# -*- coding: utf-8 -*-
import numpy as np

class CortexOrbitoFrontal :
    def __init__(self,S,rew,E) :
        self.S = S
        self.rew = rew
        self.O = np.zeros(S.size)
        self.W = np.zeros(S.size)
        self.E = E

    def poids_Wi(self, beta = 0.8) :
        for i in range(self.W.size) :
            self.W[i]+= beta *(self.S[i]*(np.sum(self.O)-(self.rew[0]*np.sum(self.S))))

    def maj_O(self) :
        for i in range(self.O.size) :
            self.O[i] = self.S[i]*self.W[i]

    def pas_de_temps(self,S,rew,E,first = False) :
        self.S = S
        self.rew = rew
        self.E = E
        self.poids_Wi()
        if first :
            self.W = np.zeros(S.size)
        self.maj_O()
