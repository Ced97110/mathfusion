import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
o = (44, 48); s = 8
P = lambda a, b: (o[0] + a * s, o[1] + b * s)
for cc in (5, -5):
    q = cc / 2
    line(ax, [P(q - 1.6, 3.2), P(q + 1.6, -3.2)], 'fixe', lw=0.9, dash=True)
line(ax, [P(-1.9, 3.8), P(1.9, -3.8)], 'sujet', lw=1.7)
arrow(ax, P(0, 0), P(2, 1), 'autre', lw=1.4)
disc(ax, *P(1, -2), 1.4, 'varie')
d = 2.2; a = (0.894, 0.447); b = (0.447, -0.894)
line(ax, [(o[0] + d * a[0], o[1] + d * a[1]), (o[0] + d * (a[0] + b[0]), o[1] + d * (a[1] + b[1])), (o[0] + d * b[0], o[1] + d * b[1])], 'encre', lw=0.5)
text(ax, P(2, 1)[0] + 8, P(2, 1)[1] + 3, r'$(2,\,1)$', 'autre', 'm')
text(ax, P(-1.9, 3.8)[0] + 4, P(-1.9, 3.8)[1] + 5, 'niveau 0', 'sujet', 's')
text(ax, P(-4.1, 3.2)[0] + 4, P(-4.1, 3.2)[1] + 3, 'autre niveau', 'fixe', 's')
text(ax, P(4.1, -3.2)[0] - 4, P(4.1, -3.2)[1] - 4, 'autre niveau', 'fixe', 's')
text(ax, P(1, -2)[0] + 8, P(1, -2)[1] - 3, r'$(1,\,-2)$', 'varie', 's')
text(ax, 44, 5, r'$2\times1+1\times(-2)=0$', 'resultat', 's')
save(fig, '71-080')
