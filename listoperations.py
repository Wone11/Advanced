
'''functions to concat a two lists'''
from pprint import pprint


def list_operand():
    list_one = [0] * 8
    list_two = [1, 2, 3, 4, 5, 6]
    new_list = list_one + list_two
    print(new_list)

'''display in gap 2 function'''
def amazin_display():
    list_one = [1,2,3,4,5,6,7,8,9]
    displayed_to =list_one[::2]
    print(displayed_to)
    
'''Display in the reverse orede'''
def reverse_display():
    list_one = [1,2,3,4,5,6,7,8,9]
    displayed_to =list_one[::-1]
    print(displayed_to)
    
'''powers of the given list'''
def power():
    list_one =[1,2,3,4,5,6,7,8,9]
    powers = [item * item for item in  list_one]
    
    print(list_one)
    print(powers)
    
def Power_In_Range():
    powers = [item * item for item in range(0,9)]
    pprint(powers)
    
# reverse_display()
# amazin_display()
# power()
Power_In_Range()