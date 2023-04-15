def calcular_imc():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en m: "))

    imc = peso / (altura ** 2)
    if imc < 16:
        print("CRITERIO DE INGRESO EN HOSPITAL")
    elif imc >= 16 and imc < 17:
        print("INFRAPESO")
    elif imc >= 17 and imc < 18:
        print("BAJO PESO")
    elif imc >= 18 and imc < 25:
        print("PESO NORMAL")
    elif imc >= 25 and imc < 30:
        print("SOBREPESO")
    elif imc >= 30 and imc < 35:
        print("SOBREPESO CRÓNICO")
    elif imc >= 35 and imc < 40:
        print("OBESIDAD PREMÓRBIDA")
    else:
        print("OBESIDAD MÓRBIDA")

    print("Su índice de masa corporal es:", imc)



if __name__ == "__main__":
    calcular_imc()


def calcular_total():
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio_unitario = int(input("Ingrese el precio unitario: "))

    subtotal = cantidad * precio_unitario
    descuento = 0

    if cantidad > 10:
        descuento = subtotal * 0.07
        if cantidad > 10:
            descuento = subtotal * 0.07
            print("Tienes descuento")
        else:
            print("no tiene descuento")

    total = subtotal - descuento

    print("Nombre del producto:", nombre_producto)
    print("Cantidad:", cantidad)
    print("Precio unitario:", precio_unitario)
    print("Subtotal:", subtotal)
    print("Descuento:", descuento)
    print("Total:", total)

if __name__=="__main__":
    calcular_total()

