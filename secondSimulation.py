# -*- coding: utf-8 -*-

import numpy as np
import Amygdala as am
import CortexOrbitoFrontal as cof
import matplotlib.pyplot as plt

if __name__ == "__main__":
 
    nb_graph = 5 # nombre de graphe
    x_range = 40 # nombre de pas
    gap = 15 # écart entre les valeurs
    
    th = np.array([]) # Stimulus du Thalamus
    s0 = np.array([]) # 1er stimulus du Cortex Sensible (Sensory Cortex)
    s1 = np.array([]) # 2eme stimulus du Cortex Sensible (Sensory Cortex)
    rew = np.array([]) # Récompense
    
    #Initialisation
    for i in range(x_range):
        th = np.append(th,1)
        
        if( ((i >= 0 and i <= 19) or (i >= 30 and i <= 39))):
            s0 = np.append(s0,1)
        else:
            s0 = np.append(s0,0)
    
        if( (i >= 10 and i <= 29)):
            s1 = np.append(s1,1)
        else:
            s1 = np.append(s1,0)
        
        if(i >= 0 and i <= 19):
            rew = np.append(rew,1)
        else:
            rew = np.append(rew,0)
        
        for i in range(gap-1):
            th = np.append(th,0)
            s0 = np.append(s0,0)
            s1 = np.append(s1,0)
            rew = np.append(rew,0)
            
    amygdale = am.Amygdala(np.array([0,0]),np.array([0]),np.array([0]))
    cortexorbitofrontal = cof.CortexOrbitoFrontal(np.array([0,0]),np.array([0]))
        
    E = np.array([]) # Tableaux des E
    
    eValue = amygdale.calcul_E(cortexorbitofrontal.O)
    
    for i in range(0,x_range*gap,gap):
        # Calcul d'un pas de temps
        amygdale.pas_de_temps(np.array([s0[i],s1[i]]),np.array([th[i]]),np.array([rew[i]]))
        cortexorbitofrontal.maj_E(eValue)
        cortexorbitofrontal.pas_de_temps(np.array([s0[i],s1[i]]),np.array([rew[i]]))
                
        # Calcult de la valeur de E
        eValue = amygdale.calcul_E(cortexorbitofrontal.O)
        
        # Ajout dans le tableau + gap
        for i in range(gap):
            E = np.append(E,eValue)
    
    # Axes de x
    x = np.arange(0,x_range*gap)
    
    # Graphe en bar de Th
    plt.subplot(nb_graph, 1, 1)
    plt.ylabel('Th')
    plt.xticks([])
    plt.bar(x,th,color=['black'])
    
    # Graphe en bar de S0
    plt.subplot(nb_graph, 1, 2)
    plt.ylabel('S0')
    plt.xticks([])
    plt.bar(x,s0,color=['black'])
    
    # Graphe en bar de S1
    plt.subplot(nb_graph, 1, 3)
    plt.ylabel('S1')
    plt.xticks([])
    plt.bar(x,s1,color=['black'])
    
    # Graphe en courbe de E
    plt.subplot(nb_graph, 1, 4)
    plt.ylim(0.0,1.2)
    plt.ylabel('E')
    plt.xticks([])
    plt.plot(x,E,'k')
    
    # Graphe en bar de Rew
    plt.subplot(nb_graph, 1, 5)
    plt.ylabel('Rew')
    plt.bar(x,rew,color=['black'])

    plt.subplots_adjust(top=1.5)
    plt.show()
