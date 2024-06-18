def buscar_pelicula_por_titulo(lista_peliculas:list[dict], titulo:str) -> None:

    """
    Recibe la lista de peliculas y el titulo a buscar por parametro. Si lo encuentra, lo printea, si no, imprime que no se encontró
    """
    
    pelicula = list(filter(lambda pelicula: pelicula['titulo'] == titulo, lista_peliculas))
    if len(pelicula) == 0:
        print("No se encontro la pelicula")
    elif len(pelicula) > 0:
        print(f"| {pelicula[0]['titulo']} | {pelicula[0]['genero']} | {pelicula[0]['anio_lanzamiento']} | {pelicula[0]['duracion']} | {pelicula[0]['apto_para_todo_publico']} |")
