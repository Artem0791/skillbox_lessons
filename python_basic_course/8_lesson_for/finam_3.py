from re import split


def to_camel_case(string):
    print(''.join(a.capitalize() for a in split('([^a-zA-Z0-9])', string)
                   if a.isalnum()))


to_camel_case("the-stealth-warrior")
to_camel_case("The_Stealth_Warrior")

# Написать функция которая будет переводить текст c "-._" в CamelCase
# (Примеры:
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior")
# Текст ввода: text = 'the_stealth_warrior'