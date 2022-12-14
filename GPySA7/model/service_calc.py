import re
import model.logger as log

priority = {"+": 1, "-": 1, "*": 2, "/": 2}
negative_expression = "Некорректное выражение"


def solve(expression: str):
    original_expression = expression
    expression = get_brackets_expression(expression)
    if expression == negative_expression:
        return negative_expression
    expression = expression.split()
    numbers = []
    operations = []
    pointer = 0
    while (pointer < len(expression)):
        tmp_element = ""
        if re.match("^-?\d+\.\d+$", expression[pointer]) != None or type(expression[pointer]) is float \
                or re.match("^-?\d+$", expression[pointer]) != None or type(expression[pointer]) is int:
            tmp_element += expression[pointer]
            pointer += 1
            if len(tmp_element) > 0:
                numbers.append(tmp_element)
        elif pointer < len(expression) and expression[pointer].isnumeric() == False:
            if len(numbers) < 1:
                number_from_stack = 0
            else:
                number_from_stack = numbers[-1]
            if len(operations) > 0 and priority.get(operations[-1]) < priority.get(expression[pointer]):
                numbers.pop()
                action_result = check_button_calc(
                    number_from_stack, expression[pointer+1], expression[pointer])
                if action_result == "Infinity" or action_result == "Undefined":
                    return action_result
                else:
                    numbers.append(str(action_result))
                pointer += 1
            elif len(operations) > 0 and priority.get(operations[-1]) >= priority.get(expression[pointer]) \
                    or len(operations) < 1:
                operations.append(expression[pointer])
            pointer += 1
    if len(numbers) == 0 and len(operations) == 0:
        log.add(f"Не распознаны операнды: {expression}", log.Status.debug.value)
        return negative_expression
    while (len(operations) > 0 and len(numbers) > 1):
        numbers[1] = str(check_button_calc(
            numbers[0], numbers[1], operations[0]))
        operations = operations[1:]
        numbers = numbers[1:]
    log.add(f"Выражение: {original_expression}", log.Status.info.value)
    log.add(f"Результат: {numbers}", log.Status.info.value)
    return numbers[0] if len(numbers) > 0 else operations[0]


def button_calc_add(first_number, second_number):
    return first_number+second_number


def button_calc_dif(first_number, second_number):
    return first_number-second_number


def button_calc_mult(first_number, second_number):
    return first_number*second_number


def button_calc_div(first_number, second_number):
    return first_number/second_number


def check_type_number(number):
    try:
        if re.match("^-?\d+\.\d+$", number) != None or type(number) is float:
            return float(number)
        elif re.match("^-?\d+$", number) != None or type(number) is int:
            return int(number)
    except Exception as ex:
        log.add(f"Ошибка типа операнда {ex}", log.Status.error.value)


def check_button_calc(first_number: str, second_number: str, operation: str):
    match operation:
        case "*":
            return button_calc_mult(check_type_number(first_number), check_type_number(second_number))
        case "/":
            if second_number == '0' and first_number != '0':
                return "Infinity"
            elif second_number == '0' and first_number == '0':
                return 'Undefined'
            else:
                return button_calc_div(check_type_number(first_number), check_type_number(second_number))
        case "+":
            return button_calc_add(check_type_number(first_number), check_type_number(second_number))
        case "-":
            return button_calc_dif(check_type_number(first_number), check_type_number(second_number))


def get_brackets_expression(expression):
    expr = ""
    if ("(" in expression) ^ (")" in expression):
        log.add(f"{negative_expression} {expression}", log.Status.error.value)
        return negative_expression
    while ("(" in expression and ")" in expression):
        match_substring = re.search('\([^\(\)]+\)', expression)
        if match_substring != None:
            expr_with_brackets = expression[match_substring.start():match_substring.end()]
            expr = expression[match_substring.start() +1:match_substring.end()-1]
            expr = str(expr)
            left_bracket = match_substring.start()-1
            right_bracket = match_substring.end()
            expr_solve = solve(expr)
            while (left_bracket < len(expression) and expression[left_bracket] == " "):
                left_bracket -= 1
            if expression[left_bracket] not in "/*-+(":
                expr_solve = f"* {expr_solve}"
            while (right_bracket < len(expression) and expression[right_bracket] == " "):
                right_bracket += 1
            if right_bracket < len(expression) and expression[right_bracket] not in "/*-+)":
                expr_solve = f"{expr_solve} *"
            expression = expression.replace(
                expr_with_brackets, f"{expr_solve} ", 1)
    return expression.strip()


def get_format_line(line):
    format_line = []
    pointer = 0
    while (pointer < len(line)):
        if (line[pointer] in "+-*/()"):
            format_line.append(line[pointer])
            pointer += 1
        elif line[pointer].isdigit():
            curr_item = ""
            while (pointer < len(line) and line[pointer].isdigit()):
                curr_item += line[pointer]
                pointer += 1
            format_line.append(curr_item)
        else:
            pointer += 1
    return str.join(" ", format_line)
