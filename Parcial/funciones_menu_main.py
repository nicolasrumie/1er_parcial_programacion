def dar_de_alta(lista:list) -> dict:
    
    for i in range(len(lista) , -1):
        identificacion = lista[i]["identificacion"] + 1

    titulo = validar_titulo()
    genero = validar_genero()
    anio_lanzamiento = validar_anio_lanzamiento()
    duracion = validar_duracion
    apto_para_todo_publico = input("Introduzca ATP (Si/No): ")
    plataformas = input("Introduzca plataformas: ")

    pelicula_a_agregar = {
            "identificacion" : identificacion,
            "titulo" : titulo,
            "genero" : genero,
            "anio_lanzamiento" : anio_lanzamiento,
            "duracion" : duracion,
            "apto_para_todo_publico" : apto_para_todo_publico,
            "plataformas" : plataformas
        }

    return pelicula_a_agregar


def validar_titulo() -> str:
    titulo = input("Introduzca titulo:")

    longitud_titulo = len(titulo)

    while longitud_titulo > 30 or titulo.isalnum() == False:
        titulo = input("Reintroduzca título: ")
        longitud_titulo = len(titulo)

    return titulo

def validar_genero() -> str:
    lista_generos = ["Acción", "Aventura", "Animación", "Biográfico"]

    genero = input("Introduzca género: ")
    bandera = True
    while bandera == True:
        for i in range(len(lista_generos)):
            genero_a_comparar = lista_generos[i]
            if genero == genero_a_comparar:
                bandera = False
                break
        if bandera == True:
            print("Error. No se encuentra ese género.")
            genero = validar_genero()
            

    return genero

def validar_anio_lanzamiento() -> int:
    anio_lanzamiento = input("Ingrese año de lanzamiento: ")

    while anio_lanzamiento.isnumeric() != True:
            anio_lanzamiento = input("Reingrese año de lanzamiento (Solo números): ")
            if anio_lanzamiento.isnumeric() == True:
                break
                
            
    anio_lanzamiento = int(anio_lanzamiento)

    while anio_lanzamiento > 2024 or anio_lanzamiento < 1888:
            anio_lanzamiento = input("Reingrese año de lanzamiento (1888-2024): ")
            while anio_lanzamiento.isnumeric() != True:
                anio_lanzamiento = input("Reingrese año de lanzamiento (Solo números): ")
            if anio_lanzamiento.isnumeric() == True:
                anio_lanzamiento = int(anio_lanzamiento)


    return anio_lanzamiento

def validar_duracion() -> int:
    duracion_pelicula = input("Introzuce duracion de la pelicula (min): ")
    while duracion_pelicula.isnumeric() != True:
        duracion_pelicula = input("Reingrese minutos (Sólo números): ")
        if duracion_pelicula.isnumeric() == True:
            duracion_pelicula = int(duracion_pelicula)
            break

    while duracion_pelicula < 0:
        duracion_pelicula = input("Reingrese minutos (Mayor a 0): ")
        duracion_pelicula = int(duracion_pelicula)

    return duracion_pelicula


