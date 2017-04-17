file = open("config_v2_ex10.txt","r")

y = file.readlines()
year = int(str(y[0]))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print ("September 13th")
else:
    print ("September 12th")