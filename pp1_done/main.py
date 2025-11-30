lst = (5, 3, 5, 5, 5)
a = 5
result = ()
for x in lst:
    result += (x * 2,) \
        if x == a else (x,)
print(result)
#--------------