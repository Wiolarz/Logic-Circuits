"""

"For the function given in the array, compute all the minimum sets of arguments with the least number of arguments.
The variables necessary for this function are x1  x2"

Task Description in Polish:

Opis wyjaśniający jak wykonywać zadanie:

Dane wejściowe:
tablica oraz para wartości X

Krok 1:
Uzyskujemy wartości:
Px1, Px2, Pf
zależnie od kolumny wypisujemy lokacje gdzie znajdują się wartości 1

musimy rezultat zapisać uwzględniając pozostałe wartości czyli:
Px1 = 1  Px2 = 2 tablica to np.
k  x1 x2 x3 f
1  1  0  0  1
2  0  1  1  0


ale zapisujemy jako
P1 = {2; 1}
P2 = {1; 2}
Pf = {2; 1}

ALE dla reszty zadania o tym zapomnijmy i traktujmy Px1/Px2/Pf jako zbiór lokalizacji jedynek
czyli np. P1 = {1}

Krok 2:
"Mnożymy" Px1 przez Px2, w praktyce oznacza to:
tworzymy od 2 do 4 grup liczb w oparciu o zasady:
1 grupa: lokalizacje które są 1 w Px1 i Px2
2 grupa: lokalizacje które są 1 w Px1 ale które już się nie pojawiły w 1 grupie
3 grupa: tak samo jak grupa 2 tylko że dla Px2
4 grupa: Reszta liczb
np. P1 * P2:
P1 = {1}  P2 = {2}
więc  P1 * P2 = {1, 2} i mamy 2 puste grupy (1 i 4)

Krok 3:
wykonujemy podobnie jak krok drugi wykorzystujemy tablice {Px1 * Px2} i Pf
By wykonać ten krok najlepiej zastosować metodę:
Tworzymy nową tablicę wynikową:
idziemy po każdym elemencie tablicy Pf:
Przypisujemy każdy element w miejsce gdzie znajduje się on w {Px1 * Px2} (czyli w jednej z 4 grup)

w momencie gdy wszystko jest przypisane, tworzymy teraz nową "Połowę" w każdej grupie:
lecimy teraz po każdej liczbie z {Px1 * Px2} której jeszcze nie przenieśliśmy
i umieszczamy ją w tej grupie co była w {Px1 * Px2}  ALE odzielamy je wszystkie nawiasami

uzyskujemy od 1 do 8' grup (ciągle mamy 4 grupy odzielone średnikami ";" a podgrupy trzymamy w odzielnych nawiasach


Krok 4:
Dla każdej GRUPY z kroku 3 tworzymy pary między podgrupami
np dla krok 3: {(1), (4, 6); (2), (3); (5); (7)}
tworzy nam:
1 4
1 6
oraz
2 3

Teraz dla każdej pary wypisujemy pary lokalizacje gdzie wartości są różne
czyli: w 1-4 lecimy po każdej wartości x dla rzędu 1 i 4
mamy wynik: 1, 2, 6, 8

Dla każdego rzędu tak znalezionych wartości sprawdzamy:
czy jest jakaś inna tablica która się znajduje w tej.
np.
z1 z2 1 2 3
z3 z4 2 3
z3z4 kompletnie zawiera sie w z1z2 co oznacza, że mamy wykreślić z1z2
(teraz jeżeli są jakieś zmienne które się powtarza w każdym nie wykreślonym rzędzie, to oznacza że mamy wynik:
te zmienne + 2 startowe wartości)


(Reszta kroków głownie się tyczy tylko 2 przykładu ale potwierdzają one jak 1 przykład działa)

i teraz robimy tak zwane: "Minimalne pokrycie kolumnowe"

Bierzemy ten każdy bajerancki rząd który nie jest przekreślony czyli w drugim przykładzie:
3 6
1 5
5 6 7
3 5 7
układamy z tych cyferek taki wzorek:
  3   6
1   5
    5 6 7
  3 5   7

No i robimy to samo co w zadaniu 3 (jeden krok z poprzedniego programu)
Czyli szukamy wszystkich możliwych kombinajci kolumn które dadzą nam cyferke na każdym rzędzie:
czyli krok 1
bierzemy 3 - mamy cyferke na rzędzie 1 i 4, potem bierzemy 5 i mamy cyferke na rzędzie 2, 3, 4
czyli mamy już cały rząd gotowa odpowiedź.
Szukamy wszystkich takich kombinacji i je wypisujemy, DODAJĄC DO KAŻDEJ ODPOWIEDZI WEJŚCIOWE 2 KOLUMNY
czyli w tym zadaniu 2 i 4
więc uzyskujemy te:
2 3 4 5;  2 4 5 6;  1 2 3 4 6; itd.
a potem na samym końcu:
patrzymy które z tych wyników jest najkrótsze, w tym zadaniu są to opdowiedzi:
2 3 4 5;  2 4 5 6; każda po 4 elementy
i to jest nasza finalna odpowiedź


TODO:
Generate nice visuals for the "patterns" method

"""

