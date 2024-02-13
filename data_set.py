import statistics
import matplotlib.pyplot as matplot

from main import data

# fonction

# nombre d'intervalle entre 0 et le plus grand nombre de la list
NUMBER_CLASS = 20


def get_largest_number(nb_list, largest_number=data[0]) -> int:
    # prend le nombre de points le plus elever de toutes les simulations

    for number in nb_list:
        if number > largest_number:
            largest_number = number
    return largest_number


largest = get_largest_number(data)


def create_final_list() -> list:
    # creer une list ou seront stocker les resultats
    final_list = []

    # creer la list final ( le plus 3 est pour bien avoir la fin de la coube )
    for i in range(NUMBER_CLASS + 8):
        final_list.append(0)

    return final_list


def create_limite_list() -> list:
    # une liste qui donne les differents intervalle au quelles les resultats des experiences peuvents appartenir
    limit_list = []
    inter = 1

    # creer la liste des limites entre les intervales
    for i in range(NUMBER_CLASS):
        limit_list.append(largest * inter / NUMBER_CLASS)
        inter += 1

    return limit_list


def result_of_data(limit_list, final_list) -> list:
    # met les valeurs dans les different classe

    for element in data:
        if element < limit_list[0]:
            final_list[0] += 1

        elif limit_list[0] < element < limit_list[1]:
            final_list[1] += 1

        elif limit_list[1] < element < limit_list[2]:
            final_list[2] += 1

        elif limit_list[2] < element < limit_list[3]:
            final_list[3] += 1

        elif limit_list[3] < element < limit_list[4]:
            final_list[4] += 1

        elif limit_list[4] < element < limit_list[5]:
            final_list[5] += 1

        elif limit_list[5] < element < limit_list[6]:
            final_list[6] += 1

        elif limit_list[6] < element < limit_list[7]:
            final_list[7] += 1

        elif limit_list[7] < element < limit_list[8]:
            final_list[8] += 1

        elif limit_list[8] < element < limit_list[9]:
            final_list[9] += 1

        elif limit_list[9] < element < limit_list[10]:
            final_list[10] += 1

        elif limit_list[10] < element < limit_list[11]:
            final_list[11] += 1

        elif limit_list[11] < element < limit_list[12]:
            final_list[12] += 1

        elif limit_list[12] < element < limit_list[13]:
            final_list[13] += 1

        elif limit_list[13] < element < limit_list[14]:
            final_list[14] += 1

        elif limit_list[14] < element < limit_list[15]:
            final_list[15] += 1

        elif limit_list[15] < element < limit_list[16]:
            final_list[16] += 1

        elif limit_list[16] < element < limit_list[17]:
            final_list[17] += 1

        elif limit_list[17] < element <= limit_list[18]:
            final_list[18] += 1

        elif limit_list[18] < element <= limit_list[19]:
            final_list[19] += 1

    return final_list


def get_ecrart_type():
    return statistics.pstdev(data)


def get_mediane():
    return statistics.median(data)


def get_moyenne():
    result = 0
    for i in data:
        result += i

    return result / len(data)


def chart_display(list_display) -> None:

    # creation du graphique
    matplot.plot(list_display)  # liste des points
    matplot.ylabel('nb dans la classe ')  # label de l'axe des y
    matplot.xlabel('classes')  # label de l'axe des x
    matplot.show()  # montre le graphique


def a():
    # affiche les résultats

    final_list = create_final_list()
    limit_list = create_limite_list()

    print(f'liste des limites: {limit_list}')

    list_display = result_of_data(limit_list, final_list)

    print(f'liste finale: {final_list}')

    print(f'moyenne: {get_moyenne()}')
    print(f'mediane: {get_mediane()}')
    print(f'ecart-type: {get_ecrart_type()}')

    # affichage du graphiquej
    chart_display(list_display)

