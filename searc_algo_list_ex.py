list=["Ion","Maria","Bob","George"]
found=[False,False]
item=["Alexandru","George"]


for i in range(len(item)):
    for j in range(len(list)):
        found[i]=list[j]==item[i]
        if found[i]:
            break

print(item)
print(found)      
for i in range(len(item)):
    if found[i]:
        print(item[i], "item found")
    else:
        print(item[i],"ITEM NOT FOUND")




    
        


        


        
