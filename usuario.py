import pickle
import datetime
from datetime import timedelta

class Usuario():
    def __init__(self, nombre_usuario):

        self.nombre = nombre_usuario
        print("Se ha creado una persona con el nombre de: ", self.nombre)

    def crear_idea(self, creador, nombre_idea, grupo, descripcion,
                  votos, calificacion):
        milista = ListaIdeas()
        idea = Idea(creador, nombre_idea, grupo, descripcion)
        milista.agregar_idea(idea)
        milista.mostrar_informacion_de_archivo_externo()


class ListaUsuarios():

    usuarios = []

    def __init__(self):
        lista_de_usuarios = open("usuarios", "ab+")
        lista_de_usuarios.seek(0)
        try:
            self.usuarios=pickle.load(lista_de_usuarios)

        except:
            print("El archivo usuarios esta vacio")
        finally:
            lista_de_usuarios.close()
            del(lista_de_usuarios)


    def agregar_usuario(self, u):
        self.usuarios.append(u)
        self.guardar_usuario_en_archivo_externo()

    def mostrar_usuario(self):
        for u in self.usuarios:
            print(u)

    def guardar_usuario_en_archivo_externo(self):
        lista_de_usuarios = open("usuarios", "wb")
        pickle.dump(self.usuarios, lista_de_usuarios)
        lista_de_usuarios.close()
        del(lista_de_usuarios)

    def retornar_informacion_de_archivo_externo(self):
        lista_de_usuarios = []
        for u in self.usuarios:
            lista_de_usuarios.append(u)
        return lista_de_usuarios

def seleccionar_usuario():
    milista = ListaUsuarios()
    lista_de_usuarios = milista.retornar_informacion_de_archivo_externo()
    nombre_usuario = input("Escriba su nombre de usuario: ")
    for u in lista_de_usuarios:
        if nombre_usuario == u.nombre:
            print("Bienvenido: ", nombre_usuario)
            return u
    print("El usuario no se encuentra registrado")
    return False

class Idea():

    def __init__(self, creador, nombre_idea, grupo, descripcion):
        self.creador = creador
        self.nombre_idea = nombre_idea
        self.grupo = grupo
        self.descripcion = descripcion
        self.votos = 0
        self.calificacion = 0
        self.fecha_inicio = self.fecha()
        self.fecha_final = self.fecha_inicio + timedelta(days=30)

    def fecha(self):
        year = int(input('Ingrese un año: '))
        month = int(input('Ingrese un mes: '))
        day = int(input('Ingrese un dia: '))
        date = datetime.date(year, month, day)
        return date
    def votar(self, voto):
        self.voto = voto

class ListaIdeas():

    ideas = []

    def __init__(self):
        lista_de_ideas = open("ideas", "ab+")
        lista_de_ideas.seek(0)
        try:
            self.ideas=pickle.load(lista_de_ideas)
            print("Se cargaron {} ideas del archivo ideas".format(len(self.ideas)))
        except:
            print("El archivo ideas esta vacio")
        finally:
            lista_de_ideas.close()
            del(lista_de_ideas)

    def agregar_idea(self, idea):
        self.ideas.append(idea)
        self.guardar_idea_en_archivo_externo()

    def mostrar_usuario(self):
        for idea in self.ideas:
            print(idea)

    def guardar_idea_en_archivo_externo(self):
        lista_de_ideas = open("ideas", "wb")
        pickle.dump(self.ideas, lista_de_ideas)
        lista_de_ideas.close()
        del(lista_de_ideas)


    def retornar_informacion_de_archivo_externo(self):
        lista_de_ideas = []
        for idea in self.ideas:
            lista_de_ideas.append(idea)
        return lista_de_ideas


def seleccionar_idea():
    milista = ListaIdeas()
    lista_de_ideas = milista.retornar_informacion_de_archivo_externo()
    nombre_idea = input("Escriba su nombre de la idea: ")
    for idea in lista_de_ideas:
        if nombre_idea == idea.nombre_idea:
            print("Esta es la idea: ", nombre_idea)
            return idea
    print("La idea no se encuentra registrada")
    return False

class Grupo():
    def __init__(self, nombre_grupo, usuarios):
        self.nombre_grupo = nombre_grupo
        self.usuarios = usuarios

