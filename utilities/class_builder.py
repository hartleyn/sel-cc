from utilities import xpath_generator

__author__ = 'Nick Hartley'
# 5/4/2018


def declaration_string_builder(var_name, value):
    indent = '    '
    return indent + str(var_name) + ' = \'' + str(value) + '\'\n'


def build_classes(driver, filename):
    buttons = xpath_generator.grab_buttons(driver)
    print(buttons)
    selects = xpath_generator.grab_selects(driver)
    print(selects)
    inputs = xpath_generator.grab_inputs(driver)
    print(inputs)

    with open(filename, 'w') as f:
        f.write('class Buttons:\n')

        for button in buttons:
            string = declaration_string_builder(button['var_name'], button['xpath'])
            f.write(string)

        f.write('class Selects:\n')

        for select in selects:
            string = declaration_string_builder(select['var_name'], select['xpath'])
            f.write(string)

        f.write('class Inputs:\n')

        for input_field in inputs:
            string = declaration_string_builder(input_field['var_name'], input_field['xpath'])
            f.write(string)
