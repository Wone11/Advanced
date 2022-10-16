#lists 

from operator import index


fruit_list= ['banana','apple','orange']
fruit_list.append('lemon')
print('Friut List: ',fruit_list)

#displaying lists using a for loop
for (i, item) in enumerate(fruit_list,start=1):
    print('index : {} fruit : {} '.format(i,item))

