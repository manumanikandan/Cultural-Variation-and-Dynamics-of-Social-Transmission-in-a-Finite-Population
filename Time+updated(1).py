
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[2]:

def pi(i,n,lam):
    ngamma, dgamma = [1], [1]
    fpnum, fpden = 1.0, 1.0
    for k in range(1,n):
        pi = lam*(k/n)*((n-k)/n) + (1-lam)*(n-k)/n*(n-k)/n
        ip = lam*((n-k)/n)*(k/n) + (1-lam)*(k/n)*(k/n)
        gam = ip/pi
        fpden = fpden*gam
        dgamma += [fpden]
        if k < i:
            fpnum = fpnum*gam
            ngamma += [fpnum]
    fp = sum(ngamma)/sum(dgamma)
    return fp


# In[10]:

pi(1,10,0,0.6,.4)


# In[4]:

def time(i,j,n,lam):
    ngamma1, ngamma, ngammaj = 1., 1., 1.
    aj, bj = 1., 1.
    num1, num2 = [1], [1]
    for k in range(1,n):
        a = lam*(k/n)*((n-k)/n) + (1-lam)*(n-k)/n*(n-k)/n
        b = lam*((n-k)/n)*(k/n) + (1-lam)*(k/n)*(k/n)
        gam = b/a
        if k < j:
            ngamma = ngamma*gam
            ngamma1 = ngamma1*gam
            num1 += [ngamma]
        elif k == j:
            aj = aj*a
            bj = bj*b
            ngamma = ngamma*gam
            ngammaj = ngammaj*ngamma
            #num2 += [ngamma]
        elif k > j:
            ngamma = ngamma*gam
            num2 += [ngamma]
    t1 = ((1-pi(i,n,lam))*sum(num1))/(ngamma1*bj)
    t2 = ((pi(i,n,lam))*sum(num2))/(ngammaj*aj)
    
    if j <= i:
        
        return (t1)
    else:
        return (t2)
    



# In[5]:

time(25,24,40,0,0.5,0.5)


# In[6]:

def meabs(i,n,lam):
    l1=[0]
    #l = []
    for j in range(1,n):
        l1 += [time(i,j,n,lam)]
    
    return (sum(l1) / float(len(l1)))


# In[16]:

meabs(49,50,0,0.3,0.7)


# In[11]:

def ti_star(i,n,lam,p,q):
    lt_star = [0]
    for j in range(1,n):
        tij = time(i,j,n,lam,p,q)*(pi(j,n,lam,p,q)/pi(i,n,lam,p,q))
        lt_star += [tij] 
    print (sum(lt_star) / float(len(lt_star)))


# In[17]:




# In[40]:


i = 1
n =50
lout = []
for lam in np.arange(0,1,.01):
    lout += [meabs(i,n,lam)]
plt.plot(np.arange(0.,1,.01),lout,label='p=0.5;q = 0.5')
plt.xlabel('λ')
plt.ylabel('Mean absorption time')
plt.title('X₀= 1; N= 50')
plt.legend(loc='upper right')
#plt.show()
plt.savefig('meabs1.png', bbox_inches='tight')

# In[31]:

out=at(1,50,0.6,0.4)
out1=at(1,50,0.5,0.5)
#out2=at(1,50,0.6,0.4)
plt.plot(np.arange(0.,1,.01),out,'red',label='p=0.3;q = 0.7')
plt.plot(np.arange(0.,1,.01),out1,'blue',label='p=0.5;q=0.5')
#plt.plot(np.arange(0.,1,.01),out2,'green',label='p=0.7;q=0.3')
plt.xlabel('λ')
plt.ylabel('Mean absorption time')
plt.title('X₀= 1; N= 50')
plt.legend(loc='lower right')
plt.show()


# In[27]:

def meafix(i,n,lam,p,q):
    l1=[0]
    #l = []
    for j in range(1,n):
        l1 += [ti_star(j,n,lam,p,q)]
    
    return (sum(l1) / float(len(l1))) 


# meafix(1,50,1,0.5,0.5)

# In[28]:

meafix(1,50,0,0.6,0.4)


# In[212]:

lam = 0
p = 0.5
q = 0.5
n = 10
lout = []
for i in range(1,n):
    lout += [meabs(i,n,lam,p,q)]
plt.plot(range(1,n),lout)
#plt.title('fp for p ='+str(p)+' and q ='+str(q))
print (lout)
plt.show()


# In[ ]:



