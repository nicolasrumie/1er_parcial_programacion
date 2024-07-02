def dar_de_alta(lista_peliculas: list[dict], identificacion:int, titulo: str, genero: str, anio_lanzamiento: str, duracion: str, apto_para_todo_publico: str, plataformas: list[str])  -> None:

    """
    Recibe la lista de peliculas y todos los parametros necesarios para poder dar de alta una pelicula y la appendea a la lista de peliculas
    """

    
    pelicula = {
            "id" : identificacion,
            "titulo" : titulo,
            "genero" : genero,
            "anio_lanzamiento" : anio_lanzamiento,
            "duracion" : duracion,
            "apto_para_todo_publico" : apto_para_todo_publico,
            "plataformas" : plataformas
        }
    
    lista_peliculas.append(pelicula)


def menu_dar_de_alta(lista_peliculas:list[dict]) -> None:

    """
    Se encarga de recibir los datos ingresados por el usuario y los valida según dato 
    """
    
    identificacion = get_identificacion(lista_peliculas)
    titulo = validar_titulo()
    genero = validar_genero()
    anio_lanzamiento = validar_anio_lanzamiento()
    duracion = validar_duracion()
    apto_para_todo_publico = validar_atp()
    plataformas = validar_plataformas()
    print("Pelicula dada de alta correctamente. ")
    
    return dar_de_alta(lista_peliculas, identificacion, titulo, genero, anio_lanzamiento, duracion, apto_para_todo_publico, plataformas)

def get_identificacion(lista_peliculas:list[dict]) -> int:

    """
    Busca el ID máximo para asignarselo a la pelicula a dar de alta
    """

    maximo_id = 0
    print(maximo_id)
    bandera_maximo = True
    for i in range(1, len(lista_peliculas)):
        if bandera_maximo == True or int(lista_peliculas[i]['id']) > maximo_id:
            maximo_id = int(lista_peliculas[i]['id'])
            bandera_maximo = False
    
    return maximo_id + 1



def validar_titulo() -> str:

    """
    Recibe el string del titulo recibido por consola por el usuario, la valida y la devuelve
    """
    titulo = input("Introduzca titulo:")

    longitud_titulo = len(titulo)

    while longitud_titulo > 30 or titulo.isnumeric() == True:
        titulo = input("Reintroduzca título: ")
        longitud_titulo = len(titulo)

    return titulo

def validar_genero() -> str:

    """
    Recibe el string del genero recibido por consola por el usuario, la valida y la devuelve
    """
    
    lista_generos = ["Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica",
        "Comedia dramática", "Crimen", "Documental", "Drama", "Fantasía", "Histórico",
        "Infantil", "Musical", "Misterio", "Policíaco", "Romance", "Ciencia ficción",
        "Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental",
        "Familiar", "Superhéroes", "Espionaje", "Artes marciales", "Fantástico", "Catástrofe",
        "Melodrama", "Erótico", "Cine independiente", "Zombies", "Vampiros", "Cyberpunk",
        "Steampunk", "Distopía", "Utopía", "Road Movie", "Docuficción", "Mockumentary",
        "Gótico", "Slasher", "Adolescente", "Culto", "Maravilloso"]

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
    """
    Recibe el año de lanzamiento, la valida y la devuelve
    """
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

    """
    Recibe la duracion, la valida y la devuelve
    """
    duracion_pelicula = input("Introzuce duracion de la pelicula (min): ")
    while duracion_pelicula.isnumeric() != True:
            duracion_pelicula = input("Reingrese minutos (Sólo números y mayores a 0): ")
            if duracion_pelicula.isnumeric() == True:
                duracion_pelicula = int(duracion_pelicula)
                break
    duracion_pelicula = int(duracion_pelicula)

    return duracion_pelicula

def validar_atp() -> bool:

    """
    Recibe el ATP, si es "Si" -> True | "No" -> False
    """
    
    atp = input("ATP Si/No: ")
    veracidad = True

    if atp == "No":
        veracidad = False

    while atp != "Si" and atp != "No":
        atp = input("Reintroduzca ATP Si/No: ")

        if atp == "Si":
            veracidad = True
            break
        elif atp == "No":
            veracidad = False
            break
        
    
    return veracidad
        

def validar_plataformas() -> str:
    """
    Recibe las plataformas por el usuario, las valida, las pone en una lista y las devuelve en forma de str con separadores
    """

    plataformas = []

    ingresando = True

    while ingresando == True:
        plataforma_ingresada = input("Ingrese plataforma: ")

        if plataforma_ingresada.isalpha() == False or len(plataforma_ingresada) > 20:
            print("Plataforma invalida")
            continue

        plataformas.append(plataforma_ingresada)

        opcion = input("Desea seguir ingresando?")

        if opcion == "Si":
            ingresando = True
        elif opcion == "No":
            ingresando = False
    
    plataforma_str = "-".join(plataformas)
    
    return plataforma_str