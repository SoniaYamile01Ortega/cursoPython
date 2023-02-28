# # var = 0  # Asignando 0 a var
# # print(var != 0) #False
# #
# # var = 1  # Asignando 1 a var
# # print(var != 0) #True
# #
# # n = int(input("Digite un numero"))
# # # if n > 100:
# # #     print({n},"n es mayor", n)
# # # print({n},"es menor que 100")
# # print(n>=100)
# # todo condicionale simples
# # edad = int(input("Ingrese la edad de la persona:"))
# # if edad >= 18:
# #   print("La Persona es mayor de edad")
# # else:
# #   print("La Persona es menor de edad")
# clima = int(input("Estado del clima"))
# if(clima == 1):
#   print("Saldré a caminar y almorzaré")
# else:
#   print("Iré al cine")
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
  largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
  largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)