import copy
import random

'''def custom_print(array):
    if isinstance(array, int):
        print(array + 1)
        return
    for value in array[:-1]:
        print(value + 1, end="_")
    print(array[-1] + 1)'''

# Print functions:


def custom_print(array):
    if isinstance(array, int):  # If array is a single integer
        print(array + 1)
        return

    def recursive_print(value):
        if isinstance(value, int):  # If value is a single integer
            print(value + 1, end="_")
            return
        else:
            for element in value[:-1]:
                recursive_print(element)
            print(value[-1] + 1, end="")
    recursive_print(array)
    print()


def array_custom_print(array):
    for part in array:
        for value in part[:-1]:
            print(value + 1, end="_")
        print(part[-1] + 1, end="; ")
    print()


def complex_array_custom_print(array):
    for i, part in enumerate(array):
        if isinstance(part, int):
            if i + 1 == len(array):
                print(part + 1, end="")
                continue
            else:
                print(part + 1, end="_")
                continue

        for value in part[:-1]:

            if isinstance(value, int):
                print(value + 1, end="_")

            else:
                for v in value[:-1]:
                    print(v + 1, end="_")

                print(value[-1] + 1, end=", ")

        try:
            print(part[-1] + 1, end="; ")
        except:
            print()
    print()

def custom_third_print(array):
    print(end="{")
    for part in array:
        if len(part) == 0:
            print(part[0] + 1, end="; ")
            continue

        for value in part[:-1]:

            if isinstance(value, int):
                print(value + 1, end="_")

            else:
                for v in value[:-1]:
                    print(v + 1, end="_")

                print(value[-1] + 1, end=", ")

        print(part[-1] + 1, end="; ")
    print("}")


# Smaller functions


def convert_to_columns(rows):
    # converting to columns
    columns = [[] for _ in range(len(rows[0]))]
    for row in rows:
        for width in range(len(rows[0])):
            columns[width].append(row[width])
    return columns


def is_subset(smaller_array, larger_array):
    """
    def is_subset(smaller_array, larger_array):
        for element in smaller_array:
            if element not in larger_array:
                return False
        return True
    """
    return len(set(smaller_array) - set(larger_array)) == 0


def remove_duplicates(array):

    if isinstance(array, int):
        return array
    new_array = []
    for value in array:
        if value not in new_array:
            new_array.append(value)

    return new_array

def remove_array_duplicates(array):
    new_array = []
    for value in array:
        if value not in new_array:
            new_array.append(value)
    return new_array


def general_unused(array, grid):

    full_values_range = [i for i in range(len(grid))]
    unused = []
    if array != full_values_range:
        for value in full_values_range:
            if value not in array:
                unused.append(value)
        return [unused] + array

    return array


# Main Logic


