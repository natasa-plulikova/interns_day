# Project of Stefan Otto Novak
# Umela Intelingencia - Klasifikator

from math import sqrt
import matplotlib.pyplot as plt
import operator
import random

K = 0
DOTS = []
CLASSIFIED_DOTS = []
CLASSIFIED1_DOTS = []
CLASSIFIED3_DOTS = []
CLASSIFIED7_DOTS = []
CLASSIFIED15_DOTS = []

DIFERENT_COLOR = 0
DIFERENT1_COLOR = 0
DIFERENT3_COLOR = 0
DIFERENT7_COLOR = 0
DIFERENT15_COLOR = 0
CLASSIFI_4METHOD = True


class Dot:
    def __init__(self, x, y, color):
        self.x = int(x)
        self.y = int(y)
        self.color = str(color)


def generate_starting_dots():
    starting_dots = [[-4500, -4400, "r"], [-4100, -3000, "r"], [-1800, -2400, "r"], [-2500, -3400, "r"], [-2000, -1400, "r"],
                     [4500, -4400, "g"], [4100, -3000, "g"], [1800, -2400, "g"], [2500, -3400, "g"], [2000, -1400, "g"],
                     [-4500, 4400, "b"], [-4100, 3000, "b"], [-1800, 2400, "b"], [-2500, 3400, "b"], [-2000, 1400, "b"],
                     [4500, 4400, "m"], [4100, 3000, "m"], [1800, 2400, "m"], [2500, 3400, "m"], [2000, 1400, "m"]] # m = Magenta ~ Purple

    for s_dot in starting_dots:
        new_dot = Dot(s_dot[0], s_dot[1], s_dot[2])     # Vytvorim nove instancie startovacich bodo
        DOTS.append(new_dot)                            # a nasledne ich prida do pola nekalsifikovancych

        if CLASSIFI_4METHOD == False:
            CLASSIFIED_DOTS.append(new_dot)                 # a do klasifikovanych bodov - pre konkretne k
        else:
            CLASSIFIED1_DOTS.append(new_dot)                # a do klasifikovanych bodov - pre stvorite klasifikovanie
            CLASSIFIED3_DOTS.append(new_dot)
            CLASSIFIED7_DOTS.append(new_dot)
            CLASSIFIED15_DOTS.append(new_dot)


def calculate_distance(dot1, dot2):
    distance = 0                        # Vypocita vzdialensot pomocou Eukleidovsej metrike
    distance += (dot1.x - dot2.x) ** 2
    distance += (dot1.y - dot2.y) ** 2
    distance = int(sqrt(distance))
    return distance


def k_NN(dot, k, dots):   #k-nearest neighbors algorithm
    distance_to_dot = []
    neighbors = []

    for clsf_dot in dots:
        distance = calculate_distance(dot, clsf_dot)
        distance_to_dot.append([clsf_dot, distance])

    distance_to_dot.sort(key=operator.itemgetter(1))   # Zoradenie podal dlzky (2. prvok). Prvy bude najblizsy sused

    for i in range(k):                          # Zoberie iba prvych k susedov
        neighbors.append(distance_to_dot[i])

    return neighbors


def classify(dot, k: int, dots):
    red = green = blue = magenta = 0
    neighbors = k_NN(dot, k, dots)

    for neighbor in neighbors:          # Urobi evidenciu farby susedov
        if (neighbor[0].color) == "r":
            red += 1

        if (neighbor[0].color) == "g":
            green += 1

        if (neighbor[0].color) == "b":
            blue += 1

        if (neighbor[0].color) == "m":
            magenta += 1

    colors = {"r": red, "g": green, "b": blue, "m": magenta}    # Kniznica pre vratenie farby s najvacsim vyskitom - pomocou max funkcie
    color = max(colors, key=colors.get)

    new_dot = Dot(dot.x, dot.y, color)      # Novy kalsifikovany bod. Zachova suradnice origanlenho bodu, ale farba moze byt rozdielna.
    return new_dot


