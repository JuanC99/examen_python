import random
def choose_secret(filename):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    f = open(filename, mode="rt", encoding="utf-8")
    linea = f.readline()
    palabras=[]
    while linea != "" :
      linea = linea.replace('\n',"")
      palabras.append(linea)
      linea = f.readline()
    f.close()
    secret = random.choice(palabras)
    return secret
    
def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    word = word.upper()
    secret = secret.upper()

    same_position = []
    same_letter = []
    contador_word = 0
    contador_secret = 0
    letra_encontrada = False

    for c in word:

      for c2 in secret:
        if(c == c2 and contador_secret == contador_word):
          same_position.append(contador_secret)
          letra_encontrada=True
        contador_secret = contador_secret+1
      
      if(c in secret and letra_encontrada==False):
        same_letter.append(contador_word)
      
      contador_word = contador_word+1
      letra_encontrada=False
    return same_position, same_letter

def print_word(word, same_letter_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ""
    i = 0
    while i < len(word):
      if(i in same_letter_position):
        transformed+=word[i].upper()
      elif(i in same_letter):
        transformed+=word[i].lower()
      else:
        transformed+="-"
      i+=1
    return transformed

    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    letras_excluidas = ("á", "é", "í", "ó", "ú")    
    f = open(filename, mode="rt", encoding="utf-8")
    linea = f.readline()
    palabras=[]
    excluir_palabra = False
    while linea != "" :
      #Eliminas los carcateres de salto de linea
      linea = linea.replace('\n',"")
      if(len(linea)==5):
        for c in linea:
          #Comprobamos que no tenga letras excluidas con ascentos
          if(c in letras_excluidas):
            excluir_palabra= True
        
        if(excluir_palabra==False):
          palabras.append(linea)
        excluir_palabra = False
      linea = f.readline()
    f.close()
    palabras_filtradas= []
    #Filtramos las 15 palabras aleatorias
    while len(palabras_filtradas) < 15:
      secret = random.choice(palabras)
      palabras_filtradas.append(secret)
      palabras.remove(secret)

    secret = random.choice(palabras_filtradas)
    return secret

 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    palabra_encontrada= False
    while palabra_encontrada == False:
      word = input("Introduce una palabra para comprabar si pertenece a la lista: ")
      if(word in selected):
        palabra_encontrada=True
      else:
        print("Introduzca una palabra valida!")
    return word


valid_words = ["tozar","risco","piocha","lomaje","merca","almea","borrar","tamtan","suma"]


if __name__ == "__main__":
    file = "palabras_extended.txt"
    secret=choose_secret_advanced(file)

    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        #word = input("Introduce una nueva palabra: ")
        word = check_valid_word(valid_words)
        same_position, same_letter = compare_words(word,secret)
        resultado=print_word(word,same_position, same_letter)
        print(resultado)
        if word.lower() == secret.lower():
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   

 
    

