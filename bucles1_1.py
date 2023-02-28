# excedente = 0
# ingreso = float(input("Digite su su ingreso:"))
# si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual
# al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2
# centavos, más el 32% del excedente sobre 85,528 pesos.
# if(ingreso<85528):
#     ipi = (ingreso * .18) - 556.02
#     ipi = round(ipi, 0)
#    # print(f"El impuesto a pagar es:%d", "",  ipi)
# else:
#     ipi = (ingreso - 85528) * 0.32 + 14839.02
# if (ipi < 0.0):
#     ipi = 0.0
# excedente = round(ipi, 0)
# print("El impuesto a pagar es:", "", ipi)
#

# # Ingresa el primer valor.
# number = int(input("Introduce un número o escribe -1 para detener: "))
#
# # Si el número no es igual a -1, continuaremos
# while number != -1:
#     # ¿Es el número más grande que el valor de largest_number?
#     if number > largest_number:
#         # Sí si, se actualiza largest_number.
#         largest_number = number
#     # Ingresa el siguiente número.
#     number = int(input("Introduce un número o escribe -1 para detener: "))
#
# # Imprime el número más grande.
# print("El número más grande es:", largest_number)