import math

def cantChewbaccas(vueltas):
    # ceil: redondea por techo de un numero
    chewbaccas = math.ceil((vueltas/3))

    return chewbaccas

#rta/: 5
chewbaccas = cantChewbaccas(13.5)
print(chewbaccas)