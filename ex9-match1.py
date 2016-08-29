print("enter text:")
t = input()
t=t.split()
print("enter pattern:")
pat = input()
pat=pat.split()
count = 0
for i in t:
    for j in pat:
        if j==i:
            count +=1
            continue
        else:
            break
if count>0:
    print("pattern is found in typed text")
else:
    print("pattern isn't found in typed text")
        
