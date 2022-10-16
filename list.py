#orginal list
fruit_list= ['banana','apple','orange']

#append an item by default position thet appends at the end
fruit_list.append('lemon')
print('Friut List: ',fruit_list)

#insert an item in the specific position
fruit_list.insert(3,'pappaya')

#add an item in the first position
fruit_list.insert(0,'tomato')

#displaying lists using a for loop
for (i, item) in enumerate(fruit_list,start=1):
    print('index : {} fruit : {} '.format(i,item))

