def menu_calcular_porcentaje(lista_peliculas:list[dict]) -> None:

    """
    Sub-menú de calcular porcentaje por genero y por atp
    """

    while True:
        print("""
            1_  Porcentaje por género.
            2_ Porcentaje por ATP.
            3_ Salir.  
            """)
        
        opcion = input("Ingrese una opción: ")
        
        match opcion:
            case "1":
                calcular_porcentajes_por_genero(lista_peliculas)
            case "2":
                calcular_porcentajes_por_atp(lista_peliculas)
            case "3":
                break
            case _:
                print("Opcion incorrecta.")

def calcular_porcentajes_por_genero(lista_peliculas: list[dict]) -> None:
    
    """
    Utiliza una función lambda que cuenta cuantas veces se repite cada género
    """
    generos = map(lambda x: x['genero'], lista_peliculas)

    generos_unicos = list(dict.fromkeys(generos))

    for genero in generos_unicos:
        calcular_porcentaje_por_genero(lista_peliculas, genero)

def calcular_porcentaje_por_genero(lista_peliculas:list[dict], genero: str) -> None:
    
    """
    Recibe el cuantas veces se repitió el género y hace el calculo de porcentaje
    """
    contador_genero = 0
    for pelicula in lista_peliculas:
        if pelicula['genero'] == genero:
            contador_genero += 1

    if contador_genero == 0:
        porcentaje_genero == 0
        
    elif contador_genero >= 1:
        porcentaje_genero = (len(lista_peliculas) * contador_genero) / 100

    print(f"El porcentaje de películas con género {genero} es {porcentaje_genero}%")


def calcular_porcentajes_por_atp(lista_peliculas: list[dict]) -> None:
    
    """
    Utiliza una función lambda que cuenta cuantas veces se repite cada atp (Si/No)
    """
    atps = map(lambda x: x['apto_para_todo_publico'], lista_peliculas)

    atps_distintos = list(dict.fromkeys(atps))

    for atp in atps_distintos:
        calcular_porcentaje_por_atp(lista_peliculas, atp)

def calcular_porcentaje_por_atp(lista_peliculas:list[dict], atp:str) -> None:
    
    """
    Recibe el cuantas veces se repitió el atp y hace el calcula" de porcentaje
    """

    contador_atp = 0

    for pelicula in lista_peliculas:
        if pelicula['apto_para_todo_publico'] == atp:
            contador_atp += 1

    if contador_atp == 0:
        porcentaje_atp = 0
    elif contador_atp >= 1:
        porcentaje_atp = (len(lista_peliculas) * contador_atp) / 100

    print(f"El porcentaje de películas con ATP {atp} es {porcentaje_atp}%")
    