"""
Zminimalizować liczbę stanów automatu dla podanej tabeli przejść-wyjść. Podać automat minimalny.
"""

def custom_print(array):
    for block in array:
        for part in block[:-1]:
            print(part + 1, end=":")
        print(block[-1] + 1, end=" ")
    print()

def list_of_text_automatons():

    # first two columns are row addresses where to go next
    # last two columns are return values
    automaton = [[],
                 [],
                 [],
                 []]

    automaton1 = [[1, 0, 0, 0],  # 000
                  [2, 0, 0, 0],
                  [2, 0, 1, 0]]

    automaton2 = [[1, 0, 0, 0],  # 001
                  [1, 0, 0, 0],
                  [0, 0, 0, 1]]

    automaton3 = [[1, 0, 0, 0],  # 010
                  [1, 2, 0, 0],
                  [0, 0, 1, 0]]



    automaton4 = [[1, 0, 0, 0],  # 011
                  [0, 2, 0, 0],
                  [0, 0, 0, 1]]

    automaton5 = [[0, 1, 0, 0],  # 100
                  [2, 0, 0, 0],
                  [0, 0, 1, 0]]

    automaton6 = [[0, 1, 0, 0],  # 101
                  [2, 1, 0, 0],
                  [0, 0, 0, 1]]
    #

    automaton7 = [[0, 1, 0, 0],  # 110
                  [0, 2, 0, 0],
                  [0, 0, 1, 0]]

    automaton8 = [[0, 1, 0, 0],  # 111
                  [0, 2, 0, 0],
                  [0, 2, 0, 1]]

    list_of_automatons = [automaton1, automaton2, automaton3, automaton4,
                          automaton5, automaton6, automaton7, automaton8]
    return list_of_automatons


def triangle(automaton):

    half_index = len(automaton[0]) // 2

    #print(half_index)
    # column 1

    for i, row in enumerate(automaton[:-1]):
        j = len(automaton) - 1
        for second_row in automaton[:-1 - i]:
            print("[", i, j, "]", sep="", end=" ")
            j -= 1
        print()


    triangle_array = []
    for i, row in enumerate(automaton[:-1]):
        new_array = []
        j = len(automaton)
        for second_row in automaton[:-1 - i]:
            j -= 1
            #print("[", i, j, "]", sep="", end=" ")
            one = automaton[i]
            two = automaton[j]
            if i == 1 and j == 7:
                x = 5
            # checking if row is V:
            x = False
            V = 0
            for index in range(half_index, len(automaton[0])):
                if one[index] == "-" or two[index] == "-":
                    V += 1
                elif one[index] == two[index]:
                    new_idx = index - half_index
                    if one[new_idx] == two[new_idx] or one[new_idx] == "-" or two[new_idx] == "-":
                        V += 1
                else:
                    x = True



            if x:
                print("[", "x", "]", sep="", end=" ")
                new_array.append("x")
            elif V == 2:
                print("[", "v", "]", sep="", end=" ")
                new_array.append("v")
            else:
                # cheking left side
                #print("[", ";", "]", sep="", end=" ")
                pairs = []
                for index in range(2):
                    if one[index] == two[index] or one[index] == "-" or two[index] == "-":
                        pass
                    else:
                        pairs.append([one[index], two[index]])
                for pair in pairs:
                    print(pair[0] + 1, pair[1] + 1, sep=":", end="")
                print(end=" ")
                pairs[0].sort()
                new_array.append(pairs[0])  # TODO work on more possible pairs
        print()
        triangle_array.append(new_array)

    problem_occurred = True
    while problem_occurred:
        problem_occurred = False
        for i, row in enumerate(triangle_array):
            for j, value in enumerate(row):
                if value != "x" and value != "v":
                    smaller = value[0]
                    larger = len(automaton) - value[1] - 1
                    if triangle_array[smaller][larger] == "x":
                        triangle_array[i][j] = "x"
                        problem_occurred = True
                        break
            if problem_occurred:
                break
    print("final")
    for row in triangle_array:
        print(row)

    list_of_addresses = []
    for i, row in enumerate(triangle_array):
        for j, value in enumerate(row):
            if value != "x":
                list_of_addresses.append([i, len(automaton) - j - 1])

    custom_print(list_of_addresses)

    # attempts to find trio  TODO quarter and more
    def negate(value):
        if value == 0:
            return 1
        return 0

    MKZ = []
    used_pairs = {-1}

    for i, pair in enumerate(list_of_addresses):
        for j, second_pair in enumerate(list_of_addresses[i + 1:], start=i + 1):
            search_pair = None
            if pair[0] in second_pair:
                value = pair[0]
                search_pair = [pair[1], second_pair[negate(second_pair.index(pair[0]))]]
                search_pair.sort()
            elif pair[1] in second_pair:
                value = pair[1]
                search_pair = [pair[0], second_pair[negate(second_pair.index(pair[1]))]]
                search_pair.sort()

            if search_pair is not None:
                for k, third_pair in enumerate(list_of_addresses[j + 1:], start=j + 1):
                    if third_pair[0] == search_pair[0] and third_pair[1] == search_pair[1]:
                        new_mkz = [value] + search_pair
                        new_mkz.sort()
                        MKZ.append(new_mkz)
                        for address in [i, j, k]:
                            used_pairs.add(address)

    print("MKZ:")
    custom_print(MKZ)
    #print(used_pairs)
    for i, pair in enumerate(list_of_addresses):
        if i not in used_pairs:
            MKZ.append(pair)
    print("MKZ:")
    custom_print(MKZ)




def testing_environment():

    automatons_list = list_of_text_automatons()

    test = []
    for t in test:
        triangle(t)

    for i, automaton in enumerate(automatons_list):
        print(automaton)
        automaton = [[1,    5,   0,  0],
                     [2,    0,   1,  1],
                     ["-",  3,  "-", 0],
                     ["-",  4,  "-", 0],
                     [2,   "-",  1, "-"],
                     [6,   "-",  1, "-"],
                     ["-",  7,  "-", 0],
                     ["-", "-", "-", 1]]
        triangle(automaton)
        break
        #for row in automaton:
        #    print(row)
        #print("-----")
        #print(testing_sets[i])
        #testing_automaton(automaton, testing_sets[i])
        #for testing_set_address in range(0, 8):




if __name__ == "__main__":
    print("start")

    testing_environment()
    print("end")


"""
12
1 3 



"""