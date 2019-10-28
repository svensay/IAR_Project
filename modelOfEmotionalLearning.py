# -*- coding: utf-8 -*-
import numpy as np

E = 0
A = np.zeros(1)
O = np.zeros(1)

alpha = 0.2
beta = 0.8

"""
    S : Stimuli venant du cortex sensoriel
    Tmax : le plus grand stimuli du thamalus
    rew : réconpense
    
"""
def amygdale(S,Tmax,rew):
    V = np.zeros(S.shape)
    
    Aj = np.sum(A) # la somme des A du précédent step
    
    for i in range(V.size):
        V[i] = alpha * (S[i]*max(0,(rew-Aj)))
        
    np.append(V,[alpha * (Tmax*max(0,(rew-Aj)))])
    
    A.resize(V.shape)
    
    for i in range(A.size - 1):
        A[i] = S[i] * V[i]
    
    np.append(A,[Tmax*V[V.size-1]])
    
    
"""
    S : Stimuli venant du cortex sensoriel
    rew : réconpense
"""
def cortexOrbitoFrontal(S,rew):
    W = np.zeros(S.shape)
    sum_Oj = 0
    
    for i in range(O.size):
        sum_Oj += (O[i] - rew)
    
    for i in range(W.size):
        W[i] = beta * ( S[i] * sum_Oj )
        
    for i in range (O.size):
        O[i] = S[i]*W[i]
    
if __name__ == "__main__":
    for i in range(0,10):
        S = np.array([1.0])
        rew = 1
        amygdale(S,1,rew)
        cortexOrbitoFrontal(S,rew)
        E = np.sum(A) - np.sum(O)
        print(E)
        print(A)
        print(O)