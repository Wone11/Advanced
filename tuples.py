
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
    print(apple.count('p'))
    
    if 'a' in apple:
        print('a Letter A Exists in tuple')
    else:
        print('A does not exists in the tuple')
 
'''
 Copy tuples oin to two parts
 
'''       
def Copy_Tuples():
    data =(1,2,3,4,5,6,7,7,8,9,10)
    copy_data=data[:5]
    print(copy_data)    
   
'''
Copy Data In range Two
''' 
def Inrange_Two():
    data =(1,2,3,4,5,6,7,8,9,10)
    copy_data=data[::2]
    print(copy_data)    
'''
Print Data In reverse
'''
def Reverse():
    data =(1,2,3,4,5,6,7,8,9,10)
    copy_data=data[::-1]
    print(copy_data)    
    
def Check_New_Stage():
    print('Diff Stage')

Letters()
Astrix()
Copy_Tuples()
Check_New_Stage()
Inrange_Two()
Reverse()