from clientes import Clientes

cliente = Clientes()


#obtenerClienteID = cliente.getClienteById(2)

#eliminarCliente = cliente.deleteClienteById(1)

#cambiarMail = cliente.cambiarCorreo(2, "correocambiado.com")


obtenerClientes = cliente.getClientes()


for cliente in obtenerClientes:
    print(cliente)