def combination_search(columns, ignore=None):
    def search_for_shortest_result(results):
        final_results = []

        min_value = len(results[0])
        for result in results:  # search lowest
            if isinstance(result, int):  # a single column resolves the problem
                min_value = 1
                break

            if min_value > len(result):
                min_value = len(result)

        for result in results:
            if isinstance(result, int):  # a single column resolves the problem
                final_results.append(result)
            else:
                if len(result) == min_value:
                    final_results.append(result)
        return final_results

    def find(graph, x, points_filled):
        """

        at the start function has only starting column as it's result
        if the column doesn't fill every needed spot
        then we start creating every possible combination
        for each row, we activate recursion.
        such recursion returns only when it's new column completes the fulfillment requirement

        searches for every combination (order irrelevant) of columns which added fill every gap with 1
                    [1, 0, 1] + [0, 1, 0] is a good pair.  If [1, 1, 1] such rows exist code should return all of them
                    the same applies for every same length combination.
                    :param columns:
                    :return:

        :param graph: complete columns array
        :param x: starting point
        :param points_filled: used in recursion, to represent current fill level
        :return: a
        :final - return: a list of all possible combinations of columns that fill every spot
        starting from a certain point
        """

        for j, val in enumerate(graph[x]):
            if val == 1:
                points_filled[j] = 1

        if sum(points_filled) == len(points_filled):
            return x

        result = []
        for i, column in enumerate(graph[x + 1:], start=x + 1):
            new_points_filled = copy.deepcopy(points_filled)
            # testing every possible first path choice for each previous path,
            # but excluding every earlier choice
            f = find(graph, i, new_points_filled)  # RECURSION
            if isinstance(f, int):
                result.append([x, f])
            elif f is None:
                pass
            else:
                for score in f:
                    result.append([x] + score)

        return result

    def ignored_lanes(results, ignore):
        correct_results = []
        for result in results:
            matching = True
            for value in ignore:
                if value in result:
                    matching = False
                    break
            if matching:
                correct_results.append(result)
        return correct_results

    useless_columns = []
    for i, column in enumerate(columns):
        useless = True
        for value in column:
            if value == 1:
                useless = False
                break
        if useless:
            useless_columns.append(i)

    print("useless", end=" ")
    custom_print(useless_columns)
    results = []

    for col_x in range(len(columns)):
        points_filled = [0 for _ in range(len(columns[0]))]
        result = find(columns, col_x, points_filled)
        if result != []:
            # removing useless data from result

            if not isinstance(result, int):
                new_result = []
                for value in result:
                    new_value = []
                    for v in value:
                        if v not in useless_columns:
                            new_value.append(v)
                    new_result.append(new_value)
                result = remove_array_duplicates(new_result)

            if isinstance(result, int):
                results.append([result])
            else:
                results += result
            #print()

    results = remove_array_duplicates(results)
    array_custom_print(results)
    print("Correct (to every answer add 2 starting X values):")
    correct_results = search_for_shortest_result(results)
    correct_results = remove_duplicates(correct_results)


    return correct_results


def method_first_step(grid, coordinates):
    def first_step(column, grid):
        def ones_in_column(column):
            P = []
            for i, value in enumerate(column):
                if value == 1:
                    P.append(i)
            return P

        print(column)
        result = ones_in_column(column)
        print_result = general_unused(result, grid)
        complex_array_custom_print(print_result)
        return result

    columns = convert_to_columns(grid)

    print("P", coordinates[0] + 1, sep="", end=" ")
    pxm = first_step(columns[coordinates[0]], grid)
    print("P", coordinates[1] + 1, sep="", end=" ")
    pxn = first_step(columns[coordinates[1]], grid)

    print("Pf:", end=" ")
    pf = first_step(columns[len(columns) - 1], grid)

    return [pxm, pxn, pf]


def method_second_step(pxm, pxn):

    first_step_of_result = []
    already_used = []

    for value in pxm:
        if value in pxn:
            first_step_of_result.append(value)
            already_used.append(value)

    # custom_print(first_step_of_result)
    print("pxm * pxn:", end=" ")

    new_pxm_and_pxn = []
    for px in [pxm, pxn]:
        result = []
        for value in px:
            if value not in already_used:
                result.append(value)
        if len(result) == 1:
            new_pxm_and_pxn.append(result)
        else:
            new_pxm_and_pxn.append(result)

    pxm_pxn = [new_pxm_and_pxn[1], new_pxm_and_pxn[0], first_step_of_result]
    complex_array_custom_print(pxm_pxn)
    return pxm_pxn


def third_step(grid, pxm_pxn, pf):
    third = []
    already_used = []
    for part in pxm_pxn[::-1]:
        new_part = [[]]
        for value in part:
            if value in pf and value not in already_used:
                already_used.append(value)
                new_part.append(value)
            elif value not in already_used:
                new_part[0].append(value)
                already_used.append(value)

        if len(new_part[0]) == 0:
            new_part.pop(0)
        third.append(new_part)

    last_part = []
    for value in pf:
        if value not in already_used:
            last_part.append(value)
            already_used.append(value)

    full_values_range = [i for i in range(len(grid))]
    unused = []
    if already_used != full_values_range:
        for value in full_values_range:
            if value not in already_used:
                unused.append(value)
        last_part = [unused] + last_part
    third.append(last_part)


    print("pxm * pxn | pf:", end=" ")
    custom_third_print(third)
    return third


