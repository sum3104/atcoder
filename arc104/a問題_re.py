import sympy as sp

a, b = map(int, input().split())

x, y = sp.symbols('x y')
eq1 = x + y - a
eq2 = x - y - b
ans = sp.solve([eq1, eq2])
print(ans[x], ans[y])
