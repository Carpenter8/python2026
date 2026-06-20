var={10,'vineet',True,1.2,True,1.2}
print(var)
print(type(var))
#add
var.add("power")
print(var)


# print(var(1)) #error


var.update(['power full'])
print(var)


#remove 
print(var.pop())
print(var)

var.remove("vineet")
print(var)


#clear methods

var.clear()
print(var)


var2={15,'vineet',True,1.9,True,1.5}

print(var.union(var2))
print(var | (var2))


print(var.intersection(var2)) #jo value common value print hoga hai 
print(var & (var2))

print(var.difference(var2))
print(var - (var2))


print(var.symmetric_difference(var2))