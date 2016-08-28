print("enter text:")
t = input()
t=t.split()
print("enter pattern:")
pat = input()
pat=pat.split()
count = 0
for i in range(len(t)):
    for j in range(len(pat)):
        if pat[j]==t[i]:
            count +=1
            continue
        else:
            break
if count>0:
    print("pattern is found in typed text")
else:
    print("pattern isn't found in typed text")
        
