import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
n = lambda v: str(v).replace('-', '−')
A, B = (1, 2, 1), (0, 1, -1)
S = tuple(p + q for p, q in zip(A, B))
assert S == (1, 3, 0)
xs = [30, 49, 68]
for x, h in zip(xs, ['1re case', '2e case', '3e case']):
    text(ax, x, 61, h, 'fixe', 's')
rows = [('a', A, 'sujet', 48), ('b', B, 'autre', 36), (r'$a+b$', S, 'resultat', 20)]
for lab, v, role, y in rows:
    text(ax, 8, y + 4.5, lab, role, 'l')
    for x, c in zip(xs, v):
        box(ax, x - 8, y, 16, 9, role, label=n(c))
text(ax, 8, 46.5, '+', 'encre', 'm')
line(ax, [(2, 31.5), (86, 31.5)], 'encre', lw=0.9)
text(ax, 44, 10, r'$1+0=1$ ; $2+1=3$ ; $1-1=0$', 'resultat', 'm')
text(ax, 44, 3.5, r'obtenu avec les paramètres 1 et 1 : dans $W$', 'resultat', 's')
save(fig, '58-128')
