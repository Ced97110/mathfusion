import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 24; o = (30, 10)
P = lambda a, b: (o[0] + s*a, o[1] + s*b)
for d in ((1, 0), (0, 1), (1, 1)):
    line(ax, [(o[0]-0.25*s*d[0], o[1]-0.25*s*d[1]), P(1.3*d[0], 1.3*d[1])], 'sujet', lw=1.3)
for a in (0, 1):
    for b in (0, 1):
        disc(ax, *P(a, b), 1.2, 'fixe' if (a, b) == (0, 0) else 'sujet')
        text(ax, P(a, b)[0] + (4.5 if a else -4.5), P(a, b)[1] + (2.5 if b else -2.5), f'({a}, {b})', 'encre', 's')
text(ax, 44, 61, r'$P_1(F)$ : 3 droites', 'sujet', 'm')
text(ax, 72, 30, 'une droite =', 'sujet', 's'); text(ax, 72, 25, '(0, 0) et un', 'sujet', 's'); text(ax, 72, 20, 'autre point', 'sujet', 's')
save(fig, '73-056')
