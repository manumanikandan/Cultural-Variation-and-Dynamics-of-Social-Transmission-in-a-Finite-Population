
# coding: utf-8

# In[55]:

import numpy as np
import math
import matplotlib.pyplot as plt


# In[ ]:

def Markov(i,n,lam,p,q,N):
    t = [] 
    X = []
    Z = []
    for j in range(0,N):
        k = np.random.randint(2,n+1)
        y = np.random.hypergeometric(i,n-i,k)
        pi = lam*(y/k)*((n-i)/n) + (1-lam)*p*((n-i)/n)
        ip = lam*((k-y)/k)*(i/n) + (1-lam)*q*(i/n)
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
        X.append(k)
        Z.append(y)
    #print (X)
    #print (Z)
    #print (X.T)
    return (t)

    plt.plot(range(0,N),t)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.title('(24,25,0.7,0.2,.8)')
    plt.show()


# In[ ]:

Markov(1,500,0,0.8,0.2,1000000)


# In[57]:

def Markov1(i,n,lam):
    t = [] 
    X = []
    k = 0
    while i < n and i != 0:
        p  = np.random.uniform(0,1)
        q  = 1-p
        pi = lam*(i/n)*((n-i)/n) + (1-lam)*p*((n-i)/n)
        ip = lam*((n-i)/n)*(i/n) + (1-lam)*q*(i/n)
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
        X.append(lam)
        k = k + 1
    #print (X)
    #print (X.T)
    return k, lam

    #plt.plot(range(0,k),t)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.title('(24,25,0.7,0.2,.8)')
    #plt.show()


# In[ ]:

Markov1(10,50,0.5)


# In[ ]:

l =[]
for i in range(0,1000):
    l.append(Markov1(40,50,0.5)[0])
print(np.average(l))    


# In[104]:

out = Markov(499,1000,0.5,0.8,0.2,100000)
out1 = Markov(1,1000,0.5,0.5,0.5,100000)
out2= Markov(999,1000,0.5,0.2,0.8,100000)

plt.plot(range(0,100000),out,'red',label='p=0.9;q = 0.6')
plt.plot(range(0,100000),out1,'blue',label='p=0.4;q=0.5')
plt.plot(range(0,100000),out2,'green',label='p=0.3;q=0.8')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.legend(loc='lower right')
#plt.savefig('lam05')
plt.show()


# In[36]:

def chain(c,n,lam,p,q,t):
    l=[]
    for i in range(0,t):
        x = ((p*n)/(p+q)) + c*math.exp(-((1-lam)*(p+q)*(i/n)))
        l.append(x)
    return l    
    plt.plot(range(0,t),l)
    plt.xlabel('No. of generation')
    plt.ylabel('State')
    plt.show()


# In[42]:

out1 = Markov(1,1000,0.8,0.8,0.2,1000000)
out2 = chain(-799,1000,0.8,0.8,0.2,1000000)
out3 = Markov(999,1000,0.8,0.2,0.8,1000000)
out4 = chain(799,1000,0.8,0.2,0.8,1000000)
plt.plot(range(0,1000000),out1,'blue',label='p=0.8;q = 0.2')
plt.plot(range(0,1000000),out2,'red',)
plt.plot(range(0,1000000),out3,'grey',label='p=0.2;q = 0.8')
plt.plot(range(0,1000000),out4,'green')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.legend(loc='lower right')
#plt.savefig('confstoch08.png')
plt.show()

# In[ ]:



