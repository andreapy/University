import numpy as np
import matplotlib.pyplot as plt


e= 1.602E-19
per= 8.988E9
en= 1.602E-13
rep= 938.28*en
egamma= 84*en 
egamma1=141*en
egamma2= 208*en
egamma3=364*en
egamma4=511*en
egamma5=662*en
egamma6=1332*en

cot= 1/np.tan(np.radians(5))
sum= 1 + (egamma/rep)
#theta= 2*np.arctan(cot/sum) 

rp= (e**2 *per)/rep
rcl= rp*rp

r=np.arange(0,1,0.01)
theta = 2*np.pi*r

f= (rcl/2)* 1/((1+ (egamma/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma/rep)*(1- np.cos(theta)))))

g=(rcl/2)* 1/((1+ (egamma1/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma1/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma1/rep)*(1- np.cos(theta)))))
h=(rcl/2)* 1/((1+ (egamma2/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma2/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma2/rep)*(1- np.cos(theta)))))
i=(rcl/2)* 1/((1+ (egamma3/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma3/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma3/rep)*(1- np.cos(theta)))))

j=(rcl/2)* 1/((1+ (egamma4/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma4/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma4/rep)*(1- np.cos(theta)))))

k=(rcl/2)* 1/((1+ (egamma5/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma5/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma5/rep)*(1- np.cos(theta)))))

l=(rcl/2)* 1/((1+ (egamma6/rep)*(1 - np.cos(theta)))**2)*(1 + (np.cos(theta))**2
+(((egamma6/rep)**2 * (1 - np.cos(theta))**2))/(1 + ((egamma6/rep)*(1- np.cos(theta)))))

fig= plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, f,label='84 keV')
ax.plot(theta, g,label='141 keV')
ax.plot(theta, h,label='208 keV')
ax.plot(theta, i,label='364 keV')
ax.plot(theta, j,label='511 keV')
ax.plot(theta, k,label='662 keV')
ax.plot(theta, l,label='1332 keV')

ax.legend(bbox_to_anchor=(0,0,1,1), bbox_transform=fig.transFigure)
#ax.legend(loc='lower left')
#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
ax.set_thetagrids(angles=[0, 45, 90, 135, 180, 225, 270,
                          315],
                  labels=list(map(lambda x: str(x)
                                  + u'\N{DEGREE SIGN}',
                                  [0, 45, 90, 135, 180, -135,-90,-45])))
#plt.thetagrids([0, 45, 90, 135, 180, 225, 270, 315],labels=['$0^{\circ}$','$45^{\circ}$','$90^{\circ}$','$135^{\cir\c}$','$180^{\circ}$','$-135^{\circ}$','$-90^{\circ}$','$-45^{\circ}$'])

#ax.set_title("A line plot on a polar axis", va='bottom')
plt.savefig('KNpolar.pdf')
plt.show()

#plt.polar(theta, f, label= '1 MeV')
#plt.polar(theta, g,'r', label= '10 MeV')
#plt.polar(theta, h,'m', label= '100 MeV')
#plt.polar(theta, i,'g', label= '1000 MeV')
#plt.legend()
#plt.thetagrids([0, -45, -90, -135, 180, 135, 90, 45],labels=['$0^{\circ}$','$-45^{\circ}$','$-90^{\circ}$','$-135^{\circ}$','$180^{\circ}$','$135^{\circ}$','$90^{\circ}$','$45^{\circ}$'])
 



