import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
s = 8

def scene(o, a, b, cap, area):
    I = lambda p: iso(p[0], p[1], p[2], o, s)
    poly(ax, [I((0, 0, 0)), I((a, 0, 0)), I((a, b, 0)), I((0, b, 0))], 'fixe')
    arrow(ax, I((0, 0, 0)), I((a, 0, 0)), 'sujet', lw=1.2)
    arrow(ax, I((0, 0, 0)), I((0, b, 0)), 'autre', lw=1.2)
    arrow(ax, I((0, 0, 0)), I((0, 0, a * b)), 'resultat', lw=1.8)
    return I

o1, o2 = (16, 14), (58, 8)
I1 = scene(o1, 1, 1, '', 1)
text(ax, I1((1, 0, 0))[0] + 1.5, I1((1, 0, 0))[1] - 2, r'$i$', 'sujet', 'm', ha='left')
text(ax, I1((0, 1, 0))[0] - 1.5, I1((0, 1, 0))[1] + 2, r'$j$', 'autre', 'm')
text(ax, I1((0, 0, 1))[0] - 3, I1((0, 0, 1))[1] + 1, r'$k$', 'resultat', 'm')
text(ax, 18, 4, r'$i\times j=k$', 'resultat', 'm')
I2 = scene(o2, 3, 2, '', 6)
text(ax, I2((3, 0, 0))[0] + 1.5, I2((3, 0, 0))[1] - 2, r'$3i$', 'sujet', 'm', ha='left')
text(ax, I2((0, 2, 0))[0] - 1.5, I2((0, 2, 0))[1] + 2, r'$2j$', 'autre', 'm')
text(ax, I2((0, 0, 6))[0] - 4, I2((0, 0, 6))[1] - 1, r'$6k$', 'resultat', 'm')
text(ax, I2((2.1, 1, 0))[0], I2((2.1, 1, 0))[1], 'aire 6', 'fixe', 's')
text(ax, 60, 2.5, r'$k\perp$ plan de $i$ et $j$ ; longueur = aire', 'resultat', 's')
text(ax, 66, 62,r'$3i\times2j=6k$', 'resultat', 'm')
save(fig, '41-117')
