# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# ○ Eg - line = “which is better python 2 or python 3”

input1="which is better python 2 or python 3"
res=[]
out=input1.split()
for i in out:
    res.append((i,out.count(i)))

print(res)