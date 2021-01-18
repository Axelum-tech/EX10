container =["Marry","John","Bob"] #heist tag
found     =[False, False, False]
item      =["name1"]     #needle
# name1=str(input(name1))
# name2=str(intput(name2))
# name3=str(input(name3))


for j in range(len(item)):

    for i in range(len(container)):
        found[j]  = container[i]==item[j] #tip boolean
        if found[j]:
            break

# print(item)
# print(found)
for j in range(len(item)):
    if found[j]:
        print(item[j],"FOUND!!!")
    else:
        print("NOT FOUND!!!")

