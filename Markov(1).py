
# coding: utf-8

# In[1]:

import numpy as np
import math
import matplotlib.pyplot as plt


# In[9]:

def Markov(i,n,lam,N):
    t = [] 
    X = []

    for k in range(0,N):
        pi = lam*(i/n)*((n-i)/n) + (1-lam)*((n-i)/n)*((n-i)/n)
        ip = lam*((n-i)/n)*(i/n) + (1-lam)*(i/n)*(i/n)
        x = np.random.uniform(0,1)
        if pi!=0 and ip!=0:
            if  x <= pi and pi !=0:
                i=i+1
            elif pi <x<= ip+pi and ip != 1:
                i=i-1
            else:
                i=i
        else:
            i=i
        t.append(i) 
        X.append(x)
    #print (X)
    #print (X.T)
    return t

    plt.plot(range(0,N),t)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.title('(24,25,0.7,0.2,.8)')
    plt.show()


# In[11]:

Markov(100,500,0.5,0.8,.2,100000)


# In[14]:

out = Markov(1,1000,0,0.9,0.9,100000)
out1 = Markov(1,1000,0,0.6,0.3,100000)
out2= Markov(1,1000,0,0.3,0.9,100000)

plt.plot(range(0,100000),out,'red',label='p=0.9;q = 0.9')
plt.plot(range(0,100000),out1,'blue',label='p=0.6;q=0.3')
plt.plot(range(0,100000),out2,'green',label='p=0.3;q=0.9')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.title('Markov chain when p+q ≠ 1')
plt.legend(loc='lower right')
plt.show()


# In[12]:

def chain(c,n,lam,t):
    l=[]
    for i in range(0,t):
        x = (n)/(2) + c*math.exp(-((1-lam)*2*i))
        l.append(x)
    return l    
    plt.plot(range(0,t),l)
    plt.xlabel('No. of generation')
    plt.ylabel('State')
    plt.show()


# In[13]:

out1 = Markov(1,1000,0,100000)
out2 = chain(-499,1000,0,100000)
out3 = Markov(999,1000,0,100000)
out4 = chain(499,1000,0,100000)
plt.plot(range(0,100000),out1,'blue',label='i=1;n = 1000')
plt.plot(range(0,100000),out2,'red')
plt.plot(range(0,100000),out3,'grey',label='i=999;n = 1000')
plt.plot(range(0,100000),out4,'green')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.title('Markov chain ')
plt.legend(loc='lower right')
#plt.show()
plt.savefig('stoch0.png', bbox_inches='tight')

# In[ ]:



