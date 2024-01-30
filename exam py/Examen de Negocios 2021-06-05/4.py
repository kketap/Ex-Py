listin = {'919654665':'Pedro', '917489210': 'Luis', '623543213':'Carmen', '674833721':'Luis'}

listin2 = {}

for i in listin.values():
    
    listin2[i] = {}

for k , v in listin.items():
    
    if k[0] == '6':
        listin2[v]["movil"] = k
    else :
        listin2[v]["fijo"] = k

print(listin2)

for i in sorted(listin2.keys()):
    
    print("Teléfonos de",i)

    for k , v in listin2[i].items():
        
        print('\t', k, ':', v)