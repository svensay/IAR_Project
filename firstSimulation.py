# -*- coding: utf-8 -*-
import numpy as np
import Amygdala as am
import CortexOrbitoFrontal as cof
import matplotlib.pyplot as plt

if __name__ == "__main__":
 
    nb_graph = 7
    x_range = 1700
    
    th = np.ones((x_range,), dtype=int) # Stimulus du Thalamus
    s = np.ones((x_range,), dtype=float) # Stimulus du Cortex Sensible (Sensory Cortex)
    
    a = np.ones((300,), dtype=int) # Récompense de 0 a 300 environ qui vaut 1
    b = np.zeros((400,), dtype=int) # Récompense de 300 a 700 environ qui vaut 0
    c = np.ones((300,), dtype=int) # Récompense de 700 a 1000 environ qui vaut 1
    d = np.zeros((400,), dtype=int) # Récompense de 1000 a 1400 environ qui vaut 0
    e = np.ones((300,), dtype=int) # Récompense de 1400 a 1700 environ qui vaut 1
    rew = np.concatenate((a, b, c, d, e), axis=0) # Récompense
    
    amygdale = am.Amygdala(np.array([s[0]]),np.array([th[0]]),np.array([rew[0]]))
    cortexorbitofrontal = cof.CortexOrbitoFrontal(np.array([s[0]]),np.array([rew[0]]))
    
    E = np.array([]) # Tableaux des E
    
    vth = np.array([]) # Tableaux des Vth
    
    v0 = np.array([]) # Tableaux des V0
    
    w0 = np.array([]) # Tableaux des W0

    eValue = float(s[0])
    
    for i in range(x_range):
        # Calcul d'un pas de temps
        amygdale.pas_de_temps(np.array([s[i]]),np.array([th[i]]),np.array([rew[i]]))
        cortexorbitofrontal.maj_E(eValue)
        cortexorbitofrontal.pas_de_temps(np.array([s[i]]),np.array([rew[i]]))
        
        # Calcult de la valeur de E
        eValue = amygdale.calcul_E(cortexorbitofrontal.O)
        
        # Ajout dans les tableaux leurs valeurs respectives
        E = np.append(E,eValue)
        vth = np.append(vth,amygdale.V[-1])
        v0 = np.append(v0,amygdale.V[0])
        w0 = np.append(w0,cortexorbitofrontal.W[0])
        #print("\t i = ", i)
    
    # Axes de x
    x = np.arange(0,x_range)
    
    # Graphe en bar de Th
    plt.subplot(nb_graph, 1, 1)
    plt.ylabel('Th')
    plt.xticks([])
    plt.bar(x,th,color=['black'])
    
    # Graphe en bar de S
    plt.subplot(nb_graph, 1, 2)
    plt.ylabel('S')
    plt.xticks([])
    plt.bar(x,s,color=['black'])
    
    # Graphe en courbe de E
    plt.subplot(nb_graph, 1, 3)
    plt.ylabel('E')
    plt.xticks([])
    plt.plot(x,E,'k')  

    # Graphe en bar de Rew
    plt.subplot(nb_graph, 1, 4)
    plt.ylabel('Rew')
    plt.xticks([])
    plt.bar(x,rew,color=['black'])
    
    # Graphe en courbe de Vth
    plt.subplot(nb_graph, 1, 5)
    plt.ylabel('Vth')
    plt.xticks([])
    plt.plot(x,vth,'k')
    
    # Graphe en courbe de V0
    plt.subplot(nb_graph, 1, 6)
    plt.ylabel('V0')
    plt.xticks([])
    plt.plot(x,v0,'k')
    
    # Graphe en courbe de W0
    plt.subplot(nb_graph, 1, 7)
    plt.ylim(0.0,1.0)
    plt.ylabel('W0')
    plt.plot(x, w0,'k')
    
    plt.subplots_adjust(top=1.5)
    plt.show()
