# min/max array elements

print("input array of numbers separated by spaces:")
a = input()
a = a.split()
try:
    mn = float(a[0])
    mx = float(a[0])
    for i in range(len(a)):
        if float(a[i])< mn:
            mn = float(a[i])
    print('min=',mn)
    for i in range(len(a)):
        if float(a[i])>mx:
            mx = float(a[i])
    print('max=',mx)
except ValueError:
    print("array should be numeric")
except IndexError:
    print("you did't type any array element")

