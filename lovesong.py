import string





str1="aacaba"

n=1
q=3
count =0
str2=""
temp=str1[n-1:q]


for i in temp:
        
        str2+=(((string.ascii_lowercase.index(i))+1)*i)
    
print(str2)
print(len(str2))
