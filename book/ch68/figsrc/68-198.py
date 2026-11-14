import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

# restes de x^i par x^3 = 1 + x, calculés ici : v = (coef. de 1, de x, de x^2)
def mulx(v):
    a, b, c = v
    return (c, a ^ c, b)       # x * (a + b x + c x^2) = a x + b x^2 + c x^3, avec x^3 = 1 + x
rem = [(1, 0, 0)]
for _ in range(6): rem.append(mulx(rem[-1]))
assert rem == [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1),(1,0,1)]
rows = [''.join(str(v[k]) for v in rem) for k in range(3)]
fig, ax = canvas(76)
text(ax, 2, 68, 'puissance', 'fixe', 's', ha='left')
bitrow(fig, ax, 58, 68, '0123456', 'fixe', 'l', 5)
for y, lab, r in zip([56, 46, 36], ['coef. de 1', 'coef. de x', 'coef. de x²'], rows):
    text(ax, 2, y, lab, 'encre', 's', ha='left')
    roles = [('sujet' if i < 3 else 'varie') if c == '1' else 'fixe' for i, c in enumerate(r)]
    brow(fig, ax, 58, y, r, roles=roles)
text(ax, 44, 23, r'règle : $x^3 = 1 + x$', 'varie', 'm')
text(ax, 44, 15, r'colonne $i$ : reste de $x^i$', 'encre', 's')
save(fig, '68-198')
