# По условию нужно, что бы было минимальная длинна подстроки с x букв 't' в ней
# tytyyytytyy t
# 01234567891011
# 00000066666 11
# 00222222888 8
# +1
a = 'tytyyytytyyt'  #Задаём строку
x = 3 #Задаём длину подстроки

ans = 10 ** 10 #Задаём большоооооооооое число
c = [-10 ** 10 for i in range(x - 1)]#
ci = 0#

for i, e in enumerate(a):#
    if e == 't':#
        ans = min(ans, i - c[ci % (x - 1)] + 1)#
        c[ci % (x - 1)] = i#
        ci += 1#

print(ans)#
