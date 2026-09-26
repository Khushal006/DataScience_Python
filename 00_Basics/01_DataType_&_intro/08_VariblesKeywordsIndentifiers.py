# Varibles are not predefine in python interpret assumes the given variable
# int a = 10; in c++ variable is pre defined

print('Variables : an object reference or a label pointing to a dynamically allocated object in memory.')

# Python is intelligent enough to determine the data type

name = 'Khushal'
print(name)

# In C++ we need tp define the datatype while making the variable

print('Python is Dynamic Typing')
print('C++ is Static typing')

# we can store multiple datetype on the same variable in python
# this is called the dynamic binding
# c/c++ do have static binding

a = 10
print(a)
a = 'nitish'
print(a)

# multiple variable in single line

a,b,c = 1,2,3
print(a,b,c)

a=b=c=5
print(a,b,c)

# Keywords - Indentifiers 
"""" there are 32 keywords in the python which we cannot use to 
     call the varibale ex print(print) this will throw error """

"""" A compiler translates the entire program upfront before 
    execution, whereas an interpreter translates and 
    executes the code line-by-line in real-time. """

"""Keywords are reserved words with 
predefined meanings that build the core 
syntax of the language, while identifiers
are custom names given by programmers to 
label elements like variables, functions,
and classes.""" 