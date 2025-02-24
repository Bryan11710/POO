import os, json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            return json.load(open(self.archivo)) if os.path.exists(self.archivo) else {}
        except (FileNotFoundError, json.JSONDecodeError, PermissionError):
            return {}

    def guardar_inventario(self):
        try:
            json.dump(self.productos, open(self.archivo, "w"), indent=4)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def modificar_producto(self, nombre, cantidad=None, precio=None, eliminar=False):
        if eliminar:
            self.productos.pop(nombre, None)
        else:
            self.productos[nombre] = {"cantidad": cantidad or self.productos.get(nombre, {}).get("cantidad", 0),
                                      "precio": precio or self.productos.get(nombre, {}).get("precio", 0)}
        self.guardar_inventario()
        print(f"{'Eliminado' if eliminar else 'Actualizado'}: {nombre}")

    def mostrar_inventario(self):
        print("Inventario vacío" if not self.productos else json.dumps(self.productos, indent=4))

# Menú de opciones
def menu():
    inventario = Inventario()
    opciones = {"1": ("Agregar/Actualizar", False), "2": ("Eliminar", True), "3": ("Mostrar", None)}
    while (opcion := input("\n1. Agregar/Actualizar\n2. Eliminar\n3. Mostrar\n4. Salir\nOpción: ")) != "4":
        if opcion in opciones:
            if opcion == "3":
                inventario.mostrar_inventario()
            else:
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: ")) if not opciones[opcion][1] else None
                precio = float(input("Precio: ")) if not opciones[opcion][1] else None
                inventario.modificar_producto(nombre, cantidad, precio, opciones[opcion][1])
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
