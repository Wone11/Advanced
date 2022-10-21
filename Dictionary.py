'''
Dictionary for key value pairs
'''

def Data():
    data = [{'name':'Gandayiki','Age':28,'Genderd':'Male'},
            {'name':'SoulaxG','Age':30,'Genderd':'Female'},
            {'name':'Enanu','Age':68,'Genderd':'Male'}]
    
    for item in data:
        print(item)

def Operations():
    data ={'name':'Gandayiki','Age':28,'Genderd':'Male'}
    
    data['email'] = 'Ganadayiki156@gandayiki.com'
    data['City'] = 'Addis Ababa'
    print(data)
    data.pop('email')
    print(data)
    

#Functiokn call
Data()
Operations()