
# coding: utf-8

# In[20]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# $f(x)=\frac{e^x-e^-x}{e^x+e^-x}$

# In[140]:

x = np.linspace(-5, 5)
e = np.e


# In[147]:

def f(x, e):
    return ((e ** x)-(e ** -x))/((e ** x)+(e ** -x))


# In[148]:

plt.plot(x, f(x, e), 'c')
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.grid(True)
plt.title("GRAFICA TANGENTE HIPERBOLICA", fontsize = 20)


# In[154]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[241]:

def escalon(x, c):
    return np.piecewise(x, [x < 0, x > 0], [0, 1])


# In[242]:

c = np.linspace(0, 5)


# In[245]:

plt.plot(x, escalon(x, c), 'm')
plt.axis([x[0], x[-1], 0, 2.5])
plt.grid(True)
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title("GRAFICA ESCALON", fontsize = 20)


# In[177]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[171]:

sigma=0.01
x = np.linspace(-5,5)
e = np.e
pi = np.pi
x = np.linspace(-50, 50)


# In[172]:

def f(x):
    return (1/np.sqrt(2*pi*sigma**2))*(e**-((x**2)/2*(sigma**2)))


# In[173]:

plt.plot(x, f(x), 'r')
plt.grid(True)
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title("GRAFICA SIGMOIDAL", fontsize = 20)


# In[115]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[116]:

x= range(-10, 15)


# In[149]:

def f(x):
    return (4*x+1)


# In[150]:

plt.plot(x, [f(y) for y in x], 'y')
plt.grid(True)
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title("GRAFICA LINEAL", fontsize = 20)


# In[ ]:



