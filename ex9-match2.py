print("enter text:")
t = input()
print("enter pattern:")
pat = input()

if pat in t:
    print ("pattern is found in typed text")
else:
    print ("pattern isn't found in typed text")

# # second version
# if t.find(pat)>0:
#     print ("pattern is found in typed text")
# else:
#     print("pattern isn't found in typed text")
