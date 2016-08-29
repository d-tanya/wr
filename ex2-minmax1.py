# min/max array elements

print("input array of numbers separated by spaces:")
a = input()
a = a.split()
try:
    mn = float(a[0])
    mx = float(a[0])
    for i in a:
        if float(i)< mn:
            mn = float(i)
    print('min=',mn)
    for j in a:
        if float(j)>mx:
            mx = float(j)
    print('max=',mx)
except ValueError:
    print("array should be numeric. this element")
except IndexError:
    print("you did't type any array element")
