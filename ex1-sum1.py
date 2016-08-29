# Sum of array elements

print("enter array of numbers separated by spaces:")
s = input()
a = s.split()
summa = 0
try: 
    for float(elem) for elem in a:
        summa += elem
except ValueError:
	print("This element: ", elem ," not number. All elements in array should be numbers. Only elements before this element are calculated in sum.")
print('summa=',summa)