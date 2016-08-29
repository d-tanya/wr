# Sum of array elements

print("enter array of numbers separated by spaces:")
s = input()
a = s.split()
summa = 0
try: 
    for elem in a:
        elem = float(elem)
        summa += elem
except ValueError:
	print("This element: ", elem ," not number. All elements in array should be numbers")
print('summa=',summa)