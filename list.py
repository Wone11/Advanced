#lists 

from operator import index


friut_list= ['banana','apple','orange']
print('Friut List: ',friut_list)

#displaying lists using a for loop
for (i, item) in enumerate(friut_list,start=1):
    print('index : {} fruit : {} '.format(i,item))