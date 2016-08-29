print("input first array separated by spaces:")
a = input()
a = a.split()
print ("input second array separated by spaces:")
b = input()
b = b.split()
for i in a:
    for j in b:
        if i==j:
            print("matched element=",i)
