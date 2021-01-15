#Find the first and second derivative of the following function withing domain [-1, 1] using forward, backward and central finite difference scheme
#and then plot the graph. 
#Let h = 0.1/0.01/0.001
import numpy as np
# numpy module to handle arrays
import matplotlib.pyplot as plt
# matplotlib module to perform plotting
#defining the function
f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
df = lambda x:0.5*x**4 - 0.6*x**2 + 0.1
df1 = lambda x:2*x**3 - 1.2*x 
#defining the value of h
#for h in range (0.1,0.100,10):
#defining the vector of x, linspace creates an 1-D array and the default value of number of its element is 50--change 
#to 100 if you want
h = 0.01
x = np.linspace(-1,1)
#plt.plot(x,df(x), '-k')
plt.plot(x,df1(x), '-k')

#FDS difference scheme
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x)) /h**2
#dff2 = (f(x+2*h) - 2*f(x+h) + f(x)) /h**2
#plt.plot(x,dff1, '-b')
plt.plot(x,dff2, '-b')

#BDS difference scheme
dff1 = (f(x) - f (x-h))/h
dff2 = (f(x) - 2*f(x-h) + f(x-2*h)) /h**2
#plt.plot(x,dff1, '-r')
plt.plot(x,dff2, '-r')

#CDS difference scheme
dff1 = (f(x+h) - f (x-h))/(2*h)
dff2 = (f(x+h) - 2*f(x) + f(x-h)) /h**2
#plt.plot(x,dff1, '-g')
plt.plot(x,dff2, '-g')
plt.xlabel('f(x)')
plt.ylabel('df*2/dx')
plt.legend(["Theo", "FDS", "BDS", "CDS"])
plt.grid()
plt.title('f(x) = 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2')
plt.show()