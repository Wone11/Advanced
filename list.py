from listoperations import *

'''list operations here'''
def normal_list():
    #orginal list
    fruit_list= ['banana','apple','orange']

    #append an item by default position thet appends at the end
    fruit_list.append('lemon')
    print('Friut List: ',fruit_list)

    #insert an item in the specific position
    fruit_list.insert(3,'pappaya')

    #add an item in the first position
    fruit_list.insert(0,'tomato')

    #here is something needs to be removed
    fruit_list.pop(0)

    #item inserted by master
    fruit_list.insert(1,'Carrot')


    #item inserted by master
    fruit_list.insert(4,'water melon')

    #displaying lists using a for loop
    for (i, item) in enumerate(fruit_list,start=1):
        print('index : {} fruit : {} '.format(i,item))

def callOne():
    list_operand()

def display_odd():
    amazin_display()

'''Mian functions call '''
if __name__ =='__main__':
    choice = int(input('Enter a choice : '))
    if choice == 1:
        callOne()
    elif choice ==2:
        display_odd()
    elif choice ==3:
            normal_list()
    elif choice == 4:
        reverse_display()
    elif choice == 5:
        power()
    else:
        print('No correct choice ')