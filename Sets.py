
'''
Classes for doing set oprations inside
'''
class Operations:
    
    def Set(self):
        data = {1,2,3,4,5,6}
        print(data)
        
    def Hello(self):
        data = set('Hello')
        print(data)

    '''
    Create set first and add and element in range 0-10
    '''
    def Add(self):
        data = set()
        for item in range(0,10):
            data.add(item)
        print(data)

if __name__ == '__main__':
    list_set = Operations()
    list_set.Set()
    list_set.Hello()
    list_set.Add()