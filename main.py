import os
from usuario import *
import datetime
from grafica import graficar_promedio

def menu():

    #Función que limpia la pantalla y muestra nuevamente el menu

    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Crear un usuario")
    print("\t2 - Crear una idea")
    print("\t3 - Crear un grupo")
    print("\t4 - Votar una idea")
    print("\t5 - Graficar")
    print("\t9 - Salir")

while True:
    # Mostramos el menu
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu == "1":
        print("")
        milista = ListaUsuarios()
        user = input("Escriba el nombre de usuario: ")
        u = Usuario(user)
        milista.agregar_usuario(u)
        input("\npulsa una tecla para continuar")
    elif opcionMenu == "2":
        print("")
        usuario = seleccionar_usuario()
        grupo = seleccionar_grupo()
        if usuario and grupo:
            milista = ListaIdeas()
            nombre_de_idea = input("Escriba el nombre de la idea: ")
            descripcion_idea = input("Describa la idea: ")
            idea = Idea(usuario, nombre_de_idea, grupo, descripcion_idea)
            milista.agregar_idea(idea)
            print("Se agrego la idea: ", idea.nombre_idea, " correctamente")

        input("\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        print("")
        milista = ListaGrupos()
        usuario = seleccionar_usuario()
        lista_usuarios_grupo = []
        lista_usuarios_grupo.append(usuario)
        try:
            nombre_grupo = input("Escriba el nombre del grupo: ")
            mas_usuarios = input("¿Desea agregar mas usuarios al grupo? (si/no)")
            if mas_usuarios=="si":
                print("Escriba el nombre de los usuarios (estos ya deben estar registrados)")

                while True:
                    u = seleccionar_usuario()
                    lista_usuarios_grupo.append(u)
                    a = input("Si desea terminar esciba la palabra 'salir'\n"
                              "de lo contrario presione cualquier tecla: ")
                    if a == "salir":
                        break

            grupo = Grupo(nombre_grupo, lista_usuarios_grupo)
            milista.agregar_grupo(grupo)

        except:
            print("No se puede crear el grupo, intente de nuevo")

        input("\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        print("")

        usuario = seleccionar_usuario()
        idea = seleccionar_idea()
        milista = ListaVotos()
        permiso = True
        lista_votos = milista.retornar_informacion_de_archivo_externo()
        for v in lista_votos:
            if v.nombre_usuario.nombre==usuario.nombre and v.idea.nombre_idea==idea.nombre_idea:
                permiso = False
            else:
                permiso = True
            if permiso:
                print("El usuario tiene permitido votar")
            else:
                print("El usuarino NO tiene permitido votar")

        if permiso:
            hoy = datetime.datetime.now()
            limite = datetime.datetime.combine(idea.fecha_final, datetime.time(0, 0))
            if hoy <= limite:
                print("Se puede votar")
                calificacion = int(input("Ingrese la calificicacion a esta idea: (0-10)"))
                if calificacion >= 0 and calificacion <= 10:
                    voto_idea = Voto(usuario, idea, calificacion)
                    milista.agregar_voto(voto_idea)
                    print("El voto se creo correctamente")
                else:
                    print("La calificacion esta fuera del rango establecido (0-10)")
            else:
                print("La idea ya no es vigente")




        input("\npulsa una tecla para continuar")

    elif opcionMenu == "5":
        print("")

        promedio_usuario = promedio_votos_usuario()
        promedio_idea = promedio_votos_idea()
        promedio_general = promedio_general()
        try:
            graficar_promedio(promedio_usuario[1], promedio_idea[1], promedio_usuario[0], promedio_idea[0], promedio_general)
        except:
            print("Verifique que no haya errores tipograficos en los campos ingresados")


        input("\npulsa una tecla para continuar")
    elif opcionMenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")











