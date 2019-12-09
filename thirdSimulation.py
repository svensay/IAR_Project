# -*- coding: utf-8 -*-

import numpy as np
import Amygdala as am
import CortexOrbitoFrontal as cof
import matplotlib.pyplot as plt

if __name__ == "__main__":
 
    nb_graph = 6 # nombre de graphe
    x_range = 36 # nombre de pas de temps
    gap = 6
    
    th = np.array([]) # Stimulus du Thalamus
    s0 = np.array([]) # 1er stimulus du Cortex Sensible (Sensory Cortex)
    s1 = np.array([]) # 2eme stimulus du Cortex Sensible (Sensory Cortex)
    s2 = np.array([]) # 3eme stimulus du Cortex Sensible (Sensory Cortex)
    rew = np.array([]) # Récompense
    
    #Initialisation
    for i in range(x_range):
        """
        if(i % gap1 == 0 and i < 210):
            th = np.append(th,1)
        else:
            th = np.append(th,0)
         """
        th = np.append(th,1)
         
        #if((i >= 60 and i < 160) and (i % gap1 == 0)):
        if((i >= 10 and i <= 25) ):
            s0 = np.append(s0,1)
        else:
            s0 = np.append(s0,0)
    
        #if( ((i >= 70 and i < 160) and i % gap2 == 0 ) or ((i >= 160 and i <= 180) and i % gap1 == 0 )):
        if( ((i >= 11 and i <= 25) and i % 2 == 1 ) or ((i >= 26 and i <= 30))):
            s1 = np.append(s1,1)
        else:
            s1 = np.append(s1,0)
        
        #if( ((i >= 0 and i < 60) or (i > 160 and i <= 210)) and i % gap1 == 0 ):
        if( ((i >= 0 and i <= 9) or (i >= 26 and i <= 36))):
            s2 = np.append(s2,1)
        else:
            s2 = np.append(s2,0)
        
        #if((i >= 0 and i < 60 and i % gap1 == 0) or ((i >= 60 and i < 150 and i % gap2 == 0))):
        if((i >= 0 and i <= 10) or ((i >= 12 and i <= 24 and i % 2 == 0))):
            rew = np.append(rew,1)
        else:
            rew = np.append(rew,0)
            
        for i in range(gap-1):
            th = np.append(th,0)
            s0 = np.append(s0,0)
            s1 = np.append(s1,0)
            s2 = np.append(s2,0)
            rew = np.append(rew,0)
            
    amygdale = am.Amygdala(np.array([0,0,0]),np.array([0]),np.array([0]))
    cortexorbitofrontal = cof.CortexOrbitoFrontal(np.array([0,0,0]),np.array([0]))
        
    E = np.array([]) # Tableaux des E
    
    eValue = amygdale.calcul_E(cortexorbitofrontal.O)
    
    for i in range(0,x_range*gap,gap):
            
        # Calcul d'un pas de temps
        amygdale.pas_de_temps(np.array([s0[i],s1[i],s2[i]]),np.array([th[i]]),np.array([rew[i]]))
        
        #cortexorbitofrontal.maj_E(eValue)
        
        cortexorbitofrontal.pas_de_temps(np.array([s0[i],s1[i],s2[i]]),np.array([rew[i]]))
                
        

        print("\t i -> ",i)
        print("details de A -> ",amygdale.A)
        print("details de V -> ",amygdale.V)
        print("A = ", np.sum(amygdale.A))
        print("details de O -> ", cortexorbitofrontal.O)
        print("details de W -> ",cortexorbitofrontal.W)
        # Calcult de la valeur de E
        eValue = amygdale.calcul_E(cortexorbitofrontal.O)
        #print("O = ", np.sum(cortexorbitofrontal.O))
        print("E = ", eValue)

        cortexorbitofrontal.maj_E(eValue)
        
        # Ajout dans les tableaux leurs valeurs respectif
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
    
    # Graphe en bar de S2
    plt.subplot(nb_graph, 1, 4)
    plt.ylabel('S2')
    plt.xticks([])
    plt.bar(x,s2,color=['black'])
    
    # Graphe en courbe de E
    plt.subplot(nb_graph, 1, 5)
    plt.ylabel('E')
    plt.xticks([])
    plt.plot(x,E,'k')
    
    # Graphe en bar de Rew
    plt.subplot(nb_graph, 1, 6)
    plt.ylabel('Rew')
    plt.bar(x,rew,color=['black'])

    plt.subplots_adjust(top=1.5)
    plt.show()
