def menu_calcular_promedio(lista_peliculas:list[dict]) -> None:

    """
    Sub-menú calcular promedio por año de lanzamiento y por duración
    """
    while True:
        print("""
            1_  Año de lanzamiento.
            2_ Duración de peliculas.
            3_ Salir.  
            """)
        
        opcion = input("Ingrese una opción: ")
        opcion = int(opcion)
        

        match opcion:
            case 1:
                calcular_promedio_anio_lanzamiento(lista_peliculas)
            case 2:
                calcular_promedio_duracion(lista_peliculas)
            case 3:
                break
            case _:
                print("Opcion incorrecta.")


def calcular_promedio_anio_lanzamiento(lista_peliculas:list[dict]) -> None:
    """
    Recibe la lista de peliculas
    Suma todos los años de lanzamiento de todas las peliculas y hace el promedio
    """
    acumulador = 0
    for pelicula in lista_peliculas:
        anio_pelicula = int(pelicula['anio_lanzamiento'])
        acumulador += anio_pelicula
    
    promedio_anio_lanzamiento = acumulador / len(lista_peliculas)
    promedio_anio_lanzamiento = int(promedio_anio_lanzamiento)

    print(f"El promedio de año de lanzamiento es: {promedio_anio_lanzamiento}")

def calcular_promedio_duracion(lista_peliculas:list[dict]) -> None:
    """
    Recibe la lista de peliculas
    Suma la duracion de todas las peliculas y hace el promedio
    """
    acumulador = 0
    for pelicula in lista_peliculas:
        duracion_pelicula = int(pelicula['duracion'])
        acumulador += duracion_pelicula
    
    promedio_duracion = acumulador / len(lista_peliculas)
    print(f"El promedio de duración es: {promedio_duracion}")
        