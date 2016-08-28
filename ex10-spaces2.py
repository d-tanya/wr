print("enter text:")
t = input()
t = t.split()
try:
    a = t[0]
    for i in range(1,len(t)):
        a = a+t[i]
    print(a)
except IndexError:
    print("you didn't type any text")
