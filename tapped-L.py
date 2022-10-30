from cmath import pi
import numpy as np

wo = 2*pi*(25e6)

# Input de datos
print("Ingrese inductor L1 del inductor partido")
L_1 = float(input())

print("Ingrese inductor L2 del inductor partido")
L_2 = float(input())

print("Ingrese inductor Lin de la etapa de entrada")
L_in = float(input())

print("Ingrese resistencia Rin de la etapa de entrada")
R_in = float(input())

# Calculo de X y Q en la entrada SERIE
X_ls = (wo * L_in)
Q_in_s = X_ls/R_in

# Paso la etapa de entrada a PARALELO
R_in_p = R_in * (1+ (Q_in_s ** 2))
L_in_p = L_in * ((((Q_in_s ** 2)+1)/(Q_in_s ** 2)))
X_lp = (wo * L_in_p)
Q_in_p = R_in_p / X_lp

# Calculo la L total como el paralelo entre L_in_p y L_2 y el nuevo Q paralelo
Lt_eq_p = ((L_1 * L_in_p) / (L_1 + L_in_p) )
Xt_lp = (wo * Lt_eq_p)
Q_p = R_in_p / Xt_lp

#Paso el paralelo entre Lt_eq_p y R_in_p a SERIE
R_eq_s = R_in_p * (1/(1+ Q_p **2))
Lt_eq_p = Lt_eq_p * ((Q_p **2) / ((Q_p ** 2)+1))
X_eq_s = 1 / (wo * Lt_eq_p)
Q_eq_s = X_eq_s / R_eq_s

#La Ltotal será la suma de L_1 y Lt_eq_p
Lt = L_1 + Lt_eq_p
Xl_t = (wo * Lt)
Qt = Xl_t / R_eq_s

#Convierto la rama Lt y R_eq_s a PARALELO para poder comparar con la etapa de salida
Rt_eq_p = R_eq_s * (1+ (Qt ** 2))
Lt_eq_p = Lt * ((((Qt ** 2)+1)/(Qt ** 2)))
Xt_eq_p = (wo * Lt_eq_p)
Qt_eq_p = Rt_eq_p / Xt_eq_p

#print de resultados
print("Inductancia equivalente serie:",Lt)
print("Reactancia equivalente serie:",Xl_t)
print("Resistencia equivalente serie:",R_eq_s)
print("------------------")
print("Inductancia equivalente paralelo:",Lt_eq_p)
print("Reactancia equivalente paralelo:",Xt_eq_p)
print("Resistencia equivalente paralelo:",Rt_eq_p)
print("------------------")