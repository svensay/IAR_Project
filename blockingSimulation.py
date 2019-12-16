# -*- coding: utf-8 -*-

import numpy as np
import Amygdala as am
import CortexOrbitoFrontal as cof
import matplotlib.pyplot as plt

if __name__ == "__main__":
 
    nb_graph = 4 # nombre de graphe
    x_range = 81 # nombre de pas de temps
    gap = 1 # écart entre les valeurs
    
    th = np.ones((x_range*gap,), dtype=int) # Stimulus du Thalamus
    s0 = np.array([]) # 1er stimulus du Cortex Sensible (Sensory Cortex)
    s1 = np.array([]) # 2eme stimulus du Cortex Sensible (Sensory Cortex)
    rew = np.array([]) # Récompense
    
    #Initialisation
    for i in range(x_range):
        if(i <= 39 or (i >= 59 and i <= 81)):
            s0 = np.append(s0,1)
        else:
            s0 = np.append(s0,0)
        
        if(i >= 19 and i <= 59):
            s1 = np.append(s1,1)
        else:
            s1 = np.append(s1,0)
        
        if(i <= 39):
            rew = np.append(rew,1)
        else:
            rew = np.append(rew,0)
            
        for i in range(gap-1):
            s0 = np.append(s0,0)
            s1 = np.append(s1,0)
            rew = np.append(rew,0)
            
          
    amygdale = am.Amygdala(np.array([1,0]),np.array([1]),np.array([1]),thal=True)
    cortexorbitofrontal = cof.CortexOrbitoFrontal(np.array([0,0]),np.array([0]))
        
    E = np.array([]) # Tableaux des E
    
    eValue = amygdale.calcul_E(cortexorbitofrontal.O)
    
    for i in range(0,x_range*gap,gap):
            
       # Calcul d'un pas de temps
        amygdale.pas_de_temps(np.array([s0[i],s1[i]]),np.array([th[i]]),np.array([rew[i]]),alpha=0.15,thal=True)
        cortexorbitofrontal.maj_E(eValue)
        cortexorbitofrontal.pas_de_temps(np.array([s0[i],s1[i]]),np.array([rew[i]]),beta=0.25)

        # Calcul de la valeur de E
        eValue = amygdale.calcul_E(cortexorbitofrontal.O)
        E = np.append(E,eValue)
        
        # Ajout dans le tableau + gap
        for i in range(gap-1):
            E = np.append(E,0)

    # Axes de x
    x = np.arange(0,x_range*gap)
    
    # Graphe en bar de CS1
    plt.subplot(nb_graph, 1, 1)
    plt.ylabel('CS1')
    plt.xticks([])
    plt.bar(x,s0,color=['black'])
    
    # Graphe en bar de CS2
    plt.subplot(nb_graph, 1, 2)
    plt.ylabel('CS2')
    plt.xticks([])
    plt.bar(x,s1,color=['black'])
    
    # Graphe en bar de US
    plt.subplot(nb_graph, 1, 3)
    plt.ylabel('US')
    plt.xticks([])
    plt.bar(x,rew,color=['black'])
    
    # Graphe en courbe de E
    plt.subplot(nb_graph, 1, 4)
    plt.ylabel('E')
    plt.bar(x,E,color=['black'])


    plt.subplots_adjust(top=1.5)
    plt.show()
