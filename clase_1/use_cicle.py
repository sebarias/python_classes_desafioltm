#elemento iterable  
a = range(5) 
b = range(1,5)
print(a)
for i in a:
    print(i)

c = "amapola"
print(c.count("a"))

for i in range(20):
    if i % 2 == 0 and i != 0:
        print(i)