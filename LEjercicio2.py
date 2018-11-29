print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 3 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib.pylab as plt

u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

mu=np.mean(u)
mv=np.mean(v)

def cov(u,v):
	for i in range(len(u)):	
		return (1/(len(u)-1.0))*np.sum((u[i]-mu)*(v[i]-mv))

print 'La covarianza entre u y v tiene un valor de= ',cov(u,v)

