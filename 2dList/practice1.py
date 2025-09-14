import copy
TN = ['Chennai', 'Cuddalore', 'Villupuram', 'Madurai']
AP = ['Hyderabad', 'kadappa','Tirupathi']
KT = ['Bangalore', 'Mangalore', 'Goa']

list2d = [TN,AP,KT]

# shallow copy
list1 = [[1, 2], [3, 4]]
list2 = list1[:]
list1[0][0] = 5
print(list2)



# deep copy
print(list2d)
list2d[0][0]= 'Kanyakumari'
Indian_states = copy.deepcopy(list2d)
print(Indian_states)