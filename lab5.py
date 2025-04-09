import math
a = [1, 2, 1.5, 0.5, 1, 1, 2, 1, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 0.5, 1, 1]
hasil = 1
for eded in a:
    hasil *= eded  
S = math.cos(hasil)
print("S: ", S)
