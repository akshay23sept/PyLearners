#Find the first derivative of the following function withing domain [-1, 1] using 
#forward, backwared and central finite difference scheme
#and then plot the graph. 
#Let h = 0.1/0.01/0.001
import numpy as np
# numpy module to handle arrays
import matplotlib.pyplot as plt
# matplotlib module to perform plotting
#defining the function
f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
df = lambda x:0.5*x**4 - 0.6*x**2 + 0.1
h = 0.002
x = np.linspace(-1,1)
plt.plot(x,df(x), '-k')
#FDS difference scheme
dff1 = (f(x+h) - f(x))/h
plt.plot(x,dff1, '-b')
#BDS difference scheme
dff1 = (f(x) - f (x-h))/h
plt.plot(x,dff1, '-r')
#CDS difference scheme
dff1 = (f(x+h) - f (x-h))/(2*h)
plt.plot(x,dff1, '-g')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["theoretical", "FDS", "BDS", "CDS"])
plt.grid()
plt.title('f(x) = 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2')
plt.show()
plt.show()