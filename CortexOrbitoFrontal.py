# -*- coding: utf-8 -*-
import numpy as np

class CortexOrbitoFrontal :
    def __init__(self,S,rew) :
        self.S = S
        self.rew = rew
        self.W = np.zeros(S.size)
        self.O = np.zeros(S.size)
        self.E = 1.
        
    """
    Calcul les poids des connections W des noeuds O
    """
    def poids_Wi(self,beta = 0.8) :
        for i in range(self.W.size) :
            self.W[i]+= beta*(self.S[i]*(self.E-(self.rew[0])))
            if self.W[i] < 0 :
                self.W[i] = 0
    
    """
    Calcul la valeur des noeuds A
    """
    def maj_O(self):
        for i in range(self.O.size) :
            self.O[i] = self.S[i] * self.W[i]

    """
    Met a jour la valeur du noeud E
    """
    def maj_E(self,E):
        self.E = E
          
    """
    Applique un pas de temps qui met a jour les données
    """
    def pas_de_temps(self,S,rew) :
        self.S = S
        self.rew = rew
        self.poids_Wi()
        self.maj_O()
