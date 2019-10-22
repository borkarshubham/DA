# -*- coding: utf-8 -*-
"""DA_Assign_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NtkX5IqhFpw8qGHgHLwzcunczJMM84rR
"""

import pandas as pd
import math
import matplotlib.pyplot as plt

#from google.colab import files

#uploaded = files.upload()
#print(uploaded)

#import io
#df = pd.read_csv(io.BytesIO(uploaded['Iris.csv']))

df = pd.read_csv("iris.csv")

df

df.describe()

df.columns

col = df.columns
print(len(col))

for i in range(0,4):
  feature = col[i]
  Series_feature = df[feature]
  count = len(Series_feature)
  
  mean = 0
  
  print(feature)
  print(count)
  
  if Series_feature.dtype.name == "float64" or Series_feature.dtype.name == "int64":
    print("Attribute is numerical")
  else:
    print("Attribute is nominal")
    
  min = 5
  max = -1
  
  for element in Series_feature:
    if element > max:
      max = element
  print("Maximum is :- ",max)
  
  for element in Series_feature:
    if element < min:
      min = element
  print("Minimum is :- ",min)
 
  
  for element in Series_feature:
    mean += element
    
  mean /= count
  print("Mean = ",mean)
    
  x_sum = 0
  for element in Series_feature:
    x_sum += (element-mean)**2
  val = x_sum/(count)
  std_ev = math.sqrt(val)
  print("Variance is:- ",val)
  print("Standard deviation is:- ",std_ev)
  
  k = 0.25
  index = k*count
  
  if index.is_integer():
    percentile = (Series_feature[index-1]+Series_feature[index])/2
  else:
    index = int(index)
    percentile = Series_feature[index-1]
  print(k, " percentile is :-", Series_feature.quantile(0.25))
 
  print("\n")

for i in range(0,4):
  feature = col[i]
  df[feature].plot(kind = "hist")
  plt.title(feature+" distribution")
  plt.xlabel(feature)
  plt.show()

print("\n")
df.boxplot(by = "class", column = ["x2"], grid = False)
