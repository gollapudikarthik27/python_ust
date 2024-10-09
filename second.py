input1="which is better python 2 or python 3"
res=[]
out=input1.split()
for i in out:
    res.append((i,out.count(i)))

print(res)
