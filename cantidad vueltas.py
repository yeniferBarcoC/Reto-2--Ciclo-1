import math

def cantVueltas(puerta, polea):

    puerta_cm = puerta*100

    largo_muro = puerta_cm
    largo_cuerda = math.sqrt(puerta_cm**2+largo_muro**2)
    perimetro_polea = 2*math.pi*(polea/2)
    vueltas = largo_cuerda/perimetro_polea

    return vueltas

vueltas = cantVueltas(15,50)
print(round(vueltas,1))
