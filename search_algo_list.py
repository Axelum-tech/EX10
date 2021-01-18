container =["John","Marry","Bob"]
item      ="John"



for i in range(len(container)):
    found  = container[i]==item #tip boolean
    if found:
        break
        print()
    
if found:
    print(item,"FOUND!!!")
else:
    print("NOT FOUND!!!")

