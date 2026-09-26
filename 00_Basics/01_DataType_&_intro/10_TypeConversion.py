print('Type Conversion')

# Implicit type conversion 

print(5+5.5)
print(type(5),type(5.5))

# Python is intelligent enough
# to understand that if mathamatically
# two different datatypes can add then 
# it can also give the solution

#few things are not possible mathematically
#so python interpreter can't add string with num
""""
fnum = '4'
snum = 5
result = fnum + snum
print(result)
"""

#explicit type converter
#we can convert the str into integer using int()

fnum = '4'
snum = 5
result = int(fnum) + int(snum)
print(result)

# we can also convert integer into str using str()

fstr = '4'
Sstr = 5
result = str(fstr) + str(Sstr)
print(result)

#there are limitation we cannot convert int(4+5j)