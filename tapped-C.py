from cmath import pi
import numpy as np

wo = 2*pi*(25e6)

print("Ingrese capacitor C1 del capacitor partido")
C_1 = float(input())

print("Ingrese capacitor C2 del capacitor partido")
C_2 = float(input())

print("Ingrese capacitor Cout de la etapa de salida")
C_out = float(input())

print("Ingrese resistencia Rout de la etapa de salida")
R_out = float(input())

X_cs = 1 / (wo * C_out)
Q_out_s = X_cs/R_out

# Paso la etapa de salida a PARALELO
R_out_p = R_out * (1+ (Q_out_s ** 2))
C_out_p = C_out * ((Q_out_s ** 2)/((Q_out_s ** 2)+1))
X_cp = 1/ (wo * C_out_p)
Q_out_p = R_out_p / X_cp

# Calculo la capacidad total entre C_2 y C_out_p
C_t = C_2 + C_out_p 
X_ct = 1 / (wo*C_t)

#Calculo del Q paralelo del par C_t y R_out_p
Q_p = R_out_p / X_ct

#Paso el paralelo entre C_t y R_out_p a SERIE
R_eq_s = R_out_p * (1/(1+ Q_p **2))
C_eq_s = C_t * (((Q_p ** 2)+1)/(Q_p ** 2))
X_eq_s = 1 / (wo * C_eq_s)
Q_eq_s = X_eq_s / R_eq_s

# Hago el paralelo entre C_eq_s y C_1 para hallar la C total equivalente serie
Ct_eq_s = ((C_1 * C_eq_s) / (C_1 + C_eq_s) )
Xt_eq_s = 1 / (wo * Ct_eq_s)
Qt_eq_s = Xt_eq_s / R_eq_s

#Convierto la rama Ct_eq_s y R_eq_s a PARALELO para poder comparar con la etapa de entrada
Rt_eq_p = R_eq_s * (1+ (Qt_eq_s ** 2))
Ct_eq_p = Ct_eq_s * ((Qt_eq_s **2) / ((Qt_eq_s ** 2)+1))
Xt_eq_p = 1 / (wo * Ct_eq_p)
Qt_eq_p = Rt_eq_p / Xt_eq_p

print("Capacidad equivalente serie:",Ct_eq_s)
print("Reactancia equivalente serie:",Xt_eq_s)
print("Resistencia equivalente serie:",R_eq_s)
print("------------------")
print("Capacidad equivalente paralelo:",Ct_eq_p)
print("Reactancia equivalente paralelo:",Xt_eq_p)
print("Resistencia equivalente paralelo:",Rt_eq_p)
print("------------------")