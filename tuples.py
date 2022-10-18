
'''
Astrix function that displas a triangle of right angle and its reverse image
'''
def Astrix():
    for item in range(0,10):
        print(' * ' * item)

    for item in range(10,0,-1):
        print(' * ' * item)
        
'''Apple letters tuple'''
def Letters():
    apple = ('a','p','p','l','e')
    print(apple)
    
    if 'a' in apple:
        print('a Letter A Exists in tuple')
    else:
        print('A does not exists in the tuple')

Letters()
Astrix()