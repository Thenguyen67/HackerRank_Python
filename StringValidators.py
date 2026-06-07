
s = input()

a0 = False
a1 = False
a2 = False
a3 = False
a4 = False

for i in s:
    if(i.isalnum()):
        a0 = True
    if(i.isalpha()):
        a1 = True
    if(i.isdigit()):
        a2 = True
    if(i.islower()):
        a3 = True
    if(i.isupper()):
        a4 = True
    
print(a0)
print(a1)
print(a2)
print(a3)
print(a4)
