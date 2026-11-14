import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, s = 14, 30, 12
P = lambda a, b: (ox + a * s, oy + b * s)
arrow(ax, P(-0.5, 0), P(5, 0), 'sujet', lw=1.5)
arrow(ax, P(0, -0.5), P(0, 3.6), 'autre', lw=1.5)
text(ax, P(5, 0)[0] - 3, P(5, 0)[1] - 4, r'droite $Fu$ : $b=0$', 'sujet', 's', ha='right')
text(ax, P(0, 3.6)[0] + 2, P(0, 3.6)[1], r'droite $Fv$ : $a=0$', 'autre', 's', ha='left')
for (a, b), role, t, dx, dy in (((3, 0), 'resultat', r'$(3\ ;\ 0)$ : 0', 0, 5), ((0, 2), 'resultat', r'$(0\ ;\ 2)$ : 0', 3, 0), ((1, 1), 'limite', r'$(1\ ;\ 1)$ : 2', 3, 0)):
    disc(ax, *P(a, b), 1.5, role)
    text(ax, P(a, b)[0] + dx, P(a, b)[1] + dy, t, role, 's', ha='left' if dx else 'center')
text(ax, 44, 76, r'carré de $au+bv$ : $2ab$', 'encre', 'm')
text(ax, 44, 8, r'$2ab=0$ force $a=0$ ou $b=0$', 'encre', 'm')
save(fig, '72-053')
