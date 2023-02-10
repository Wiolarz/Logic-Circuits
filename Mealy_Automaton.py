"""
Zaprojektować minimalny automat Mealy’ego z jednym wejściem i jednym wyjściem, badający „trójki”
symboli wejściowych. Sygnał wyjściowy pojawiający się podczas trzeciego skoku sygnału wejściowego ma
mieć wartość 1 po wykryciu w ciągu wejściowym „trójki” < tu wybrana trójka >, wartość 0 dla innych
„trójek”. Sygnał wyjściowy podczas 1 i 2 skoku sygnału wejściowego powinien mieć wartość 0. Po zbadaniu
kolejnej „trójki” automat ma wracać do stanu początkowego. Podać funkcję wyjścia i funkcje wzbudzeń dla
realizacji na przerzutnikach typu D, T, JK, SR (typ przerzutnika będzie podany).



List of steps:
Part 1:
Generate graph that will generate an answer
Part 2:
Generate an array based on graph
Part 3:
Translate LETTERS [A, B, C, D] to numbers [00, 01, 11, 10]
Part 4:
Generate two arrays:
ex. given an array:
00 01
00 11
00 10
00 00
ab ab
we create next two based on columns a and b:
a:
0 0
0 1
0 1
0 0
b:
0 1
0 1
0 0
0 0

Part 5:
We have a bunch of constants:
D, T, JK, SR

each constant has a index array before each of it's values:
0 0
0 1
1 0
1 1

D:
0 1 0 1

T:
0 1 1 0

JK:
0- 1- -1 -0

SR:
0- 10 01 -0





"""


"""
"Part 1 Code:"
Step 1:
some outside function generates us a random boolean value
Step 2:
we have to return a boolean value based on given requirements like: "return 1 if input generated a string of 010"


Program outline:
given the user input, code develops an automaton


Cases when program can be shorter:

something repeats:
11

A:
1 - A


"""


def testing_automaton(automaton, text):


    current_position = 0
    for letter in text:
        letter = int(letter)
        output = automaton[current_position][letter + 2]
        current_position = automaton[current_position][letter]
        print(output)
    print("\n\n")

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


def rest_of_the_tables(original_array):
    # first part
    array = []
    for row in original_array:
        array.append([row[0], row[1]])
    #print(original_array)

    addresses = ["00", "01", "11", "10"]
    for i in range(len(array)):
        for column in range(2):
            for row in range(len(array)):
                if array[row][column] == i:
                    array[row][column] = addresses[i]

    left  = []
    right = []
    left_constants = [0, 0, 1, 1]
    right_constants = [0, 1, 1, 0]
    for i in range(len(array)):
        left.append([left_constants[i], int(array[i][0][0]), int(array[i][1][0])])
        right.append([right_constants[i], int(array[i][0][1]), int(array[i][1][1])])

    if len(array) == 3:
        left.append([1, None, None])
        right.append([0, None, None])

    # PRINT D IN HUMAN
    for row in left:
        first = True
        for value in row:

            if value is None:
                print("-", end=" ")
            else:
                print(value, end=" ")
            if first:
                print("|", end=" ")
                first = False
        print()
    print(";;;;")
    for row in right:
        first = True
        for value in row:
            if value is None:
                print("-", end=" ")
            else:
                print(value, end=" ")
            if first:
                print("|", end=" ")
                first = False
        print()

    T = [0, 1, 1, 0]
    JK_L = [0, 1, None, None]
    JK_R = [None, None, 1, 0]

    SR_L = [0, 1, 0, None]
    SR_R = [None, 0, 1, 0]
    results_constants = [T, JK_L, JK_R, SR_L, SR_R]

    def compare(constant, a, b):
        #general_addresses = ["00", "01", "10", "11"]
        if a is None or b is None:
            return None
        adr = (a * 2) + b
        return constant[adr]


    def create_result(constant, source_array):
        result = []
        # T left
        for i in range(4):
            result.append([compare(constant, source_array[i][0], source_array[i][1]),
                           compare(constant, source_array[i][0], source_array[i][2])])
        for row in result:
            for value in row:
                if value is None:
                    print("-", end=" ")
                else:
                    print(value, end=" ")
            print()

    names = ["T", "J", "K", "S", "R"]  # [T, JK_L, JK_R, SR_L, SR_R]
    for i, constant in enumerate(results_constants):
        print("----", names[i])
        create_result(constant, left)
        print(":::")
        create_result(constant, right)









def testing_environment():

    '''too simple text1 = "0"
    text2 = "1"
    text3 = "01"
    text4 = "10"
    text5 = "11"'''

    text1 = "000"
    text2 = "001"
    text3 = "010"
    text4 = "011"
    text5 = "100"
    text6 = "101"
    text7 = "110"
    text8 = "111"

    testing_sets = [text1, text2, text3, text4, text5, text6, text7, text8]
    automatons_list = list_of_text_automatons()

    print(automatons_list[5])
    rest_of_the_tables(automatons_list[5])

'''    for i, automaton in enumerate(automatons_list):
        print(automaton)
        automaton = [[0, 1, 0, 0],
                     [0, 2, 0, 0],
                     [0, 3, 0, 1],
                     [0, 0, 0, 1]]
        rest_of_the_tables(automaton)
        break
        #for row in automaton:
        #    print(row)
        #print("-----")
        #print(testing_sets[i])
        #testing_automaton(automaton, testing_sets[i])
        #for testing_set_address in range(0, 8):'''




if __name__ == "__main__":
    print("start")
    testing_environment()
    print("end")