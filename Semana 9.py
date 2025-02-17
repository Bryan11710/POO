class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir(self, id_producto, nombre, cantidad, precio):
        if any(p.id_producto == id_producto for p in self.productos):
            print("ID ya existe.")
        else:
            self.productos.append(Producto(id_producto, nombre, cantidad, precio))

    def eliminar(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]

    def actualizar(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.id_producto == id_producto:
                p.cantidad = cantidad or p.cantidad
                p.precio = precio or p.precio
                return
        print("Producto no encontrado.")

    def buscar(self, nombre):
        for p in self.productos:
            if nombre.lower() in p.nombre.lower():
                print(f"{p.id_producto}: {p.nombre}, {p.cantidad}, {p.precio}")

    def mostrar(self):
        for p in self.productos:
            print(f"{p.id_producto}: {p.nombre}, {p.cantidad}, {p.precio}")

def menu():
    print("\n1. Añadir 2. Eliminar 3. Actualizar 4. Buscar 5. Mostrar 6. Salir")
    return input("Selecciona opción: ")

def main():
    inventario = Inventario()
    while True:
        opcion = menu()
        if opcion == '1':
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir(id_producto, nombre, cantidad, precio)
        elif opcion == '2':
            id_producto = input("ID: ")
            inventario.eliminar(id_producto)
        elif opcion == '3':
            id_producto = input("ID: ")
            cantidad = input("Cantidad (deja vacío si no cambia): ")
            precio = input("Precio (deja vacío si no cambia): ")
            inventario.actualizar(id_producto, int(cantidad) if cantidad else None,
                                  float(precio) if precio else None)
        elif opcion == '4':
            nombre = input("Nombre: ")
            inventario.buscar(nombre)
        elif opcion == '5':
            inventario.mostrar()
        elif opcion == '6':
            break

if __name__ == "__main__":
    main()
