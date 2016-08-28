# Sum of array elements 2

print("enter array of numbers separated by spaces:")
s = input()
s = s.split()
try:
    for i in range(len(s)):
        s[i] = float(s[i])
except ValueError:
    print("array should be numeric")
sm = sum(s)
print ('summa=',sm)
