import view
import model.service_calc as service_calc
import model.logger as log

neg_message: str = "Некорректное значение"
example: str = "Пример: 10 + 2 * ( 3 - ( 1 / 2 )) + ( 2 + 1 * 2 )"


def menu():
    action = view.menu_view()
    if action == "1":
        menu_buttons_calc()
    if action == "2":
        menu_line_calc()
    if action == "3":
        menu_show_log()
    if action == "0":
        exit()
    else:
        menu()


def menu_buttons_calc():
    view.header("Кнопочный калькулятор")
    first_number = view.input_number(-1000000,1000000, "Введите число", f"{neg_message}")
    second_number = view.input_number(-1000000,1000000, "Введите число", f"{neg_message}")
    operation = view.input_operation("Введите операцию", f"{neg_message}")
    result = service_calc.check_button_calc(
        first_number, second_number, operation)
    view.show_example_button_calc(
        first_number, second_number, operation, result)


def menu_line_calc():
    view.header("Строчный калькулятор")
    line = view.input_line("Введите выражение", f" {neg_message}", f"{example}\n Возможен ввод без пробелов")
    result = service_calc.solve(service_calc.get_format_line(line))
    view.show_example_line_calc(line, result)


def menu_show_log():
    view.header("Файл log:")
    view.show_log(log.print_log())
