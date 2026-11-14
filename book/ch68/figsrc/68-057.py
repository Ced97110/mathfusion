import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)

def d(a, b):
    return sum(p != q for p, q in zip(a, b))

x, y, z = '10101', '11010', '00011'
dxz, dxy, dyz = d(x, z), d(x, y), d(y, z)
assert (dxz, dxy, dyz) == (3, 4, 3) and dxz <= dxy + dyz
u = 9.0
x0 = 6
text(ax, 44, 55, 'longueurs en nombre de positions', 'fixe', 's')
box(ax, x0, 38, dxz * u, 9, 'sujet', label=r'$d(x, z) = 3$')
text(ax, x0 + dxz * u + 3, 42.5, '3', 'sujet', 'l', ha='left', weight='bold')
box(ax, x0, 18, dxy * u, 9, 'varie', label=r'$d(x, y) = 4$')
box(ax, x0 + dxy * u, 18, dyz * u, 9, 'varie', label=r'$d(y, z) = 3$')
brace(ax, x0, x0 + (dxy + dyz) * u, 18, 'varie', label=r'$4 + 3 = 7$', size='m')
text(ax, 44, 4, r'$3 \leq 7$', 'encre', 'l', weight='bold')
save(fig, '68-057')
