def menu_mostrar_peliculas(lista_peliculas:list[dict]) -> None:

    """
    Sub-menú para mostrar todas las peliculas, por determinado género, año de lanzamiento, por ATP -> Si o por ATP -> No 
    """
    while True:
        print("""
            1_  Todas las peliculas.
            2_ De determinado género.
            3_ De determinado año.
            4_ Todas las ATP.
            5_ Todas las no ATP.
            6_ Salir.
            """)
        
        opcion = input("Ingrese una opción: ")
        
        match opcion:
            case "1":
                mostrar_peliculas(lista_peliculas)
            case "2":
                genero = input("Ingrese género a filtrar: ")
                mostrar_peliculas(mostrar_peliculas_por_genero(lista_peliculas, genero))
            case "3":
                anio = input("Ingrese año a filtrar: ")
                mostrar_peliculas(mostrar_peliculas_por_anio(lista_peliculas, anio))
            case "4":
                mostrar_peliculas(mostrar_peliculas_por_atp(lista_peliculas))
            case "5":
                mostrar_peliculas(mostrar_peliculas_por_no_atp(lista_peliculas))
            case "6":
                break
            case _:
                print("Opcion incorrecta.")



def mostrar_peliculas(lista_peliculas:list[dict]) ->  None:
    """
    Recibe la lista de peliculas y las printea con formato
    """
    print("*********************************************************")
    print("| TITULO | GENERO | AÑO DE LANZAMIENTO | DURACION | ATP |")
    print("---------------------------------------------------------")
    for pelicula in lista_peliculas:

        print(f"| {pelicula['id']} | {pelicula['titulo']} | {pelicula['genero']} | {pelicula['anio_lanzamiento']} | {pelicula['duracion']} | {pelicula['apto_para_todo_publico']} |")
    print("**********************************************************")
def mostrar_peliculas_por_genero(lista_peliculas: list[dict], genero:str) -> list[dict]:
    """
    Utiliza una función lambda con filter para separar en una lista determinadas peliculas con un mismo género
    """
    peliculas_filtradas = filter(lambda pelicula: pelicula['genero'] == genero, lista_peliculas)
    return peliculas_filtradas

def mostrar_peliculas_por_anio(lista_peliculas: list[dict], anio:str) -> list[dict]:
    """
    Utiliza una función lambda con filter para separar en una lista determinadas peliculas con un mismo año de lanzamiento
    """
    peliculas_filtradas = filter(lambda pelicula: pelicula['anio_lanzamiento'] == anio, lista_peliculas)
    return peliculas_filtradas

def mostrar_peliculas_por_atp(lista_peliculas: list[dict], atp:str = True) -> list[dict]:
    """
    Utiliza una función lambda con filter para separar en una lista determinadas peliculas con ATP "Si"
    """
    peliculas_filtradas = filter(lambda pelicula: pelicula['apto_para_todo_publico'] == "Si" or  True, lista_peliculas)
    return peliculas_filtradas

def mostrar_peliculas_por_no_atp(lista_peliculas: list[dict], atp:str = False) -> list[dict]:
    """
    Utiliza una función lambda con filter para separar en una lista determinadas peliculas con ATP "No"
    """
    peliculas_filtradas = filter(lambda pelicula: pelicula['apto_para_todo_publico'] == "No" or False, lista_peliculas)
    return peliculas_filtradas