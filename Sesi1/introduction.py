# integers
print(123123123123123123123123123123123123123123123123 + 1)
print(10)
print(type(10))

#floating-point numbers
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

#Strings
print("Hacktiv8")
print(type("Hacktiv8"))
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

#Boolean
print(type(True))
print(type(False))

print(100 > 200) #False
print(100 == 200) #False
print(100 < 200) #True

#Variable Assignment
n=300
print(n)

a=b=c=400
print(a,b,c)

#Variable Names
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
# Camel Case, Example: numberOfCollegeGraduates
# Pascal Case, Example: NumberOfCollegeGraduates
# Snake Case,Example: number_of_college_graduates

#Operators and Expressions
a = 10
b = 20
print(a + b)
print(a + b - 5)

#Arithmetic Operators
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

#String Manipulation
s = 'foo'
t = 'bar'
# + and * Operators
print(s + t )
print(s * 4)
#Case Conversion
print(s.capitalize())
print(s.lower())
print(s.swapcase())

#Python Lists
a = ['foo', 'bar', 'baz', 'qux']
print(a)

#Modifying List Value
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-1] = 20
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

#Python Tuples
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])
# packing and unpacking
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1)

#Defining and Accessing Dictionary
MLB_team = {    'Colorado': 'Rockies',    'Boston': 'Red Sox',    'Minnesota': 'Twins',}
print(MLB_team['Minnesota'])
#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
MLB_team

#Building a Dictionary Incrementally
person = {}
person['fname'] = 'Hack'
person['lname'] = '8'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])


