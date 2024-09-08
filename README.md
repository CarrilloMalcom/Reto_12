# Reto_12

### Soy Malcom Yamil Carrillo Quintero y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo
<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

## 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

### endswith:
Verifica si un string empieza en un valor o caracter determinado. Tiene la sintaxis ***string.endswith(Valor, Inicio, Fin)***

**Ejemplo:**

```python
string = "Hola amigos"

E_w = string.endswith("amigos")

print(E_w) # Imprimirá True
```


### startswith:
Verifica si un empieza en un valor o caracter determinado. Tiene la sintaxis ***string.startswith(Valor, Inicio, Fin)***


**Ejemplo:**

```python
string = "Hola amigos"

S_w = string.endswith("Hola")

print(S_w) # Imprimirá True
```

### isalpha:
Verifica si todos los carácteres del string son letras. Tiene la sintaxis ***string.isalpha()***

**Ejemplo:**

```python
string = "Hola"

I_a = string.isalpha()

print(I_a) # Imprimirá True
```

### isalnum:
Verifica si todos los carácteres del string son alfanumericos. Tiene la sintaxis ***string.isalnum()***

**Ejemplo:**

```python
string = "Hola123"

I_an = string.isalnum()

print(I_an) # Imprimirá True
```

### isdigit:
Verifica si todos los carácteres del string son numeros. Tiene la sintaxis ***string.isdigit()***

**Ejemplo:**

```python
string = "12345²"

I_d = string.isalnum()

print(I_d) # Imprimirá True
```

### isspace:
Verifica si todos los carácteres del string son espacios. Tiene la sintaxis ***string.isspace()***

**Ejemplo:**

```python
string = " "

I_s = string.isspace()

print(I_s) # Imprimirá True
```

### istitle:
Verifica si el string esta en formato de titulo, es decir, todas las primeras letras del texto estan en mayuscula. Tiene la sintaxis ***string.istitle()***

**Ejemplo:**

```python
string = "Hola Amigos, Como Va Todo"

I_t = string.istitle()

print(I_t) # Imprimirá True
```

### islower:
Verifica si el string esta en minuscula en su totalidad. Tiene la sintaxis ***string.islower()***

**Ejemplo:**

```python
string = "hola amigos"

I_l = string.islower()

print(I_l) # Imprimirá True
```

### isupper:
Verifica si el string esta en mayuscula en su totalidad. Tiene la sintaxis ***string.isupper()***

**Ejemplo:**

```python
string = "HOLA AMIGOS"

I_l = string.isupper()

print(I_l) # Imprimirá True
```


## 2.Procesar el archivo y extraer:

Cantidad de vocales
Cantidad de consonantes
Listado de las 50 palabras que más se repiten

```python
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
```



