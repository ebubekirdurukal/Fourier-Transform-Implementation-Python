import numpy as np
import cmath
import matplotlib.pyplot as plt
from scipy import signal

def transform(x):
	y=[]
	for r in range(500):
		m=complex(0)
		for t in range(len(x)):
			m+=x[t]*np.exp(-2*np.pi*1j*t*r/len(x))
		y.append(m)
	return y
t=np.linspace(0,1,1000)#sampled at 1000 Hz
freq=10
f=np.sin(2*np.pi*5*t)+5*np.sin(2*np.pi*10*t)+np.sin(2*np.pi*15*t)+9*np.sin(2*np.pi*20*t)
p=transform(f)
p=[j for j in p if j>0]#no negative frequencies
fig,(ax1,ax2)=plt.subplots(1,2)

ax1.plot(f,color='red')#input signal
ax1.set(xlabel='zaman', ylabel='Büyüklük')
ax1.title.set_text('Girdi Sinyali')
ax1.grid()
ax2.plot(p)#output
ax2.set(xlabel='frekans')
ax2.set_label('Fourier Dönüşümü')
ax2.title.set_text('Fourier Dönüşümü')
ax2.grid()
plt.show()
