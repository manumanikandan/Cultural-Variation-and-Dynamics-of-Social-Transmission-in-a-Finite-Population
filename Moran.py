
# coding: utf-8

# In[6]:

import numpy as np
import matplotlib.pyplot as plt


# In[7]:

def pi(i,n,lam,p,q,z):
    ngamma, dgamma = [1], [1]
    fpnum, fpden = 1.0, 1.0
    for k in range(1,n):
        y = np.random.hypergeometric(i,n-i,z)
        pi = lam*(y/z)*((n-k)/n) + (1-lam)*(p)*(n-k)/n
        ip = lam*((z-y)/z)*(k/n) + (1-lam)*(q)*(k/n)
        gam = ip/pi
        fpden = fpden*gam
        dgamma += [fpden]
        if k < i:
            fpnum = fpnum*gam
            ngamma += [fpnum]
    x=sum(ngamma)
    y=sum(dgamma)
    fp = x/y
    #print (ngamma)
    #print (x)
    #print (dgamma)
    #print (y)
    return fp


# In[5]:

pi(1,100,0,0.2,0.8)


# In[9]:

lz = []
i =2500
n = 50
lam = 0.8
lq = np.arange(0,1.0,0.01)
lp = np.arange(0,1.0,0.1)
for p in lp:
    l = []
    for q in lq:
        l += [pi(i,n,lam,p,q)]
    lz += [l]

for p in range(len(lz)):
    plt.plot(lq,lz[p])
plt.xlabel('q')
plt.ylabel('fp')
plt.title('fp for gamma ='+str(lam))
plt.show()


# In[47]:

def fp(i,n,p,q):
    lout = []
    for lam in np.arange(0,1,.01):
        lout += [round(pi(i,n,lam,p,q),2)]
    return lout    
#plt.plot(np.arange(0.,1,.01),lout)
#plt.xlabel('λ')
#plt.ylabel('Fixation probability')
#plt.title('p = 0.5; q = 0.5; X₀= 1; N= 50')
#print (lout)
#plt.show()


# In[58]:

out=fp(200,500,0.2,0.8)
out1=fp(200,500,0.5,0.5)
out2=fp(200,500,0.8,0.2)
plt.plot(np.arange(0.,1,.01),out,'red',label='p=0.2;q = 0.8')
plt.plot(np.arange(0.,1,.01),out1,'blue',label='p=0.5;q=0.5')
plt.plot(np.arange(0.,1,.01),out2,'green',label='p=0.8;q=0.2')
plt.xlabel('λ')
plt.ylabel('Fixation probability')
plt.title('X₀= 250; N= 500')
plt.legend(loc='lower right')
plt.show()


# In[13]:

lz = []
i = 40
n = 50
lam = 0.2
lp = np.arange(0,1.0,0.1)
lq = np.arange(0,1.0,0.01)
for p in lp:
    l = []
    for q in lq:
        l += [pi(i,n,lam,p,q)]
    lz += [l]

for p in range(len(lz)):
    plt.plot(lq,lz[p])
plt.xlabel('q')
plt.ylabel('fp')
plt.title('fp for lambda ='+str(lam))
plt.show()


# In[240]:

fp(1,100,0.2,0.8)


# In[239]:

pi(1,100,0.01,0.2,0.8)


# In[ ]:




# In[ ]:



