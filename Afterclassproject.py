Val1={'Codingal':3 ,'is':2, "best":2, "for":2, "coding":1 }
print(Val1)
x = 2
z = 0
for i in Val1:
    if Val1[i] == x:
        z = z + 1
print("The number of time ", x, "repeats in the text above:", z)