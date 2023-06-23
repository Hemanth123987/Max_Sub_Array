l=[2,-4,5,-1,2,-3]
new_list=[]
for i in range(len(l)):
    for j in range(i,len(l)+1):
        
        a=l[i:j]
        s=sum(a)
        new_list.append(s)
print(max(new_list))