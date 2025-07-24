clientesDiccionario={}
def ingresarClientes():
    try:
        nombreCLienteAux=input("Ingrese el nombre del cliente: ")
        idClienteAux=input("Ingrese el id del cliente: ")
        destinosDiccionarioAux={}
        i=1
        print("---Destinos---")
        print("Aqui podra ingresar los destinos (minimo 1 y maximo 5)")
        cantidad=int(input("Ingrese la cantidad de destinos a ingresar: "))
        if(cantidad >= 1):
            while i<=cantidad:
                nombreDestinoAux=input("Ingrese el nombre del destino: ")
                destinosDiccionarioAux[i]={
                    "nombre": nombreDestinoAux,
                }
                i=i+1
            clientesDiccionario[idClienteAux]={
                "nombre":nombreDestinoAux,
                "destinos":destinosDiccionarioAux,
            }
        else:
            print("Debe ingresar al menos un destino")
    except ValueError:
        print("ERROR: DATOS INGRESADOS NO VALIDOS")
