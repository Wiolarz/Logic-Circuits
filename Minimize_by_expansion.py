"""
"Minimize the function by expansion. Give all solutions."


starting grid
0 0 0 0 0
1 1 0 0 0
1 1 0 1 0
0 1 1 1 0
1 1 0 0 1
0 1 0 1 1

R:
1 1 1 0 1
0 0 0 1 0
0 0 1 1 0
1 0 0 0 1
0 1 1 0 0


Step 1 for each row in the starting grid:
Step 2 for each value in a row we negate each column in grid R:
Step 3 we print that grid,
Step 4 then we search for smallest combinations of columns that will create a full column of 1
Step 5 we assign each column_id a True value if on a starting grid, corresponding value is 1, otherwise we assign False

Example steps 1-5
1 for row 4: "0 1 1 1 0"
2 we negate values of R
3:
1 0 0 1 1
0 1 1 0 0
0 1 0 0 0
1 1 1 1 1
0 0 0 1 0
4:
2 4
5:
[2 True, 4 True]

Step 6 At the end we create an empty array with same number of rows as in starting array.
with length of each row being equal to the number of unique results from every "5:"
Step 7 For each row we assign a 1 value if on that row we used of the unique result from "5:"
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 1, 1, 1]

Step 8: We search for unique combination just like in  Step "4:"
[0, 5, 7]
[1, 5, 7]
[2, 5, 7]
[3, 5, 7]

"""
import copy


def convert_to_columns(rows):
    # converting to columns
    columns = [[] for _ in range(len(rows[0]))]
    for row in rows:
        for width in range(len(rows[0])):
            columns[width].append(row[width])
    return columns


def combination_search(columns, ignore=None):
    def search_for_shortest_result(results):
        final_results = []
        try:
            min_value = len(results[0][0])

            for row in results:  # search lowest

                for score in row:
                    if min_value > len(score):
                        min_value = len(score)

            for row in results:
                for score in row:
                    if len(score) == min_value:
                        final_results.append(score)
            return final_results

        except:
            return results

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

    a = [1, 0, 1], \
        [0, 1, 0], \
        [1, 0, 1]

    b = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [1, 0, 1]]
    # a, b test data
    """
    1, 2, 4
    2, 3
    3, 4
    For B test data:
    1 0 0
    1 1 0
    0 1 1
    1 0 1
    
    1 1 0 1
    0 1 1 0
    0 0 1 1
    
    0 0 0
    1 0 0 (1)
    1 1 0 (1, 2)
    1 1 1 (1 2 3)
    1 1 1 (1 2 4)
    1 1 1 (1 3)
    1 0 1 (1 4)
    
    """


    results = []
    print("results for this B")
    for col_x in range(len(columns)):
        points_filled = [0 for _ in range(len(columns[0]))]
        result = find(columns, col_x, points_filled)
        if result != []:
            print("row", col_x + 1, end="--  ")
            if isinstance(result, int):
                print(result + 1)
            else:
                for res in result:
                    for value in res:
                        print(value + 1, end=" ")
                    print("::", end=" ")
                print()
                #print(result)
            results.append(result)
            #print()

    '''if ignore is not None:
        print("with ignored:")
        results_without_ignored_lanes = ignored_lanes(results, ignore)
        print(results_without_ignored_lanes)'''

    correct_results = search_for_shortest_result(results)

    print("Correct:")
    for row in correct_results:
        if isinstance(row, int):
            print(row + 1)
        else:
            for value in row:
                print(value + 1, end=" ")
            print()
    return correct_results


def rows_to_ignore(B):
    rows_to_ignore = []
    number_rows = []
    for number_row in B:
        new_number_row = []
        for i, value in enumerate(number_row, start=1):
            if value == 1:
                new_number_row.append(i)
        number_rows.append(new_number_row)

    for i, new_row in enumerate(number_rows[:-1]):
        for new_row2 in number_rows[i + 1:]:
            if i in rows_to_ignore or i + 1 in rows_to_ignore:
                break
            if new_row == new_row2:  # if identical
                rows_to_ignore.append(i)

            first_in_second = True
            for value in new_row:
                if value not in new_row2:
                    first_in_second = False
                    break
            if first_in_second:
                rows_to_ignore.append(i + 1)
                continue
            else:
                second_in_first = True
                for value in new_row2:
                    if value not in new_row:
                        second_in_first = False
                        break

            if second_in_first:
                rows_to_ignore.append(i)
    return rows_to_ignore


def B_print(B, row_id, rows_to_ignore):
    print("B", row_id + 1)
    for print_row in B:
        print(print_row)
    print("rows to ignore (cross those out):", end=" ")
    for row in rows_to_ignore:
        print(row + 1, end=" ")
    print()


