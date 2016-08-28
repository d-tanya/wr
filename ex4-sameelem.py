print("input first array separated by spaces:")
a = input()
a = a.split()
print ("input second array separated by spaces:")
b = input()
b = b.split()
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            print("a[",i,"]= b[",j,"]=",a[i])
