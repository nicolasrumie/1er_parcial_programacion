from sub_menu_dar_de_alta import *

def menu_modificar_pelicula(pelicula:dict) -> None:
    while True:
        if pelicula == None:
            print("No existe ninguna pelicula con ese título. ")
            break

        print("""
            1_ Modificar título.
            2_ Modificar género.
            3_ Modificar año de lanzamiento.
            4_ Modificar duración.
            5_ Modificar ATP.
            6_ Salir.
            """)
        
        opcion = input("Ingrese una opción: ")
        
        match opcion:
            case "1":
                nuevo_titulo = validar_titulo()
                pelicula['titulo'] = nuevo_titulo
                print("Se modificó correctamente el titulo. ")
            case "2":
                nuevo_genero = validar_genero()
                pelicula["genero"] = nuevo_genero
                print("Se modificó correctamente el género. ")
            case "3":
                nuevo_anio_lanzamiento = validar_anio_lanzamiento()
                pelicula["anio_lanzamiento"] = nuevo_anio_lanzamiento
                print("Se modificó correctamente el año de lanzamiento. ")
            case "4":
                nueva_duracion = validar_duracion()
                pelicula["duracion"] = nueva_duracion
                print("Se modificó correctamente la duración. ")
            case "5":
                nuevo_atp = validar_atp()
                pelicula["apto_para_todo_publico"] = nuevo_atp
                print("Se modificó correctamente el ATP. ")
            case "6":
                return pelicula
            case _:
                print("Opcion incorrecta.")


def buscar_pelicula(lista_peliculas:list[dict], filtrar_titulo:str) -> dict:
    flag = True
    for i in range(len(lista_peliculas)):
        if filtrar_titulo == lista_peliculas[i]['titulo']:
            identificador = lista_peliculas[i]
            flag = False
            break
    if flag == True:
        return None

        
    return identificador


    

        
    