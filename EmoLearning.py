# -*- coding: utf-8 -*-
import numpy as np
import Amygdala as am
import CortexOrbitoFrontal as cof

if __name__ == "__main__":
    S = np.ones(1)
    Th = np.max(S)
    #rew = np.zeros(1500)
    #for i in range(1500) :
    #    if i < 300 or (i > 600 and i < 901) or (i > 1201 and i < 1502) :
    #        rew[i] = 1.
    rew = np.ones(15)
    amygdale = am.Amygdala(S,Th,rew[0])
    CoF = cof.CortexOrbitoFrontal(S,rew[0])
    for i in range(15) :
        amygdale.pas_de_temps(S,Th,rew[i])
        CoF.pas_de_temps(S,rew[i])
        E = amygdale.calcul_E(CoF.O)
        print(" i -> ",i)
        print("E = ",E)
        print("A = ",amygdale.A)
        print("V = ",amygdale.V)
        print("O = ",CoF.O)
        print("W = ",CoF.W)
        print(" ")

        S = np.ones(1)
        Th = np.max(S)
