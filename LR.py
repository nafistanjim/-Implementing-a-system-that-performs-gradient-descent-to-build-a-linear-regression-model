from msilib.schema import Error
import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv(r"C:\Users\nafis\OneDrive\Desktop\CSE445\data.csv")

x=dt['x'] # determining x 
y=dt['y'] # deter mining y

m = 0                                                         #Initial value of m 
c = 0                                                         #Initial value of m 
L = 0.0001                                                    # learning Rate

n = int(100)                                                  # Number of elements in x column

iterations = 1000                                             # valu will be updated 1000 times


                           # Performing Gradient Descent in Linear Regression Modle 

for i in range(iterations): 
    y_pred = m*x + c                                          # Predicted value of y
    Dm = (-2/n) * sum(x*(y-y_pred))                           # Derivative of COST with respectto m
    Dc = (-2/n) * sum(y-y_pred)                               # Derivative of COST with respect to c
    m = m-L*Dm                                                # Updated value of m
    c = c-L*Dc                                                # Updated value of c
    #print (m, c)                                              #1000 times updated output value of m and c 

print('m:',m)                                                 #New m output
print('c:',c)  

print("The iteration" + m)

y_pred = m*x + c                                              #prediction output
plt.scatter(x, y)
plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)], color='red')
plt.show()
