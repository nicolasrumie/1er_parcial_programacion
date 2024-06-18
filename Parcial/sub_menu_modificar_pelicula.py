def menu_modificar_pelicula(pelicula:dict) -> None:
    while True:
        print("""
            1_ Modificar título.
            2_ Modificar género.
            3_ Modificar año de lanzamiento.
            4_ Modificar duración.
            5_ Modificar ATP.
            6_ Salir.
            """)
        
        opcion = input("Ingrese una opción: ")
        opcion = int(opcion)
        
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Opcion incorrecta.")


def buscar_pelicula(lista_peliculas:list[dict], titulo:str) -> dict:
    for i in range(len(lista_peliculas)):
        if titulo == lista_peliculas[i]['titulo']:
            identificador = lista_peliculas[i]['id']
            break
        
    return identificador


    

        
    