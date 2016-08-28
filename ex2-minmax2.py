# min/max array elements

print("input array of numbers separated by spaces:")
a = input()
a = a.split()
try:
    mn = min(a)
    mx = max(a)
    print("min=",mn)
    print("max=",mx)
except ValueError:
    print("you didn't type any array element")
