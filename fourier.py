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
f=np.sin(2*np.pi*freq*t)
f=signal.square(2 * np.pi * freq * t)
p=transform(f)
p=[j for j in p if j>0]#no negative frequencies
fig,(ax1,ax2,ax3,ax4)=plt.subplots(1,4)
ax1.plot(f)#input signal
ax2.scatter(np.exp(-2*np.pi*1j*t).real,np.exp(-2*np.pi*1j*t).imag)#exponential
ax3.scatter(np.real(p),np.imag(p))#transform's plot in coordinate system. Don't know why it seems weird.
ax4.plot(p)#output

plt.show()




