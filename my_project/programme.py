# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 08:41:37 2017

@author: Robin
"""
import os
from matplotlib import pyplot as plt
import numpy as np

os.chdir("C:/Users/USER/Desktop/projet_theorie_erreurs/my_project")

M = np.loadtxt('data/QI12_donnee.dat')
col0 = M[:,0]
col1 = M[:,1]
col2 = M[:,2]
col3 = M[:,3]

for e in range(10):
    plt.plot(range(100), col1[100*e:100*e+100], 'x', label = "algorithme de compression 1")
    plt.plot(range(100), col2[100*e:100*e+100], 'x', label = "algorithme de compression 2")
    plt.plot(range(100), col3[100*e:100*e+100], 'x', label = "algorithme de compression 3")
    
    plt.legend(loc='upper left', frameon=False)

    plt.axis('equal')

    plt.title('Compression d\'un fichier audio de '+str(100*e+100)+ 'ko' + '\nsur 100 echantillons' )
    plt.savefig("plot_data_file"+ str(e) + ".png")

    plt.show()
