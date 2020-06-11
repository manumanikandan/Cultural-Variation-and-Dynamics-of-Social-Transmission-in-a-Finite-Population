
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.special import comb
from random import seed
from random import randint
from scipy.stats import hypergeom


# In[2]:

def hypergeom_pmf(N, A, n, x):
    
    '''
    Probability Mass Function for Hypergeometric Distribution
    :param N: population size
    :param A: total number of desired items in N
    :param n: number of draws made from N
    :param x: number of desired items in our draw of n items
    :returns: PMF computed at x
    '''
    Achoosex = comb(A,x)
    NAchoosenx = comb(N-A, n-x)
    Nchoosen = comb(N,n)
    
    return (Achoosex)*(NAchoosenx/Nchoosen)


# In[385]:

def hypergeom_pmf1(N, A, n, x):
    
    '''
    Probability Mass Function for Hypergeometric Distribution
    :param N: population size
    :param A: total number of desired items in N
    :param n: number of draws made from N
    :param x: number of desired items in our draw of n items
    :returns: PMF computed at x
    '''
    Achoosex = comb(A,x)
    NAchoosenx = comb(N-A, n-x)
    Nchoosen = comb(N,n)
    
    return ((Achoosex)*(NAchoosenx/Nchoosen))*x


# In[5]:

hypergeom_pmf(20,10,10,8)


# In[387]:

def hypergeom_cdf(N, A, n, t, min_value=None):
    
    '''
    Cumulative Density Funtion for Hypergeometric Distribution
    :param N: population size
    :param A: total number of desired items in N
    :param n: number of draws made from N
    :param t: number of desired items in our draw of n items up to t
    :returns: CDF computed up to t
    '''
    if min_value:
        return np.sum([hypergeom_pmf(N, A, n, x) for x in range(min_value, t+1)])
    
    return np.sum([hypergeom_pmf(N, A, n, x) for x in range(t+1)])


# In[388]:

hypergeom_pmf(500,100,200,50)


# In[6]:

def chain(i,n,z,N,lam,p,q):
    t=[]
    l1=[]
    l2=[]
    l3=[]
    for k in range(0,N):
        y = np.random.uniform(0,1)
        x = hypergeom.rvs(n,i,z)
        pi= lam*(hypergeom_pmf(n, i, z, x))*(x/z)*((n-i)/n) + (1-lam)*p*((n-i)/n)
        ip= lam*(hypergeom_pmf(n, n-i, z,z-x))*((z-x)/z)*(i/n) + (1-lam)*q*(i/n)
        if i != 0 and i != n:
            if  y <= pi:
                i=i+1
            elif pi <y<= ip+pi:
                i=i-1
            else:
                i=i
        else:
            i=i
        l1.append(pi)  
        l2.append(ip)
        l3.append(y)
        t.append(i) 
    #print(l1)
    #print(l2)
    #print(l3)
    return t
    #plt.plot(range(0,N),t)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.title('(24,25,0.7,0.2,.8)')
    #plt.show()


# In[441]:

chain(10,50,15,1000,0.5,0.7,0.3)


# In[ ]:

out = chain(1,50,6,100000,0.5,0.8,0.2)
out1 = chain(1,50,6,100000,0.5,0.5,0.5)
out2= chain(1,50,6,100000,0.5,0.2,0.8)

plt.plot(range(0,100000),out,'red',label='p=0.8;q = 0.2')
plt.plot(range(0,100000),out1,'blue',label='p=0.5;q=0.5')
plt.plot(range(0,100000),out2,'green',label='p=0.2;q=0.8')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.title('Markov chain when p+q = 1')
plt.legend(loc='lower right')
plt.show()


# In[ ]:

def pi(i,n,lam,p,q):
    ngamma, dgamma = [1], [1]
    fpnum, fpden = 1.0, 1.0
    for k in range(1,n):
        z=np.random.randint(2,n+1)
        if (z // 2) == 0:
            pi= lam*(((1 - hypergeom_cdf(n,k,z,(z//2))) + ((hypergeom_pmf(n,k,z,z//2))/2))*((n-k)/n)) + (1-lam)*p*((n-k)/n)
            ip= lam*(((hypergeom_cdf(n,k,z,(z//2)-1)) + ((hypergeom_pmf(n,k,z,z//2))/2))*(k/n)) + (1-lam)*q*(k/n)
            gam = ip/pi
            fpden = fpden*gam
            dgamma += [fpden]
            if k < i:
                fpnum = fpnum*gam
                ngamma += [fpnum]
        else:
            pi= lam*(((1 - hypergeom_cdf(n,i,z,((z-1)//2))))*((n-i)/n)) + (1-lam)*p*((n-i)/n)
            ip= lam*(((hypergeom_cdf(n,i,z,((z-1)//2))))*(i/n)) + (1-lam)*q*(i/n)
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


# In[ ]:

pi(50,125,1,0.5,0.5)


# In[434]:

def Markov(i,n,lam,p,q,N):
    t = [] 
    X = []

    for k in range(0,N):
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
        X.append(x)
    #print (X)
    #print (X.T)
    #print (t)

    #plt.plot(range(0,N),t)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.title('(24,25,0.7,0.2,.8)')
    #plt.show()


# In[399]:

Markov(1,50,100000,0.5,0.8,0)


# In[403]:

out1 = Markov(1,500,0.2,0.8,0.2,100000)
out2= chain(1,500,6,100000,0.2,0.8,0.2)
out3= chain(1,500,26,100000,0.2,0.8,0.2)
out4= chain(1,500,46,100000,0.2,0.8,0.2)

plt.plot(range(0,100000),out1,'red',label='p=0.5;q = 0.5')
plt.plot(range(0,100000),out2,'blue',label='k=6')
plt.plot(range(0,100000),out3,'green',label='k=26')
plt.plot(range(0,100000),out4,'green',label='k=44')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.title('Markov chain when p+q = 1')
plt.legend(loc='lower right')
plt.show()


# In[8]:

def chain1(c,n,lam,p,q,t):
    l=[]
    for i in range(0,t):
        x = ((p*n)/(p+q)) + c*math.exp(-((1-lam)*(p+q)*i)/n)
        l.append(x)
    return l    
    #plt.plot(np.arange(0,t),l)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.show()


# In[9]:

out1 = chain(100,500,20,100000,0.2,0.7,0.3)
out2 = chain1(-250,500,0.5,0.7,0.3,100000)
out3 = chain(400,500,260,100000,0.2,0.3,0.7)
out4 = chain1(250,500,0.5,0.3,0.7,100000)
plt.plot(np.arange(0,100000),out1,'blue',label='k=20')
plt.plot(np.arange(0,100000),out2,'red',label='p=0.7;q=0.3')
plt.plot(np.arange(0,100000),out3,'grey',label='k=260')
plt.plot(np.arange(0,100000),out4,'green',label='p=0.3;q=0.7')
plt.xlabel('No. of generation')
plt.ylabel('Current state')
plt.title('Markov chain N=500 ')
plt.legend(loc='lower right')
plt.show()


# In[ ]:



