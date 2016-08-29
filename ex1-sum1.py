# Sum of array elements

print("enter array of numbers separated by spaces:")
s = input()
a = s.split()
summa = 0
try: 
    floats = [float(elem) for elem in a]
    for i in floats:
        summa += i
except ValueError:
	print("All elements in array should be numbers.")
print('summa=',summa)