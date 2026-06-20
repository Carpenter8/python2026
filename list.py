'''
# empty list 
list1=[]
print(type(list1))
'''

list2=[10,20,'vineet','pagal',10,80]
#count()
print(list2.count(10))
#index
print(list2.index(80))
print(list2.index(10,1))

#insert methods

list2.insert(2,'piyush Bhai')
print(list2)

#pop(delete)
list2.pop(3)
print(list2)

# extend methods

list3=['neha','mohit']

list2.extend(list3)
print(list2)

#copy methods 

list3=list2.copy()
print(list3)


'''
list3=list[:]
print(list3)
 '''


#sort methods aacessing or decesding order 
list4=[1,3,5,8,9,2,6]
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)



#reverse methods

list4.reverse()
print(list4)


list5=['anshik','ankit','nomi','mohin']
a=[word for word in list5 if word.startswith('a')]
print(a)

# list unpacket 
list6=['vvinee','pushpa']
n1,n2=list6
print(n1)
print(n2)