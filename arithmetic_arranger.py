import re


def arithmetic_arranger(problems, solve=False):
    # Solution requires:
    #  2 blank spaces from the longest one (if the longest doesn't have the math symbol)
    #  4 black spaces from one problem to another
    #  same number of "-" as the longest one + 2

    if len(problems) > 5:
        return 'Error: Too many problems.'
    numbers_split = [re.split(" [+-] ", problem) for problem in problems]
    symbol_split = [re.split("[0-9]", problem) for problem in problems]
    symbol_split_clean = [list(filter(None, symbol))[0] for symbol in symbol_split]

    counter = 0
    divider = []
    solutions = []

    for number in numbers_split:
        if symbol_split_clean[counter][1] != '+' and symbol_split_clean[counter][1] != '-':
            return "Error: Operator must be '+' or '-'."
        if len(number[0]) > 4 or len(number[1]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not number[0].isdigit() or not number[1].isdigit():
            return "Error: Numbers must only contain digits."

        if solve:
            if symbol_split_clean[counter][1] == '+':
                solution = int(number[0]) + int(number[1])
            elif symbol_split_clean[counter][1] == '-':
                solution = int(number[0]) - int(number[1])

        if len(number[0]) > len(number[1]):
            number[0] = "  " + number[0]
            number[1] = symbol_split_clean[counter][1] + " " * (len(number[0])-len(number[1]) -1) + number[1]
            divider.append("-" * (len(number[0])))
        elif len(number[0]) == len(number[1]):
            number[0] = "  " + number[0]
            number[1] = symbol_split_clean[counter][1] + " " + number[1]
            divider.append("-" * (len(number[0])))
        else:
            if len(number[0]) == 1:
                number[0] = " " + number[0]
            number[0] = " " * (len(number[1])) + number[0]
            number[1] = symbol_split_clean[counter][1] + " " + number[1]
            divider.append("-" * (len(number[0])))

        counter += 1
        if solve:
            solutions.append(str(" " * (len(str(number[0])) - len(str(solution)))) + str(solution))
        if len(numbers_split)>1 and counter < len(numbers_split):
            number[0] += " " * 4
            number[1] += " " * 4
            divider.append(" " * 4)
            if solve:
                solutions.append(" " * 4)

    solution_list = ["", "", ""]
    for number in numbers_split:
        solution_list[0] += number[0]
        solution_list[1] += number[1]

    result = solution_list[0] + "\n" + solution_list[1] + "\n" + "".join(divider)
    if solve:
        result += "\n" + "".join(solutions)

    return result
