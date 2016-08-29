# quicksort array

print("input array of numbers separated by spaces:")
a = input()
a = a.split()
try:
    for i in range(len(a)):
        a[i] = float(a[i])

    def sort(a=[]):
        beforepart = []
        samepart = []
        afterpart = []
        if len(a)<2:
            return a
        else:
            startelem = a[0]
            for i in a:
                if i < startelem:
                    beforepart.append(i)
                elif i == startelem:
                    samepart.append(i)
                elif i > startelem:
                    afterpart.append(i)
            arr = sort(beforepart)+samepart+sort(afterpart)
            return arr

    k = sort(a)
    print(k)

except ValueError:
    print("array should be numeric")