class ListaGrupos():

    grupos = []

    def __init__(self):
        lista_de_grupos = open("grupos", "ab+")
        lista_de_grupos.seek(0)
        try:
            self.grupos=pickle.load(lista_de_grupos)
            print("Se cargaron {} grupos del archivo grupos".format(len(self.grupos)))
        except:
            print("El archivo grupos esta vacio")
        finally:
            lista_de_grupos.close()
            del(lista_de_grupos)


    def agregar_grupo(self, g):
        self.grupos.append(g)
        self.guardar_grupo_en_archivo_externo()

    def mostrar_grupo(self):
        for u in self.grupos:
            print(u)

    def guardar_grupo_en_archivo_externo(self):
        lista_de_grupos = open("grupos", "wb")
        pickle.dump(self.grupos, lista_de_grupos)
        lista_de_grupos.close()
        del(lista_de_grupos)

    def retornar_informacion_de_archivo_externo(self):
        lista_de_grupos = []
        for g in self.grupos:
            lista_de_grupos.append(g)
        return lista_de_grupos

def seleccionar_grupo():
    milista = ListaGrupos()
    lista_de_grupos = milista.retornar_informacion_de_archivo_externo()
    nombre_grupo = input("Escriba su nombre del grupo: ")
    for g in lista_de_grupos:
        if nombre_grupo == g.nombre_grupo:
            print("Selecciono el grupo: ", nombre_grupo)
            return g
    print("El grupo no se encuentra registrado")
    return False


class Voto():
    def __init__(self, nombre_usuario, idea, calificacion):
        self.calificacion = calificacion
        self.idea = idea
        self.nombre_usuario = nombre_usuario
        self.fecha = datetime.datetime.now()

class ListaVotos():

    votos = []

    def __init__(self):
        lista_de_votos = open("votos", "ab+")
        lista_de_votos.seek(0)
        try:
            self.votos=pickle.load(lista_de_votos)

        except:
            print("***")
        finally:
            lista_de_votos.close()
            del(lista_de_votos)


    def agregar_voto(self, u):
        self.votos.append(u)
        self.guardar_voto_en_archivo_externo()

    def mostrar_voto(self):
        for v in self.votos:
            print(v)

    def guardar_voto_en_archivo_externo(self):
        lista_de_votos = open("votos", "wb")
        pickle.dump(self.votos, lista_de_votos)
        lista_de_votos.close()
        del(lista_de_votos)

    def retornar_informacion_de_archivo_externo(self):
        lista_de_votos = []
        for v in self.votos:
            lista_de_votos.append(v)
        return lista_de_votos


def promedio_votos_usuario():
    milista = ListaVotos()
    usuario = seleccionar_usuario()
    lista_votos = milista.retornar_informacion_de_archivo_externo()
    calificacion = 0
    numero_de_votos = 0
    try:
        for v in lista_votos:
            if v.nombre_usuario.nombre==usuario.nombre:
                calificacion = calificacion + v.calificacion
                numero_de_votos = numero_de_votos + 1
        if numero_de_votos == 0:
            return print("El usuario no ha votado por alguna idea")
        else:
            promedio = calificacion/numero_de_votos
            print("El promedio de calificaciones del usuario es: ", promedio)
            return [promedio, usuario.nombre]
    except:
        print("Ocurrio un error en la identificación del usuario, intentelo de nuevo")


def promedio_votos_idea():
    milista = ListaVotos()
    idea = seleccionar_idea()
    lista_votos = milista.retornar_informacion_de_archivo_externo()
    calificacion = 0
    numero_de_votos = 0
    try:
        for v in lista_votos:
            if v.idea.nombre_idea == idea.nombre_idea:
                calificacion = calificacion + v.calificacion
                numero_de_votos = numero_de_votos + 1
        if numero_de_votos == 0:
            return print("La idea no ha recibido ningun voto")
        else:
            promedio = calificacion / numero_de_votos
            print("El promedio de calificaciones en la idea es: ", promedio)
            return [promedio, idea.nombre_idea]
    except:
        print("Ocurrio un error en la identificación de la idea, intentelo de nuevo")

def promedio_general():
    milista = ListaVotos()
    lista_votos = milista.retornar_informacion_de_archivo_externo()
    calificacion = 0
    numero_de_votos = 0
    for v in lista_votos:
            calificacion = calificacion + v.calificacion
            numero_de_votos = numero_de_votos + 1
    if numero_de_votos == 0:
        return print("No se ha realizado ninguna votacion")
    else:
        promedio = calificacion / numero_de_votos
        print("El promedio de calificaciones general es: ", promedio)
        return promedio
