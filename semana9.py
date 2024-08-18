class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

        class Inventario:
            def __init__(self):
                self.productos = []

            def añadir_producto(self, producto):
                # Verificar que el ID sea único
                for p in self.productos:
                    if p.get_id() == producto.get_id():
                        print("Error: El ID del producto ya existe.")
                        return
                self.productos.append(producto)
                print(f"Producto {producto.get_nombre()} añadido correctamente.")

            def eliminar_producto(self, id):
                for i, producto in enumerate(self.productos):
                    if producto.get_id() == id:
                        del self.productos[i]
                        print(f"Producto con ID {id} eliminado correctamente.")
                        return
                print("Error: Producto no encontrado.")

            def actualizar_producto(self, id, cantidad=None, precio=None):
                for producto in self.productos:
                    if producto.get_id() == id:
                        if cantidad is not None:
                            producto.set_cantidad(cantidad)
                        if precio is not None:
                            producto.set_precio(precio)
                        print(f"Producto con ID {id} actualizado correctamente.")
                        return
                print("Error: Producto no encontrado.")

            def buscar_producto(self, nombre):
                resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
                if resultados:
                    for producto in resultados:
                        print(
                            f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
                else:
                    print("No se encontraron productos con ese nombre.")

            def mostrar_productos(self):
                if self.productos:
                    for producto in self.productos:
                        print(
                            f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
                else:
                    print("El inventario está vacío.")


class Inventario:
    pass


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad: "))
            precio = float(input("Introduce el precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
#tiffany_quiñonez

