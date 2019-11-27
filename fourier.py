#Fourier Transform Implementation
#Ebubekir Durukal January 17th 2019
#References:
#https://www.nayuki.io/page/how-to-implement-the-discrete-fourier-transform
#https://www.youtube.com/watch?v=spUNpyF58BY&t=442s

import numpy as np
import cmath
import matplotlib.pyplot as plt
from scipy import signal

def transform(x):
	y=[]
	for r in range(500):#when range of output is large , it takes weird values 
		m=complex(0)
		for t in range(len(x)):
			m+=x[t]*np.exp(-2*np.pi*1j*t*r/len(x))
		y.append(m)
	return y
t=np.linspace(0,1,1000)#sampled at 1000 Hz
freq=10
f=np.sin(2*np.pi*freq*t)+5*np.sin(2*np.pi*20*t)+np.sin(2*np.pi*25*t)+np.cos(2*np.pi*5*t)+np.cos(2*np.pi*15*t)
p=transform(f)
p=[j for j in p if j>0]#no negative frequencies
fig,(ax1,ax2)=plt.subplots(1,2)
ax1.plot(f)#input signal
ax2.plot(p)#output
plt.show()




