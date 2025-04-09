C = [5, 7, 9, 11, 14, 16, 18]  
cem = 0        
say = 0         
for eded in C:
    if eded % 3 == 2:   
        cem += eded    
        say += 1        
if say > 0:
    ededi_orta = cem / say
    print("ededi orta: ", ededi_orta)
else:
    print("uygun eded tapilmadi")
