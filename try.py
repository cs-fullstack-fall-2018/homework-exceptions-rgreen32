

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Cant multiply letters by numbers")



#############################
try:
    x = 5
    y = 0

    z = x/y
except:
    print("Cant do that")

finally:
    print("All Done")