def generate_colored_dot(x_from, x_to, y_from, y_to, color):
    global DOTS, CLASSIFIED_DOTS, CLASSIFIED1_DOTS, CLASSIFIED3_DOTS, CLASSIFIED7_DOTS, CLASSIFIED15_DOTS, DIFERENT_COLOR, DIFERENT1_COLOR, DIFERENT3_COLOR, DIFERENT7_COLOR, DIFERENT15_COLOR

    x_random = random.randint(x_from, x_to)     # Nahodne suradnice
    y_random = random.randint(y_from, y_to)

    dot = Dot(x_random, y_random, color)    # Instancia noveho bodu

                                            # Unikatne suradnice
    while DOTS.__contains__(dot):           # Ak nahodou existuje bod s tymito suradnicamy,
        y_random = random.randint(y_from, y_to)     # tak generuj novu instanciu s inym y,
        dot = Dot(x_random, y_random, color)        # az kym bude mat unikatne suradnice


    random_color = random.randint(1, 100)   # 99% pravdepodobnost farby jeho kvadrantu
    if random_color == 100:                 # Ak bude 100, tak toto je 1% pripad inej farby
        list_of_colors = ["r", "g", "b", "m"]
        random_color = random.choice(list_of_colors)    # Vyberie nahodnu farbu, ktora musi byt rozdielna
        while dot.color == random_color:                # od originalnej farby
            random_color = random.choice(list_of_colors)
        dot.color = random_color

    DOTS.append(dot)        # Tuna uz dot bude finalny bod, prida ho do pola bodov

    if CLASSIFI_4METHOD == False:   # Klasifikovat iba specifickym k
        clsf_dot = classify(dot, K, CLASSIFIED_DOTS)

        if dot.color != clsf_dot.color:     # Uspesnost
            DIFERENT_COLOR += 1             # Pocitanie rozdielnych tried (farb)
        CLASSIFIED_DOTS.append(clsf_dot)    # Tuna uz clsf_dot bude finalny kalsifikovany bod, prida ho do pola kalsifikovanych bodov

    else:   # To iste ako pre specificky k, iba tu sa spusit pre vsetky 4 k (,1, 3, 7, 15)
        clsf1_dot = classify(dot, 1, CLASSIFIED1_DOTS)
        clsf3_dot = classify(dot, 3, CLASSIFIED3_DOTS)
        clsf7_dot = classify(dot, 7, CLASSIFIED7_DOTS)
        clsf15_dot = classify(dot, 15, CLASSIFIED15_DOTS)

        if dot.color != clsf1_dot.color:     # Uspesnost
            DIFERENT1_COLOR += 1             # Pocitanie rozdielnych tried (farb)

        if dot.color != clsf3_dot.color:     # Uspesnost
            DIFERENT3_COLOR += 1             # Pocitanie rozdielnych tried (farb)

        if dot.color != clsf7_dot.color:     # Uspesnost
            DIFERENT7_COLOR += 1             # Pocitanie rozdielnych tried (farb)

        if dot.color != clsf15_dot.color:     # Uspesnost
            DIFERENT15_COLOR += 1             # Pocitanie rozdielnych tried (farb)

        CLASSIFIED1_DOTS.append(clsf1_dot)    # Tuna uz clsf_dot bude finalny kalsifikovany bod, prida ho do pola kalsifikovanych bodov
        CLASSIFIED3_DOTS.append(clsf3_dot)
        CLASSIFIED7_DOTS.append(clsf7_dot)
        CLASSIFIED15_DOTS.append(clsf15_dot)


def generate_dots(n_dots):
    for i in range(int(n_dots / 4)):                     # Tymto cyklo je zaistene, ze nový bod bude mat zakazdym inu triedu
        generate_colored_dot(-5000, 0, -5000, 0, "r")    # Cerveny
        generate_colored_dot(0, 5000, -5000, 0, "g")     # Zeleny
        generate_colored_dot(-5000, 0, 0, 5000, "b")     # Modry
        generate_colored_dot(0, 5000, 0, 5000, "m")      # Fialovy - Magenta


def display_plot(dots, k, n_dots):
    for dot in dots:                # Vykresly kazdy bod
        plt.scatter(dot.x, dot.y, color=dot.color)

    if k == 0:                      # Ked k = 0, tak vypisuje neklasifikovane body
        title = "Without classification. - dots: " + str(n_dots)
    else:
        title = "With classification. k: " + str(k) + " - dots: " + str(n_dots)
    plt.title(title)                # Pridat nadpis
    plt.grid()                      # Pridat orientacne ciary
    plt.show()                      # Vykreslit na plot


def main():
    global K, CLASSIFI_4METHOD

    command = input("Do you want to classify with all 4 methods? (k = 1, 3, 7, 15) [yes/no]: ")  # Nastavit ako bude
    while command != "yes" and command != "no":                                                  # program fungovat
        command = input("Please type again: [yes/no]: ")

    if command == "no":
        K = int(input("Inser k: "))
        CLASSIFI_4METHOD = False

    n_dots = int(input("Insert the number of dots: "))


    generate_starting_dots()   # Generovanie startovaciach bodov
    generate_dots(n_dots)      # Generovanie vsetkych bodov

    display_plot(DOTS, 0, n_dots)    #Vypis bez kalsifikacie

    if CLASSIFI_4METHOD == False:   # Vypis specificky k
        display_plot(CLASSIFIED_DOTS, K, n_dots)
        accuracy = 100 * float(-1 * (DIFERENT_COLOR - n_dots))/float(n_dots)
        print("Accuracy of classifier:", accuracy, "%")

    else:                                     # Vypsi stovrite klasifikovanie
        display_plot(CLASSIFIED1_DOTS, 1, n_dots)
        display_plot(CLASSIFIED3_DOTS, 3, n_dots)
        display_plot(CLASSIFIED7_DOTS, 7, n_dots)
        display_plot(CLASSIFIED15_DOTS, 15, n_dots)

        accuracy = 100 * float(-1 * (DIFERENT1_COLOR - n_dots))/float(n_dots)
        print("Accuracy of classifier k = 1:", accuracy, "%")

        accuracy = 100 * float(-1 * (DIFERENT3_COLOR - n_dots))/float(n_dots)
        print("Accuracy of classifier k = 3:", accuracy, "%")

        accuracy = 100 * float(-1 * (DIFERENT7_COLOR - n_dots))/float(n_dots)
        print("Accuracy of classifier k = 7:", accuracy, "%")

        accuracy = 100 * float(-1 * (DIFERENT15_COLOR - n_dots))/float(n_dots)
        print("Accuracy of classifier k = 15:", accuracy, "%")


if __name__ == "__main__":
    main()