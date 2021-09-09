import pickle
import numpy as np

filepath="./dataset/vocab/vocab.pkl"

f=open(filepath,'rb')

dict1=pickle.load(f)

print(dict1)

print(len(dict1))

filename="./dataset/vocab/embedding.npy"

arr= np.load(filename)

print(arr)
print(len(arr))
