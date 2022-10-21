
'''
Astrix function that displas a triangle of right angle and its reverse image
'''
def Astrix():
    for item in range(0,10):
        print(' * ' * item)

    for item in range(10,0,-1):
        print(' * ' * item)
        

#Function call
Astrix()