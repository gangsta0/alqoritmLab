ust = 3
alt = 1
altHasil = 1
t = ust/alt
cem = 3
while t>=0.001:
    alt = alt * altHasil
    t = ust/alt
    altHasil = altHasil + 1
    ust += 1
    cem += t
print(cem)
