# Literals the value you store in variable is called literals

print("Literals can be stores by different ways")

a = 0b1010 #binary literal
b = 100 #Decimal literal
c = 0o310 #octal literal
d = 0x12c #Hexadecimal

print(a)
print(b)
print(c)
print(d)

# Float Literal

float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

print(float_1)
print(float_2)
print(float_3)

# Complex Literals

x = 3.14j
print(x.real, x.imag) #it can take real than imaginary part of the imaginary number

#string Literals

string = "This is Python"
strings = 'This is Python'
char = 'c'
multi_str = """ this is 
                multiline-str
                you can write 
                string in multiple
                lines"""

print(string)
print(strings)
print(char)
print(multi_str)

# Unicode can be used using u"\unicode"

unicode = u"\U0001F600\U0001F60E"
print(unicode)

# Rawstring - In Python, a raw string is a string literal prefixed with an r or R that treats the backslash character (\) as a literal character rather than an escape character

raw_string = r"raw\nstring"
print(raw_string)

# Boolean - In Python, we can also do the mathematical operations on boolean

a = True+4
b = False+10
print(a)
print(b)

# None - In Python, we have none so prestore a variable with none and use it later on
# Python, Didn't allow us to just create a variable without storing anything

""""
k
a = 3
b = 5
print('program_exe')
this return ERORR
"""

k = None
a = 5
b = 10
print('program_exe')