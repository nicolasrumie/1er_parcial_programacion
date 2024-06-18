def menu_ordenar_pelicula(lista_peliculas:list[dict]) -> None:

    """
    Abre el sub-menú para ordenar peliculas por título, género, año de lanzamiento y por duración 
    """

    while True:
        print("""
            1_ Ordenar por título.
            2_ Ordenar por género.
            3_ Ordenar por año de lanzamiento.
            4_ Ordenar por duración.
            5_ Salir.
            """)
        
        opcion = input("Ingrese una opción: ")
        opcion = int(opcion)
        
        match opcion:
            case 1:
                forma_int = None
                forma = input("Ascendente (1) | Descendente (2): ")
                if forma.isnumeric() == True:
                    forma_int = int(forma)
                if forma_int == 1 or forma_int == 2:
                    forma = int(forma)
                else:
                    while forma.isalnum() == True:
                        forma = input("Error. Reingrese forma: ")
                        if forma.isnumeric() == True:
                            forma_int = int(forma)
                            if forma_int == 1 or forma_int == 2:
                                break

                forma = int(forma)
                
                if forma == 1:
                    bubble_sort(lista_peliculas, 'titulo')
                    print("Peliculas ordenadas por titulo ascendentemente")
                else:
                    bubble_sort_descendente(lista_peliculas, 'titulo')
                    print("Peliculas ordenadas por titulo descendentemente")

            case 2:
                forma_int = None
                forma = input("Ascendente (1) | Descendente (2): ")
                if forma.isnumeric() == True:
                    forma_int = int(forma)
                if forma_int == 1 or forma_int == 2:
                    forma = int(forma)
                else:
                    while forma.isalnum() == True:
                        forma = input("Error. Reingrese forma: ")
                        if forma.isnumeric() == True:
                            forma_int = int(forma)
                            if forma_int == 1 or forma_int == 2:
                                break

                if forma == 1:
                    bubble_sort(lista_peliculas, 'genero')
                    print("Peliculas ordenadas por genero ascendentemente")
                else:
                    bubble_sort_descendente(lista_peliculas, 'genero')
                    print("Peliculas ordenadas por genero descendentemente")
            case 3:
                forma_int = None
                forma = input("Ascendente (1) | Descendente (2): ")
                if forma.isnumeric() == True:
                    forma_int = int(forma)
                if forma_int == 1 or forma_int == 2:
                    forma = int(forma)
                else:
                    while forma.isalnum() == True:
                        forma = input("Error. Reingrese forma: ")
                        if forma.isnumeric() == True:
                            forma_int = int(forma)
                            if forma_int == 1 or forma_int == 2:
                                break

                if forma == 1:
                    bubble_sort(lista_peliculas, 'anio_lanzamiento')
                    print("Peliculas ordenadas por año de lanzamiento ascendentemente")
                else:
                    bubble_sort_descendente(lista_peliculas, 'anio_lanzamiento')
                    print("Peliculas ordenadas por año de lanzamiento descendentemente")
            case 4:
                forma_int = None
                forma = input("Ascendente (1) | Descendente (2): ")
                if forma.isnumeric() == True:
                    forma_int = int(forma)
                if forma_int == 1 or forma_int == 2:
                    forma = int(forma)
                else:
                    while forma.isalnum() == True:
                        forma = input("Error. Reingrese forma: ")
                        if forma.isnumeric() == True:
                            forma_int = int(forma)
                            if forma_int == 1 or forma_int == 2:
                                break

                if forma == 1:
                    bubble_sort(lista_peliculas, 'duracion')
                    print("Peliculas ordenadas por duracion ascendentemente")
                else:
                    bubble_sort_descendente(lista_peliculas, 'duracion')
                    print("Peliculas ordenadas por duracion descendentemente")
            case 5:
                break
            case _:
                print("Opcion incorrecta.")

def bubble_sort(lista_peliculas:list[dict], clave:str) -> None:

    """
    Filtrado Bubble Sort, filtra ascendentemente
    """

    for j in range (len(lista_peliculas)):
        intercambio = False
        for i in range(len(lista_peliculas)-1 -j):
            if lista_peliculas[i][clave] > lista_peliculas[i + 1][clave]:
                auxiliar = lista_peliculas[i][clave]
                lista_peliculas[i][clave] = lista_peliculas[i + 1][clave]
                lista_peliculas[i + 1][clave] = auxiliar
                intercambio = True
        if intercambio == False:
            break

def bubble_sort_descendente(lista_peliculas:list[dict], clave:str) -> None:

    """
    Filtrado Bubble Sort, filtra descendientemente
    """

    for j in range (len(lista_peliculas)):
        intercambio = False
        for i in range(len(lista_peliculas)-1 -j):
            if lista_peliculas[i][clave] < lista_peliculas[i + 1][clave]:
                auxiliar = lista_peliculas[i][clave]
                lista_peliculas[i][clave] = lista_peliculas[i + 1][clave]
                lista_peliculas[i + 1][clave] = auxiliar
                intercambio = True
        if intercambio == False:
            break