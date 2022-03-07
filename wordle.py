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

    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
 
def check_valid_word():
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """

if __name__ == "__main__":
    file = "palabras_reduced.txt"
    secret=choose_secret(file)
    lista1 , lista2 = compare_words("CAMPO", "CREMA")
    palabra = print_word("CAMPO", lista1, lista2)
    print(palabra)
    

