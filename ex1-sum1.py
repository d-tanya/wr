# Sum of array elements

print("enter array of numbers separated by spaces:")
s = input()
a = s.split()
summa = 0
try: 
    for i in range(len(a)):
        a[i] = float(a[i])
        summa += a[i]
    print('summa=',summa)
except ValueError:
    print("array should be numeric")
