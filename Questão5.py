#Declarar

A : int = 0
B : int = 0
C : int = 0
Delta : int = 0
X1 : int = 0
X2 : int = 0
import math

#Inicio

A = int (input("Digite o valor de A: "))
B = int (input ("Digite o valor de B: "))
C = int (input ("Digite o valor de C: "))
Delta = (B*B-4*A*C)
X1 = (-B+math.sqrt (Delta))/(2*A)
X2 = (-B-math.sqrt (Delta))/(2*A)
print ("O Valor de X1 é: ",X1)
print ("O Valor de X2 é: ",X2)

#Fim