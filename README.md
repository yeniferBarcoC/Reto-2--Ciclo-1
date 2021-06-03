Yenifer Barco Castrillón
Mayo 18/2021

##Reto 2: La puerta del castillo

En este reto se va a continuar con la segunda parte del ejercicio de la puerta del castillo. para ello vamos a partir de la lista de requisitos de software que definimos en el documento.

##Requisitos de software

 |R1:Convertir metros a centímetros. |
 | :-------------: |
|Dado el largo de la puerta en metros se realiza la conversión a centímetros aplicando la fórmula de conversión. |

 |R2:Calcular largo de la cuerda. |
 | :-------------: |
|Dado el largo de la puerta calcular el largo de la cuerda con la fórmula del teorema de Pitágoras. |

 |R3: Calcular el perímetro de la polea. |
 | :-------------: |
|Dado el diámetro de la polea se calcula el perímetro de la polea con la fórmula del perímetro de un circulo. |

 |R4:Calcular número de vueltas de la polea. |
 | :-------------: |
|Obtener el número de vueltas de la polea dividiendo el largo de la cuerda por el perímetro de la polea utilizando la formula dada en la etapa de definición del problema. |

 |R5: Calcular número de chewbaccas. |
 | :-------------: |
|Obtener el número de chewbaccas necesarios para cerrar la puerta a partir del número de vueltas de la polea, utilizando la formula dada en la etapa de definición del problema. |

 |R6:Calcular la velocidad. |
 | :-------------: |
|Dado el tiempo en minutos se realiza la conversión a segundos para calcular la velocidad a la que es necesario cerrar la puerta, utilizando la fórmula de la velocidad. |

## Algoritmos
Por cada requisito funcional se tiene un algoritmo. En el análisis y diseño que hicimos aplicando IDEAL se identificaron 6 subproblemas los cuales se pasaron a un algoritmo cada uno. Como se ve a continuación:

---
Algoritmo:	R1: Convertir metros a centímetros:
---
1.	Leer largo_puerta
2.	Convertir largo_puerta_cm ← largo_puerta*100
3.	Retornar largo_puerta_cm

---
Algoritmo:	R2: Calcular largo de la cuerda:
---
1.	Llamar largo_puerta_cm
2.	Calcular largo_muro ← largo muro=largo_puerta_cm
3.	Calcular largo_cuerda ← √(largo_puerta_cm)^2+(largo_muro)^2 
4.	Retornar largo_cuerda

---
Algoritmo:	R3: Calcular perímetro de la polea:
---
1.	Leer diametro_polea
2.	Calcular perimetro_polea ←  2π((diametro_polea)/2)
3.	Retornar perimetro_polea

---
Algoritmo:	R4: Calcular número de vueltas de la polea
---
1.	Llamar largo_cuerda
2.	Llamar perimetro_polea
3.	Calcular num_vueltas_polea ← (largo_cuerda)/(perimetro_polea)
4.	Retornar num_vueltas_polea

---
Algoritmo:	R5: Calcular número de chewbaccas
---
1.	Llamar num_vueltas_polea
2.	Calcular num_chewbaccas ← (numero_vueltas_polea)/3
3.	Retornar num_chewbaccas

---
Algoritmo:	R6: Calcular velocidad para cerrar la puerta
---
1.	Llamar tiempo_maximo
2.	Llamar largo_cuerda
3.	Convertir tiempo_maximo_seg ← tiempo_maximo*60
4.	Calcular velocidad ← (largo_cuerda)/(tiempo_maximo_seg)
5.	Retornar velocidad
