
# coding: utf-8

# In[81]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from random import seed
from random import randint


# In[82]:

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


# In[103]:

hypergeom_pmf(100,50,10,4)


# In[115]:

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
        print (np.sum([hypergeom_pmf(N, A, n, x) for x in range(min_value, t+1)]))
    
    print (np.sum([hypergeom_pmf(N, A, n, x) for x in range(t+1)]))


# In[116]:

hypergeom_cdf(100,50,10,4)


# In[117]:

def chain(i,n,N):
    t=[]
    l=[]
    for k in range(0,N):
        seed(k)
        x=randint(2,n)
        y = np.random.uniform(0,1)
        if (x % 2) == 0:
            pi= ((1 - hypergeom_cdf(n,i,x,(x/2))) + ((hypergeom_pmf(n,i,x,x/2))/2))*((n-i)/n)
            ip= ((hypergeom_cdf(n,i,x,(x/2))) + ((hypergeom_pmf(n,i,x,x/2))/2))*(i/n)
            if pi!=0 and ip!=0:
                if  y <= pi and pi !=0:
                    i=i+1
                elif pi <x<= ip+pi and ip != 1:
                    i=i-1
                else:
                    i=i
            else:
                i=i
        else:
            pi= ((1 - hypergeom_cdf(n,i,x,((x-1)/2))))*((n-i)/n)
            ip= ((hypergeom_cdf(n,i,x,((x-1)/2))))*(i/n)
            if pi!=0 and ip!=0:
                if  y <= pi and pi !=0:
                    i=i+1
                elif pi <x<= ip+pi and ip != 1:
                    i=i-1
                else:
                    i=i
            else:
                i=i
        l.append(x)        
        t.append(i) 
    print(l)    
    #print (t)


# In[118]:

chain(10,50,20)


# In[112]:

seed(1)
randint(1,100)


# In[107]:

seed(1)
randint(1,100)


# In[ ]:



