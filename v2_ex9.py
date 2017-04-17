import datetime
file = open("config_v2_ex9.txt","r")

t = file.readlines()
# print(t)
a = t[0]
b = t[1]

a = a.split('-')
b = b.split('-')
aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
cc = aa-bb
dd = str(cc)
print(dd.split()[0])