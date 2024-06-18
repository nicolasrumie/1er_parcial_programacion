def eliminar_pelicula(lista_peliculas:list[dict], titulo:str) -> None:

    """
    Recibe en titulo a eliminar por parametro y lo elimina de la lista de peliculas
    """
    
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]['titulo'] == titulo:
            lista_peliculas.pop(i)
            print(f"La pelicula {titulo} fue eliminada.")
            return
        
    print("No se encontró la pelicula.")

        