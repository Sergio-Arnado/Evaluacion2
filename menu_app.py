def agregar_compra(compras):
    compra = float(input("Ingrese el monto de la compra: "))
    compras.append(compra)
    print("Compra agregada correctamente.")
def mostrar_compras(compras):
    if len(compras) == 0:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra:.2f}")
def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")
def main():
    compras = []
    total_gastado = 0
    while True:
        print("Menú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        print("Seleccione una opción:")
        opcion = int(input())
        if opcion == 1:
            agregar_compra(compras)
        elif opcion == 2:
            mostrar_compras(compras)
        elif opcion == 3:
            mostrar_total(compras)
        elif opcion == 4:
            print("Gracias, vuelve pronto.")
            break
        else:
            print("Error. Ingresar opciones entre 1 y 4.")
if __name__ == "__main__":
    main()