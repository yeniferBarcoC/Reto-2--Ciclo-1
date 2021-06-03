# -*- coding: utf-8 -*-
"""
Reto 2. La puerta del castillo
Yenifer Barco Castrillón
Mayo 18-2021
"""
#======================================================================
#    Librerias utilizadas
# =====================================================================
import math


#======================================================================
#    Definicion de funciones(Dividir)
# =====================================================================
def convertir_a_cm(largo_puerta):
  """ 
  Parameters
  ----------
  largo_puerta:float
     valor del largo de la puerta en metros
  Returns
  -------
  largo_puerta_cm:float
     valor del largo de la puerta en cm    
  """ 
  largo_puerta_cm = largo_puerta*100
  
  return largo_puerta_cm
#---------------------------------------------------------
def calcular_largo_cuerda(largo_puerta_cm):
  """ 
  Parameters
  ----------
  largo_puerta_cm:float
     valor del largo de la puerta en centimetros
  Returns
  -------
  largo_cuerda:float
     valor del largo de la cuerda    
  """ 
  largo_muro = largo_puerta_cm
  largo_cuerda = math.sqrt(largo_puerta_cm**2+largo_muro**2)
  
  return largo_cuerda
#---------------------------------------------------------
def calcular_perimetro_polea(diametro_polea):
  """ 
  Parameters
  ----------
  diametro_polea:float
     valor del diametro de la polea en cm
  Returns
  -------
  perimetro_polea:float
     valor del perimetro de la polea 
  """ 
  perimetro_polea = 2*math.pi*(diametro_polea/2)
  
  return perimetro_polea
#--------------------------------------------------------
def calcular_vueltas_polea(largo_cuerda, perimetro_polea):
  """ 
  Parameters
  ----------
  largo_cuerda:float
     valor del largo de la cuerda
  perimetro_polea:float
     valor delperimetro de la polea
  Returns
  -------
  num_vueltas_polea:float
     valor de las vueltas que da la polea al cerrar la puerta
  """
  num_vueltas_polea = largo_cuerda/perimetro_polea
  
  return num_vueltas_polea
#-------------------------------------------
def calcular_numero_chewbaccas(num_vueltas_poleas):
  """ 
  Parameters
  ----------
  num_vueltas_polea:float
     valor de las vueltas que da la polea al cerrar la puerta
  Returns
  -------
  num_chewbaccas:float
     valor de chewbaccas necesarios para cerrar la puerta
  """
  num_chewbaccas = (num_vueltas_poleas/3)
  
  return num_chewbaccas
#-------------------------------------------
def calcular_velocidad(largo_cuerda, tiempo_maximo):
  """ 
  Parameters
  ----------
  largo_cuerda:float
     valor del largo de la cuerda
  tiempo_maximo:float
     valor del tiempo maximo en el que se necesita cerrar la puerta
  Returns
  -------
  velocidad:float
     valor de la velocidad con la que se necesita cerrar la puerta
  """
  tiempo_maximo_seg = tiempo_maximo*60
  velocidad = largo_cuerda/tiempo_maximo_seg
  return velocidad

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
  
#lectura del largo de la puerta
largo_puerta = float(input("Ingrese el largo de la puerta en metros: "))

#lectura diametro de la polea
diametro_polea = float(input("Ingrese el diametro de la polea en centimetros: "))

#lectura del tiempo maximo de cierre de la puerta
tiempo_maximo = float(input("Ingrese el tiempo maximo de cierre de puerta en minutos: "))
  
#Llamado/invocación de funciones
largo_puerta_cm = convertir_a_cm(largo_puerta)
largo_cuerda = calcular_largo_cuerda(largo_puerta_cm)
perimetro_polea = calcular_perimetro_polea(diametro_polea)
num_vueltas_polea = calcular_vueltas_polea(largo_cuerda, perimetro_polea)
num_chewbaccas = calcular_numero_chewbaccas(num_vueltas_polea)
velocidad = calcular_velocidad(largo_cuerda,tiempo_maximo)

#Muestra el usuario los resultados
print("\nLa polea dio ", "{0:.4f}".format(num_vueltas_polea), " vueltas")
print("Se necesitan ", "{0:.4f}".format(num_chewbaccas), " chewbaccas para cerrar la puerta")
print("la velocidad necesaria para girar la puerta es de ","{0:.4f}".format(velocidad)," cm/seg")