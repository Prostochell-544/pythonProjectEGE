import sys

sys.setrecursionlimit(10000)
def F(n):
    if n<=6:
        return n
    else:
        return 2*n+3+F(n-1)
print(F(6188)-F(6185))
############################################################3034 780 3085 6848
#НОРМ РЕШЕНИЕ
############################################################
f = {n: n for n in range(1, 7)}
for n in range(7, 7000):
    f[n] = 2 * n + 3 + f[n - 1]
print(f[6188] - f[6185])
print(2 * 6188 + 3 + 2 * 6187 + 3 + 2 * 6186 + 3)
