#Aplicar descuento por la compra de ropa
print("Ingrese el numero de prendas de ropa adquiridos: ")
numero = float(input())
print("Ingrese el numero el costo total de las prendas: ")
costo = float(input())
descuento = 0
if numero <= 4:
    descuento = (costo * 15)/100
    costo = costo - descuento

    print(f"Usted tiene que que pagar: {costo}")
elif numero == 8:
    descuento = (costo * 25)/100
    costo = costo - descuento
    print(f"Usted tiene que pagar: {costo}")

elif numero > 8:
    descuento = (costo * 50) / 100
    costo = costo - descuento
    print(f"Usted tiene que pagar: {costo}")