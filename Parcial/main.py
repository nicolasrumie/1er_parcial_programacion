from funciones_menu_main import *

dar_de_alta_csv = open("Parcial\peliculas.csv", "r")
lineas = dar_de_alta_csv.readlines()
dar_de_alta_csv.close()

lista_peliculas = []
for i in range(1, len(lineas)):

    datos = lineas[i]
    datos = datos.split(",")
    identificacion = datos[0]
    titulo = datos[1]
    genero = datos[2]
    anio_lanzamiento = datos[3]
    duracion = datos[4]
    apto_para_todo_publico = datos[5]
    plataformas = datos[6]
    plataformas = plataformas.replace("\n", "")

    pelicula = {
            "identificacion" : identificacion,
            "titulo" : titulo,
            "genero" : genero,
            "anio_lanzamiento" : anio_lanzamiento,
            "duracion" : duracion,
            "apto_para_todo_publico" : apto_para_todo_publico,
            "plataformas" : plataformas
        }

    lista_peliculas.append(pelicula)

# for i in range(len(lista_peliculas)):
#     print("ID: ", lista_peliculas[i]["identificacion"])
#     print("Titulo: ", lista_peliculas[i]["titulo"])
#     print("Nombre: ", lista_peliculas[i]["genero"])
#     print("Año: ", lista_peliculas[i]["anio_lanzamiento"])
#     print("Duración (minutos): ", lista_peliculas[i]["duracion"])
#     print("ATP: ", lista_peliculas[i]["apto_para_todo_publico"])
#     print("Plataformas: ", lista_peliculas[i]["plataformas"])
#     print("----------------------------------------------------------")


while True:
    print("""
            Bienvenido a nuestro menú:
        1_ Dar de alta.
        2_ Modificar película.
        2_ Eliminar película.
        4_ Mostrar películas.
        5_ Ordenar películas.
        6_ Buscar película (título).
        7_ Calcular promedio (año o duración).
        8_Calcular porcentaje (género o ATP).
        9_ Salir. """)
    
    eleccion = int(input("Ingrese opción a elegir: "))
    

    match eleccion:
        case 1:
            pelicula_a_agregar = dar_de_alta(lista_peliculas)
            lista_peliculas.append(pelicula_a_agregar)
        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass
            
        case 6:
            pass

        case 7:
            pass

        case 8:
            pass

        case 9:
            print("¡Gracias por usar nuestro programa!")
            break

        case _:
            print("Eleccion incorreta. (1-8) sino 9 para salir.")

