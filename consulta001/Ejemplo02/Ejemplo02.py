#Calcular promedio de final notas del colegio
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}, calcularemos tu nota final")
notamatematica = float(input("Ingrese su nota de matematica: "))
print (f"su nota de matematica es de: {notamatematica}")
notalenguaje = float(input("Ingrese su nota de Lengua y Literatura: "))
print (f"su nota de Lengua y Literatura es de: {notalenguaje}")
notaciencias = float(input("Ingrese su nota de Ciencias Naturales: "))
print (f"su nota de Ciencias Naturales es de: {notaciencias}")
notasociales = float(input("Ingrese su nota de Estudios Sociales: "))
print (f"su nota de Estudios Sociales es de: {notasociales}")

promediofinal = (notamatematica + notalenguaje + notaciencias + notasociales)/4
print (f"Su promedio final es de: {promediofinal} ")