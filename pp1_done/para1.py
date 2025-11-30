def fun(i):
    global c, l, a
    if l[i] == a:
        c += 1
    if i < len(l) - 1:
        fun(i + 1)

l = [5,3,5,1,5]
a = 5
c = 0
fun(0)
print(f"Елемент {a}, {c}\n")
print(c)
print(l)
print(a)