#Python "while" Loops
#1
n = 5
while n > 0:
    n -= 1
    print(n)

#2
i = 1
while i < 6:
  print(i)
  i += 1

#3
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

#4
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

#The else clause
#1
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

#2
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

#Nested while Loops
#1
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

#One-Line while Loops
n = 5
while n > 0: n -= 1; print(n)

#The Python for Loop
#1
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

#2
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

#3
for k in d:
    print(d[k])

#4
for k in d.values():
    print(k)

#5
for k, v in d.items(): 
    print(k, ":", v) 

#Iterating Through a Dictionary
#1
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

#2
for k in d:
    print(d[k])

#3
for v in d.values():
    print(v)

#The range() Function
#1
for n in (0, 1, 2, 3, 4):
    print(n)

#2
x = range(5)
for n in x:
    print(n)

#Altering for Loop Behavior
    #The break and continue statements
#1
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

#2
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

#3
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

#4
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 
