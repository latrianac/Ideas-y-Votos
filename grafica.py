import numpy as np
import matplotlib.pyplot as plt

def graficar_promedio(nombre_usuario, nombre_idea, promedio_usuario, promedio_idea, promedio_general):

    objects = (nombre_usuario, nombre_idea, 'Promedio General')
    incomes = [promedio_usuario, promedio_idea, promedio_general]
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, incomes, align='center')
    plt.xticks(y_pos, objects)
    plt.ylabel('Promedio')
    plt.xlabel('Nombres')
    plt.title('Promedio en las Votaciones')
    plt.show()
