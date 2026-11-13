import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, x1 = 8, 74
f = numberline(ax, x0, x1, 40, 0, 6, labels=False)
u = f(1) - f(0)
for k in range(4):
    box(ax, f(0) + k * u / 4, 42, u / 4, 6, 'resultat', r=0.2)
text(ax, f(0) + 4 * u, 52, r'$4\times\frac{1}{4}$', 'resultat', 'l')
text(ax, f(1), 32, '= 1 : inverses', 'resultat', 'm', ha='left')
f2 = numberline(ax, x0, x1, 12, 0, 6, labels=False)
for k in range(2):
    box(ax, f2(0) + k * 3 * u, 14, 3 * u, 6, 'limite', label='3')
text(ax, f2(3), 26, r'$2\times3$', 'limite', 'l')
text(ax, f2(6), 4, '= 6, pas 1', 'limite', 'm')
save(fig, '06-061')