def fourth_step(grid, third):

    comparison_list_rows = []

    for part in third:
        if isinstance(part[0], int):
            continue
        for value in part[0]:
            for second_value in part[1:]:
                comparison_list_rows.append([value, second_value])

    print("lista porownan:", end=" ")
    array_custom_print(comparison_list_rows)

    comparison_list_x = []
    for pair in comparison_list_rows:
        pair_result = []
        for i in range(len(grid[0]) - 1):
            if grid[pair[0]][i] != grid[pair[1]][i]:
                pair_result.append(i)
        comparison_list_x.append(pair_result)
    array_custom_print(comparison_list_x)

    # Reduction of unnecessary rows from comparison_list_x
    correct_comparison_list_x = []
    for i, result in enumerate(comparison_list_x):
        its_correct = True
        for j, second_result in enumerate(comparison_list_x):
            if i == j:
                continue
            if is_subset(second_result, result):
                its_correct = False
        if its_correct:
            correct_comparison_list_x.append(result)
    array_custom_print(correct_comparison_list_x)

    # Now we search for create a grid based on X values

    last_grid = []
    max_len = 0
    for row in correct_comparison_list_x:
        for value in row:
            if max_len < value:
                max_len = value
    for i in range(len(correct_comparison_list_x)):
        last_grid.append([0 for _ in range(max_len + 1)])

    for i, row in enumerate(correct_comparison_list_x):
        for value in row:
            last_grid[i][value] = 1

    print("columns")
    '''for row in last_grid:
        print(row)
    print("new")'''

    last_grid_columns = convert_to_columns(last_grid)
    '''for row in last_grid_columns:
        print(row)'''
    end_results = combination_search(last_grid_columns)
    return end_results


def method(grid, coordinates):

    pxm, pxn, pf = method_first_step(grid, coordinates)

    # second step: pxm * pxn
    pxm_pxn = method_second_step(pxm, pxn)
    # third step = (pxm*pxn) / pf
    third = third_step(grid, pxm_pxn, pf)

    end_results = fourth_step(grid, third)

    for row in end_results:
        row += coordinates
        row.sort()
        custom_print(row)




def testing_environment():
    def data_converter(data):
        grid = data[0]
        coordinates = [data[1][0] - 1, data[1][1] - 1]  # we modify coordinates to align with python array index system
        return grid, coordinates


    grid1 = [[1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1]]
    grid1_x = [4, 9]


    grid2 = [[0, 0, 1, 0, 1, 1, 0, 1],
             [1, 1, 0, 0, 1, 1, 1, 1],
             [0, 1, 0, 1, 0, 0, 1, 1],
             [0, 0, 1, 1, 0, 1, 1, 0],

             [1, 1, 0, 0, 1, 0, 1, 1],
             [0, 0, 0, 1, 1, 1, 0, 1],
             [0, 1, 0, 0, 0, 0, 1, 0],
             [1, 0, 1, 0, 0, 1, 1, 1],

             [0, 1, 1, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 0],
             [0, 1, 1, 0, 1, 1, 0, 1],
             [0, 1, 0, 0, 1, 1, 0, 1]]
    grid2_x = [2, 4]

    grid3_x = [3, 8]
    grid3 = [[1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],

             [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
             [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1]]

    grid4 = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
             [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1]]
    grid4_x = [5, 10]

    grid5 = [[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
             [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],

             [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
             [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
             [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
             [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1]]
    grid5_x = [3, 7]

    testing_sets = [[grid1, grid1_x], [grid2, grid2_x], [grid3, grid3_x], [grid4, grid4_x], [grid5, grid5_x]]

    for testing_set_address in range(1, 6):
        data = data_converter(testing_sets[testing_set_address - 1])
        method(data[0], data[1])
        print("\n\n\n")




if __name__ == "__main__":
    print("start")

    testing_environment()

    print("end")

