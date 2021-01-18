d={}


for i in range(10000000):
    key=input("Enter the key:")
    if key=="":
        break
    val=input("Enter the value:")

    d[key]=val

print('You have now', len(d),'values')
print('The dictionary contains:',d)

#HW3: Modiy the FOR loop or WHILE, so it STOPS KEY-->""