import numpy as np
import matplotlib.pyplot as plt

#Grafico para coeficientes másicos de atenuacion con la base da datos de XCOM 
#Material: Argon (Z=18)

#-----------------------------------
#DATA FROM XCOM DATABASE (NIST)

#ALUMINIUM 
#Densidad  2.70 g/cm^3
'''
Al= np.genfromtxt('xcomAl.txt')
E = Al[:,0]

AlCom = Al[:,1]
AlPh = Al[:,2]
AlT = Al[:,3]
'''
#Soft Tissue 4 Components
#Densidad 1.00 g/cm^3
'''
St = np.genfromtxt('xcomST.txt')
E = St[:,0]


StCom = St[:,1]
StPh = St[:,2]
StT = St[:,3]
'''

#Argon 
##Densidad 

Bo = np.genfromtxt('ArgonXCOM.txt')

E = Bo[:,0]

BoCom = Bo[:,2]
BoPh = Bo[:,3]
BoPP=Bo[:,4]
BoT = Bo[:,7]







#----------------------------------


plt.loglog(E,BoCom,'r',label= r'Compton')
plt.loglog(E,BoPh,'b',label=r'Fotoeléctrico')
plt.loglog(E,BoPP, label='Producción de Pares')
plt.loglog(E,BoT,'g', label='Total')

plt.legend()

plt.xlabel(r'Energía (MeV)')
plt.ylabel(r'$\mu/\rho$ ($cm^{2}/g$)')
#plt.axis([0.001,2.1,0.000008,10000])
#plt.grid(True)

plt.text(0.4,1,'Argón',color='black', fontsize=14)

plt.savefig('Argon.pdf')
plt.show()

