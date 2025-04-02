from conexion import conectar

class Clientes():

    def createCliente(self, nombre, apellido, correo):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO clientes (nombre, apellido, correo) VALUES (%s, %s, %s) ", (nombre, apellido, correo))

        affectedRows = cursor.rowcount

        message = ""

        if affectedRows == 0 :
            message = f"No se creó ningún cliente"
            return message

        message =  f"Se agrego con exito el cliente"

        conexion.commit()
        cursor.close()
        conexion.close()
        return message


    def getClientes(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()

        cursor.close()
        conexion.close()
        return clientes

    def getClienteById(self, id):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))

        cliente = cursor.fetchone()

        if cliente is None:
            return "El cliente no existe"

        cursor.close()
        conexion.close()

        return cliente

    def deleteClienteById(self, id: str):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))

        affectedRows = cursor.rowcount

        message = ""

        if affectedRows == 0 :
            message = f"El cliente {id} no existe"
            return message


        message =  f"Se eliminó el cliente con el ID {id}"


        conexion.commit()
        cursor.close()
        conexion.close()

        return message

    def cambiarCorreo(self, id, correo):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("UPDATE clientes SET correo = %s WHERE id = %s", (correo, id))


        affectedRows = cursor.rowcount
        message = ""

        if affectedRows == 0 :
            message = f"El cliente {id} no existe"
            return message


        message =  f"Se modificó el correo del cliente con id: {id}, su nuevo correo ahora es: {correo}"


        conexion.commit()
        cursor.close()
        conexion.close()

        return message











