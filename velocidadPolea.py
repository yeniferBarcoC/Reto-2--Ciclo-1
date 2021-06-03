import math

def velocidadPolea(puerta,tiempo):

    puerta_cm = puerta*100
    largo_muro = puerta_cm
    largo_cuerda = math.sqrt(puerta_cm**2+largo_muro**2)
    
    tiempo_maximo_seg = tiempo*60
    velocidad = largo_cuerda/tiempo_maximo_seg

    return velocidad

#rta/: 8.84
velocidad = velocidadPolea(15,4)
print(round(velocidad,2))