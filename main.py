clientesDiccionario={}
def ingresarClientes():
    try:

        idClienteAux=input("Ingrese el id del cliente: ")
        if not idClienteAux in clientesDiccionario:
            nombreCLienteAux = input("Ingrese el nombre del cliente: ")
            destinosDiccionarioAux={}
            i=1
            print("---Destinos---")
            print("Aqui podra ingresar los destinos (minimo 1 y maximo 5)")
            cantidad=int(input("Ingrese la cantidad de destinos a ingresar: "))
            if(cantidad >= 1):
                while i<=cantidad:
                    nombreDestinoAux=input(f"Ingrese el nombre del destino #{i}: ")
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
        else:
            print("El codigo del cliente ya existe")

    except ValueError:
        print("ERROR: DATOS INGRESADOS NO VALIDOS")

def verClientes():
    print("==CLIENTES==")
    if len(clientesDiccionario)>0:
        j=1
        for clave, valor in clientesDiccionario.items():
            print(f"Client #{j}")
            print(f"Codigo cliente: {clave}")
            print(f"Nombre: {valor["nombre"]}")
            for claveDestino, valorDestino in valor["destinos"].items():
                print(f"Id del destino: {claveDestino}")
                print(f"Lugar del destino: {valorDestino["nombre"]}")
            print("------"*10)


    else:
        print("No hay clientes ingresados")
while True:
    print("==MENU PRINCIPAL==")
    print("1. Ingresar clientes")
    print("2. Ver clientes")
    print("3. Ver numero total de destinos")
    print("4. Cliente con mas destinos")
    print("5. Salir")
    opcion=input("Ingrese el numero de opcion")

    match opcion:
        case "1":
            ingresarClientes()
        case "2":
            verClientes()