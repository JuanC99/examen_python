import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    #El error viene por la incializacion de la lista resultado, ya que cada vez que encuentra un elemento se vuelve a inicializar.
    #Para solucionar este error basta con incializar la lista resultado, antes de que inicien todas las comprobaciones
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    #El error viene dado por el formato en el que generamos el clients_lista ya que no concide con el formato que deseamos en 
    # en las comprobaciones del test. Para solucionarlo basta con eliminar el nodo nif, que englobaba a el resto de elementos, ya 
    # que en este caso nif, se utiliza para identificar el elemento en el diccionario
    clients_list[nif] = {
              'name': name,
              'address': address,
              'phone': phone,
              'email': email
        
    }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """
    #El error vien dado porque al asignar el valor de una lista, este actua como un punetero, por lo que si eliminas los valores de una lista,
    #estos tambien se eliminan de la lista original. Para solucionar este error podemos utilizar la funcion copy, que genenera una copia
    # de la lista sin llegar a ser un puntero
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales.copy()
       
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

    
