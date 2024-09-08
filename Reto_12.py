def Cant_voc(archivo:str):

    """
    Esta función cuenta la cantidad de vocales que hay en un texto

    Args:
        Esta función recibe como argumento un string como archivo

    Returns:
        La función retorna Voc, que es un entero siendo el numero contado por la función  
    """

    txt=archivo.lower()
    Vocales=["a", "e", "i", "o", "u"]
    Voc=0
    for i in Vocales:
        Voc+=txt.count(i)
    return Voc

def Cant_cons(archivo:str):

    """
    Esta función cuenta la cantidad de consonantes que hay en un texto

    Args:
        Esta función recibe como argumento un string como archivo

    Returns:
        La función retorna Con, que es un entero siendo el numero contado por la función  
    """

    txt=archivo.lower()
    Consonantes=["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    Con=0
    for i in Consonantes:
        Con+=txt.count(i)
    return Con

def Cant_Pal(archivo:str):

    """
    Esta función cuenta la cantidad de repeticiones de cada palabra del texto

    Args:
        Esta función recibe como argumento un string como archivo

    Returns:
        La función retorna Top, que es una lista de strings conformada por las palabras y orden de mayor a menor reparación  
    """

    txt=archivo.split() # Separar l texto en una lista
    Pal=[]
    Cnt=[]
    Top=[]
    for i in txt: #Ciclo para contar las palabras
        if i in Pal:
            a=Pal.index(i)
            Cnt[a]+=1
        else:
            Pal.append(i)
            Cnt.append(1)
    Cnt_alt=Cnt.copy() # Otra lista para la cuenta de palabras
    Cnt_alt.sort(reverse=True) # Ordenar la lista
    Cnt_alt=Cnt_alt[:50] #Tomar solo los primeros 50 elementos de la lista
    for i in Cnt_alt: # Ciclo para ordenar las palabras repetidas
        a=Cnt.index(i)
        b=Pal[a]
        Top.append(f" {Pal[a]} Repetida {Cnt[a]}")
        Cnt.pop(a)
        Pal.pop(a)
    return Top


if __name__=="__main__":
    archivo:str = open("mbox.txt","r").read()
    Voc=Cant_voc(archivo)
    Cons=Cant_cons(archivo)
    Top=Cant_Pal(archivo)
    print(f"Vocales={Voc}")
    print(f"Consonantes={Cons}")
    for i in range(50): #Imprimir solo los primeros 50 elementos del "ranking"
        print(Top[i])