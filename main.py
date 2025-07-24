clientesDiccionario={}
def ingresarClientes():
    try:

        idClienteAux=input("Ingrese el id del cliente: ")
        if not idClienteAux in clientesDiccionario:
            nombreClienteAux = input("Ingrese el nombre del cliente: ")
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
                    "nombre":nombreClienteAux,
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
            j=j+1


    else:
        print("No hay clientes ingresados")

def destinosTotal():
    contadorDestinos=0
    for clave, valor in clientesDiccionario.items():
        for claveDestino, valorDestino in valor["destinos"].items():
            contadorDestinos = contadorDestinos + 1

def recursivaDestinosTotal(clientesDic):
    cantidadClientes=len(clientesDic)
    i=1
    if i==cantidadClientes:
        return 1
    else:
        for clave, valor in clientesDic.items():
            for claveDestino, valorDestino in valor["destinos"].items():
                return 1 + recursivaDestinosTotal(clientesDic)

while True:
    print("==MENU PRINCIPAL==")
    print("1. Ingresar clientes")
    print("2. Ver clientes")
    print("3. Ver numero total de destinos")
    print("4. Cliente con mas destinos")
    print("5. Salir")
    opcion=input("Ingrese el numero de opcion: ")

    match opcion:
        case "1":
            ingresarClientes()
        case "2":
            verClientes()
        case "3":
            print("")