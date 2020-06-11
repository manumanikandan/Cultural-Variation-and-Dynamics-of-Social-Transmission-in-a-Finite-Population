
# coding: utf-8

# In[64]:

import numpy as np
import matplotlib.pyplot as plt


# In[65]:

def pi(i,n,lam,p,q):
    ngamma, dgamma = [1], [1]
    fpnum, fpden = 1.0, 1.0
    for k in range(1,n):
        z = np.random.randint(2,n+1)
        y = np.random.hypergeometric(i,n-i,z)
        pi = lam*(y/z)*((n-k)/n) + (1-lam)*(p)*(n-k)/n
        ip = lam*((z-y)/z)*(k/n) + (1-lam)*(q)*(k/n)
        gam = ip/pi
        fpden = fpden*gam
        dgamma += [fpden]
        if k < i:
            fpnum = fpnum*gam
            ngamma += [fpnum]
    fp = sum(ngamma)/sum(dgamma)
    return fp


# In[66]:

pi(1,10,0,0.8,.2)


# In[67]:

def time(i,j,n,lam,p,q):
    ngamma1, ngamma, ngammaj = 1., 1., 1.
    aj, bj = 1., 1.
    num1, num2 = [1], [1]
    for k in range(1,n):
        z = np.random.randint(2,n+1)
        y = np.random.hypergeometric(i,n-i,z)
        a = lam*(y/z)*((n-k)/n) + (1-lam)*(p)*(n-k)/n
        b = lam*((z-y)/z)*(k/n) + (1-lam)*(q)*(k/n)
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
    t1 = ((1-pi(i,n,lam,p,q))*sum(num1))/(ngamma1*bj)
    t2 = ((pi(i,n,lam,p,q))*sum(num2))/(ngammaj*aj)
    
    if j <= i:
        
        return (t1)
    else:
        return (t2)
    



# In[68]:




# In[70]:

def meabs(i,n,lam,p,q):
    l1=[0]
    #l = []
    for j in range(1,n):
        l1 += [time(i,j,n,lam,p,q)]
    
    return (sum(l1) / float(len(l1)))


# In[ ]:


# In[80]:

meabs(1,100,0,0.2,0.8)


# In[88]:

def ti_star(i,n,lam,p,q):
    lt_star = [0]
    for j in range(1,n):
        tij = time(i,j,n,lam,p,q)*(pi(j,n,lam,p,q)/pi(i,n,lam,p,q))
        lt_star += [tij] 
    return sum(lt_star) / float(len(lt_star))


# In[89]:

ti_star(5,10,0.5,0.5,0.5)


# In[86]:

p = 0.8
q = 0.2
i = 1
n =100
lout = []
for lam in np.arange(0,1,.01):
    lout += [meabs(i,n,lam,p,q)]
plt.plot(np.arange(0.,1,.01),lout,label='p=0.8;q = 0.2')
plt.xlabel('λ')
plt.ylabel('Mean absorption time')
plt.legend(loc='upper right')
plt.show()


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


# In[90]:

def meafix(i,n,lam,p,q):
    l1=[0]
    #l = []
    for j in range(1,n):
        l1 += [ti_star(j,n,lam,p,q)]
    
    print (sum(l1) / float(len(l1))) 


# meafix(1,50,1,0.5,0.5)

# In[92]:

meafix(99,100,0,0.8,0.2)


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


# In[75]:

def Markov2(i,n,lam,N):
    lout = []
    t = [] 
    X = []
    k = 0
    for k in range(N):
        p  = np.random.uniform(0,1)
        q  = 1 - p
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
        #k = k + 1
        lout += [meabs(i,n,lam,p,q)]
    #print (X)
    #print (X.T)
    return k, lout

    #plt.plot(range(0,k),t)
    #plt.xlabel('No. of generation')
    #plt.ylabel('State')
    #plt.title('(24,25,0.7,0.2,.8)')
    #plt.show()


# In[76]:

out=Markov2(20,50,0.5,500)


# print(out[1])

# In[77]:

plt.plot(range(500),out[1])
plt.show()


# In[62]:

print(out[1][-1])


# In[ ]:



