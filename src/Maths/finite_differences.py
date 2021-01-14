#Find the first and second derivative of the following function at x = 0.1
#fun = 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
#Compare numerical solution at h = 0.1, 0.01, 0.001
#The analytical differentiation yields 
      #  f'(0.1) = 0.09405
       # f''(0.1) = -0.118

#defining the function
f = lambda x:0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
#defining the value of x where we wan't to calculate differences
#defining step size
x = 0.1
h = 0.01 
#check the % error by varying h
#defininin theoritical or analystical value for comparision
df1 = 0.090405
df2 = -0.118
#Forward difference scheme
print("\t f'x, \t\t error, \tf''x, \t\t error")
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x)) /h**2
print ("FDS\t% f\t% f\t% f\t% f"%(dff1, dff1 - df1, dff2, dff2 - df2))
#Backward difference scheme
dff1 = (f(x) - f (x-h))/h
dff2 = (f(x) - 2*f(x-h) + f(x-2*h)) /h**2
print ("BDS\t% f\t% f\t% f\t% f"%(dff1, dff1 - df1, dff2, dff2 - df2))
#Central difference scheme
dff1 = (f(x+h) - f (x-h))/2*h
dff2 = (f(x+h) - 2*f(x) + f(x-h)) /h**2
print ("CDS\t% f\t% f\t% f\t% f"%(dff1, dff1 - df1, dff2, dff2 - df2))
