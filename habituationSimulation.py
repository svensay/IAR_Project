# -*- coding: utf-8 -*-

import numpy as np
import Amygdala as am
import CortexOrbitoFrontal as cof
import matplotlib.pyplot as plt

if __name__ == "__main__":
 
    nb_graph = 2 # nombre de graphe
    x_range = 23 # nombre de pas de temps
    gap = 5 # écart entre les valeurs
    
    th = np.zeros((x_range*gap,), dtype=int) # Stimulus du Thalamus
    s = np.array([]) # Stimulus du Cortex Sensible (Sensory Cortex)
    rew = np.array([]) # Récompense
    
    #Initialisation
    for i in range(x_range):
        s = np.append(s,1)
        
        if(i == 0):
            rew = np.append(rew,1)
        else:
            rew = np.append(rew,0)
        for i in range(gap-1):
            s = np.append(s,0)
            rew = np.append(rew,0)
            
    amygdale = am.Amygdala(np.array([0]),np.array([0]),np.array([0]))
    cortexorbitofrontal = cof.CortexOrbitoFrontal(np.array([0]),np.array([0]))
        
    E = np.array([]) # Tableaux des E
    
    eValue = amygdale.calcul_E(cortexorbitofrontal.O)
    
    for i in range(0,x_range*gap,gap):
            
        # Calcul d'un pas de temps
        amygdale.pas_de_temps(np.array([s[i]]),np.array([th[i]]),np.array([rew[i]]))
        cortexorbitofrontal.maj_E(eValue)
        cortexorbitofrontal.pas_de_temps(np.array([s[i]]),np.array([rew[i]]))

        # Calcult de la valeur de E
        eValue = amygdale.calcul_E(cortexorbitofrontal.O)
        E = np.append(E,eValue)
        # Ajout dans le tableau + gap
        for i in range(gap-1):
            E = np.append(E,0)

    # Axes de x
    x = np.arange(0,x_range*gap)
    
    # Graphe en bar de CS
    plt.subplot(nb_graph, 1, 1)
    plt.ylabel('CS')
    plt.xticks([])
    plt.bar(x,s,color=['black'])
    
    # Graphe en courbe de E
    plt.subplot(nb_graph, 1, 2)
    plt.ylabel('E')
    plt.bar(x,E,color=['black'])


    plt.subplots_adjust(top=1.5)
    plt.show()
