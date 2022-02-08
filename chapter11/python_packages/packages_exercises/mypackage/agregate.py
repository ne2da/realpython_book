import mypackage.mysubpackage.math as calculate_area
# <имя_пакета>.<имя_вложенного_пакета>.<имя_модуля> as <псевдоним>
import mypackage.mysubpackage.string as show_message
#<имя_пакета>.<имя_вложенного_пакета>.<имя_модуля> as <псевдоним>

def represent_final_output():
    a, l, w = calculate_area.get_area(5,8)
    # Вызов функции shout() посредством псевдонима calculate_area, заданного # # для цепочки  <имя_пакета>.<имя_вложенного_пакета>.<имя_модуля> as <псевдоним>
    print('Rectangle length', l)
    print('Rectangle width', w)
    print('Rectangle area', a)
    template_str =  f'The area of a {l}-by-{w} rectangle is {a}'
    result = show_message.shout(template_str)
    # Вызов функции shout() посредством псевдонима, заданного для цепочки
    #  <имя_пакета>.<имя_вложенного_пакета>.<имя_модуля> as <псевдоним>
    return result