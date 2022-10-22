'''Handle and raise and errors..'''
def Handllers():
    numberOne = 5
    if numberOne < 0:
        raise Exception('Number Shold be POSITIVE!')
    else:
        print(numberOne)

'''Zero Devission Error'''
def Devizion():
    try:
        numberOne  = int(input('Enter The Devider : '))
        numberTwo  = int(input('Enter The Devidend : '))
        checkType   = numberOne + numberTwo
        print(numberOne / numberTwo)
    
    except ZeroDivisionError as message:
        print(message)
        
    except TypeError as message:
        print(message)
    except ValueError as message:
        print(message)
    else:
        print('Every Thing is OK')

#Call the Methods....
Handllers()
Devizion()