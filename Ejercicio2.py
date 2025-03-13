# Listado de productos
productos = {"id1": {"Nombre": "Pantalón", "Precio": 39.99, "Cantidad": 75},
             "id2": {"Nombre": "Camisa", "Precio": 19.99, "Cantidad": 100},
             "id3": {"Nombre": "Zapatos", "Precio": 59, "Cantidad": 50},
             "id4": {"Nombre": "Corbata", "Precio": 9.99, "Cantidad": 200}
             }

# Listado de pedidos
pedidos = [{"id_pedido": 99, "Email":  "Antonio@gmail.com",
            "Productos": {"id1": 2, "id2": 1}, "Estado": "Enviado"},
           {"id_pedido": 100, "Email": "Maria@gmail.com",
            "Productos": {"id3": 1, "id4": 2}, "Estado": "Entregado"},
           {"id_pedido": 101, "Email": "Antonio@gmail.com",
            "Productos": {"id5": 3}, "Estado": "Enviado"}]

# Listado de clientes registrados
clienteRegistrados = {"Cliente 1": {"Nombre": "Antonio", "Email": "Antonio@gmail.com", "Dirección": "Calle 12 # 43"},
                      "Cliente 2": {"Nombre": "Maria", "Email": "Maria@gmail.com", "Dirección": "Calle 13 # 44"},
                      "Cliente 3": {"Nombre": "Pedro", "Email": "Pedro@gmail.com", "Dirección": "Calle 14  # 45"}
                      }

print("Pedidos actuales:")
for pedido in pedidos:
    print(f"Id_pedido: {pedido['id_pedido']}")
    print(f"Email: {pedido['Email']}")
    print(f"Productos: {pedido['Productos']}")
    print(f"Estado: {pedido['Estado']} \n")

print("Productos actuales:")
for id_producto, producto in productos.items():
    print(f"Id: {id_producto}")
    print(f"Nombre: {producto['Nombre']}")
    print(f"Precio: {producto['Precio']}")
    print(f"Cantidad: {producto['Cantidad']} \n")

# Añadir un nuevo producto
productos["id5"] = {"Nombre": "Chaqueta", "Precio": 102.99, "Cantidad": 10}

# Cambiar estado de pedido 101 a entregado
for pedido in pedidos:
    if pedido["id_pedido"] == 101:
        pedido["Estado"] = "Entregado"
        print("Pedido 101 actualizado a satisfactoriamente")

# Mostrar los pedidos de un cliente por email
print("Mostrando pedidos de un cliente por email")
pedidosCliente = []  # Lista para almacenar los pedidos
correo = input("Ingresa el correo: ")
for producto in pedidos:
    if producto["Email"] == correo.capitalize():
        pedidosCliente.append(producto["Productos"])  # Agregar a la lista

if not pedidosCliente:  # Validad que no este vacia
    print("Cliente no encontrado")
else:
    for pedido in pedidosCliente:
        for id_producto, cantidad in pedido.items():  # Recorrer los productos en el pedido
            if id_producto in productos:
                producto = productos[id_producto]  # Se obttinen los datos del producto
                print(f"Nombre: {producto['Nombre']}")
                print(f"Precio: {producto['Precio']}")
                print(f"Cantidad: {cantidad}")
                print()
            else:
                print(f"Producto {id_producto} no encontrado\n")
