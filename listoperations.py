
'''
operational list functons
'''

def list_operand():
    list_one = [0] * 8
    list_two = [1, 2, 3, 4, 5, 6]
    new_list = list_one + list_two
    print(new_list)


def amazin_display():
    list_one = [1,2,3,4,5,6,7,8,9]
    displayed_to =list_one[::2]
    print(displayed_to)
# list_operand()

amazin_display()