def create_B(data):
    """
    Steps "1:, 2:"
    :param data:
    :return:
    """
    list_of_B = []
    grid = data[0]
    R = data[1]
    for row_id, row in enumerate(grid):
        # Creating "B(kx, R)" for each row "k"
        new_R = copy.deepcopy(R)
        for i, value in enumerate(row):
            if value == 1:
                for new_row in new_R:
                    for j, new_value in enumerate(new_row):
                        if i == j:
                            if new_value == 1:
                                new_row[j] = 0
                            else:
                                new_row[j] = 1


        list_of_B.append(new_R)
    return list_of_B


def data_print(data):
    print("K:")
    for row in data[0]:
        print(row)
    print("R:")
    for row in data[1]:
        print(row)
    print()


def boolean_function(test_grids):

    for data in test_grids:
        data_print(data)
        list_of_B = create_B(data)

        final_result = []
        for B_id, B in enumerate(list_of_B):

            ignore = rows_to_ignore(B)
            B_print(B, B_id, ignore)

            columns = convert_to_columns(B)

            results = combination_search(columns, ignore)

            # Step
            edited_results = []
            for result in results:
                edited_result = []
                for element in result:
                    if data[0][B_id][element] == 1:
                        edited_result.append([element, True])
                    else:
                        edited_result.append([element, False])
                edited_results.append(edited_result)
            final_result.append(edited_results)


            '''for size in range(1, len(row) - len(rows_to_ignore)):
                pass'''  # TODO implement rows to ignore as optimization effort
            print("\n")
        print("Each row represents solutions for each B")
        print("if a value has a corresponding word == False it means that you have to write a line on top of the number")
        for row in final_result:
            for row_result in row:
                for res in row_result:
                    print(res[0] + 1, res[1], end=" ")
                print(end=":: ")
            print()

            #print(row)



        # Removing duplicates
        unique_final_result = []
        for row in final_result:
            for result in row:
                unique_result = True
                for unique in unique_final_result:
                    if result == unique:
                        unique_result = False
                if unique_result:
                    unique_final_result.append(result)
        print("-- List of unique solution to our B tables")
        for i, row in enumerate(unique_final_result):
            print(i + 1, end=" row  ")
            for res in row:
                print(res[0] + 1, res[1], end=" ")
            print(end=":: ")
            #print(row)
            print()
        print("Based on those unique result we assign each a number based on how it early it appeared")

        final_graph_values = []
        for row in final_result:
            row_results = []
            for result in row:
                for i, unique in enumerate(unique_final_result):
                    if result == unique:
                        row_results.append(i)
                        # print(i, end=" ")
            row_results.sort()  # TODO DEBUG ONLY
            final_graph_values.append(row_results)
            #print()

        for row in final_graph_values:
            for value in row:
                print(value + 1, end=" ")
            print()
        print("we cross out rows that have an another row that is completely contained by that row")
        final_graph = []

        for _ in range(len(final_result)):  # number of rows
            final_graph.append([0 for _ in range(len(unique_final_result))])


        for i, row in enumerate(final_graph_values):
            for value in row:
                final_graph[i][value] = 1
        print("final graph:")
        for row in final_graph:
            print(row)
        print("Every possible solution, you should write down few of those that are similar to correct results")
        final_graph = convert_to_columns(final_graph)

        end_result = combination_search(final_graph)




def testing_enviro():
    grid = [[0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1]]
    R = [[1, 1, 1, 0, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 0, 0]]

    grid2 = [[0, 0, 0, 1, 0],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 1, 0],
             [1, 0, 1, 1, 0],
             [1, 1, 1, 0, 1],
             [1, 0, 1, 0, 0]]
    R2 = [[0, 0, 0, 1, 1],
          [0, 1, 1, 1, 1],
          [1, 0, 0, 1, 1],
          [1, 1, 1, 0, 0],
          [1, 1, 1, 1, 0]]
    """
    3:
    {2, 3}, {3, 5}  x2 !x3    !x3 !x5
    """
    grid3 = [[1, 1, 1, 1, 0]]

    R3 = [[0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0],
          [0, 1, 0, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 0, 0, 0, 1]]

    grid4 = [[0, 1, 1, 1, 1]]

    R4 = [[0, 1, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 1, 0],
          [1, 1, 1, 0, 1],
          [1, 0, 0, 0, 1]]

    grid5 = [[1, 1, 1, 0, 1]]
    R5 = [[1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 1],
          [1, 1, 1, 1, 0],
          [0, 1, 0, 1, 0]]

    #test_grids = [[grid, R], [grid2, R2]]
    #test_grids = [[grid, R], [grid3, R3]]
    test_grids = [[grid5, R5]]

    boolean_function(test_grids)


if __name__ == "__main__":
    print("start")
    testing_enviro()
    print("end")

"""
[0, 0, 0, 1, 1] 4 5
[0, 0, 1, 0, 1] 3 5
[0, 1, 1, 0, 1] 2 3 5
[1, 0, 0, 1, 0] 1 4
[1, 1, 1, 1, 0] 1 2 3 4


{1, 5}  { 3, 4}  {4, 5}
"""