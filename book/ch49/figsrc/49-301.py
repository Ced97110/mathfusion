import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, y0, s = 10, 14, 8.5
for i in range(4):
    for j in range(6):
        disc(ax, x0 + i * s, y0 + j * s, 0.7, 'fixe')
p = (x0 + 3 * s, y0)
q = (x0 + 3 * s, y0 + 5 * s)
arrow(ax, (x0 + 1.2, y0), (x0 + 1 * s - 1, y0), 'sujet', lw=1.6)
line(ax, [(x0 + s, y0), (p[0], p[1])], 'sujet', lw=1.6)
arrow(ax, (p[0], y0 + 1.2), (p[0], y0 + 5 * s - 1.2), 'autre', lw=1.6)
disc(ax, q[0], q[1], 1.6, 'resultat')
text(ax, q[0] - 3, q[1] + 3.5, r'$(3,5)$', 'resultat', 's', ha='right')
text(ax, x0 + 1.5 * s, y0 - 4, r'3 fois $(1,0)$', 'sujet', 's')
text(ax, p[0] + 3, y0 + 2.5 * s, r'5 fois $(0,1)$', 'autre', 's', ha='left', rot=0)
text(ax, 66, 58, 'couples d’entiers', 'encre', 's')
box(ax, 58, 28, 28, 20, 'resultat')
text(ax, 72, 42, r'$(3,5) =$', 'resultat', 'm')
text(ax, 72, 36, r'3 $\times (1,0)$', 'sujet', 's')
text(ax, 72, 31, r'+ 5 $\times (0,1)$', 'autre', 's')
save(fig, '49-301')
