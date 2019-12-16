# -*- coding: utf-8 -*-
import numpy as np

class Amygdala:
    def __init__(self,S,Th,rew,thal = True) :
        if thal :
            S_t = S.size+1
        else :
            S_t = S.size
        self.S = S
        self.Th = Th
        self.rew = rew
        self.V = np.zeros(S_t)
        self.Aj = 0.1*(S_t)
        self.A = np.full((S_t),0.1)
        if not thal :
            for i in range(S_t) :
                self.A[i] = self.A[i]*self.S[i]
        if thal :
            for i in range(S_t-1) :
                self.A[i] = self.A[i]*self.S[i]
            self.A[-1] = Th * 0.1
    
    """
    Attribué a Aj la somme des A pour le calcul du prochain pas de temps
    """
    def calcul_somme_A(self):
        self.Aj = np.sum(self.A)

    """
    Calcul les poids des connections V des noeuds A
    """
    def poids_Vi(self,alpha,thal) :
        if thal :
            V_t = self.V.size-1
        else :
            V_t = self.V.size
        for i in range(V_t) :
            self.V[i] += alpha*(self.S[i]*max(0,(self.rew-self.Aj)))
        if thal :
            self.V[-1] +=alpha*(self.Th*max(0,(self.rew-self.Aj)))
    
    """
    Calcule la valeur des noeuds A
    """
    def maj_A(self,thal):
        if thal :
            A_t = self.A.size-1
        else :
            A_t = self.A.size
        for i in range(A_t):
            self.A[i] = self.S[i] * self.V[i]
        if thal:
            self.A[-1] = self.Th* self.V[-1]

    """
    Applique un pas de temps qui met a jour les données
    """
    def pas_de_temps(self,S,Th,rew,alpha=0.2,thal=True) :
        self.S = S
        self.Th = Th
        self.rew = rew
        
        self.calcul_somme_A()
        self.poids_Vi(alpha,thal)
        self.maj_A(thal)
        
    """
    Calcule la valeur du noeud E
    """
    def calcul_E(self,O) :
        if(np.sum(self.A) - np.sum(O) < 0):
            return 0
        return np.sum(self.A) - np.sum(O)
