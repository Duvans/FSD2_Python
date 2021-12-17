#Assignment1
temp = 0
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949
  ]

for i in numbers:
    if i % 2 == 0:
        if i <= 918:
            print(i)
print("Done")

#improvement => 
print("\n===IMPROVEMENT===\n")
#1 Sorting List in Ascending and Descending Order
print("#1 Sorting List in Ascending and Descending Order\n")
numbers.sort()
print('list in Ascending Order: ', numbers)

numbers.sort(reverse= True)
print('List in Descending Order: ', numbers)

#2 Print even numbers that more than or equal to 918 
print("\n\n#2 Print even numbers that more than or equal to 918\n")
for i in numbers:
    if i % 2 == 0:
        if i >= 918:
            print(i)
print("Done\nThank You")
