import matplotlib.pyplot as plt
import numpy as np

import pandas as pd 
df= pd.read_csv("people7.txt") 
print(df.describe())
print(df.head())
print(df.dtypes)
print(df['spx'])

plt.figure(1)
plt.plot(df['spx'],df['spy'],'r*')
plt.plot(df['px'],df['py'],'b*')

plt.figure(2)
plt.plot(df['spang'],'r*')
plt.plot(df['ang'],'b*')
plt.show()

#t=[0:0.1:1]
#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()