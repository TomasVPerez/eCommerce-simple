class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.compras = []

    def comprar(self, inv, producto):
        inventarioDict = inv.inventario
        if producto in inventarioDict:
            if inventarioDict[producto] > 0:
                self.compras.append(producto)
                inventarioDict[producto] -= 1
            else:
                print("No hay mas stock")
        else:
            print("No vendemos ese producto")

    def mostrarCompras(self):
        print(f"{self.nombre} compro:")
        for producto in self.compras:
            print(producto.nombre)

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregarProducto(self, producto, cantidad):
        if producto not in self.inventario:
            self.inventario[producto] = cantidad #Como clave pasamos el objeto producto y su correspondiente cantidad
        else:
            self.inventario[producto] += cantidad

    def mostrarInventario(self):
        for clave, valor in self.inventario.items(): #items nos devuelve la clave y su valor 
            print(f"{clave.nombre}: {str(valor)}")
        print()






