from clientes import Clientes

cliente = Clientes()



obtenerClientes = cliente.getClientes()


for cliente in obtenerClientes:
    print(cliente)
