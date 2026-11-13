import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for k, (lab, r) in enumerate([(r'$(x_1,x_2)$', 'sujet'), (r'$(-x_1,x_2)$', 'varie'), (r'$(x_2,-x_1)$', 'resultat')]):
    box(ax, 2 + k * 31, 52, 22, 12, r, label=lab, size='s')
arrow(ax, (24.5, 58), (32.5, 58), 'varie'); arrow(ax, (55.5, 58), (63.5, 58), 'varie')
text(ax, 28.5, 62.5, r'$s_1$', 'varie', 's'); text(ax, 59.5, 62.5, r'$s_2$', 'varie', 's')
vals = [['0', '1'], ['-1', '0']]
for i in range(2):
    for j in range(2):
        box(ax, 8 + j * 13, 22 - i * 13, 11, 11, 'sujet', label=r'$%s$' % vals[i][j], size='m')
text(ax, 22, 5, 'la matrice', 'sujet', 's')
text(ax, 43, 24, r'$=R_{-90°}$', 'resultat', 'm')
cc = (68, 24); r = 11
pts = [(cc[0]+r*math.cos(math.radians(a)), cc[1]+r*math.sin(math.radians(a))) for a in range(0, -86, -3)]
disc(ax, cc[0], cc[1], r, 'fixe', fill=False, lw=0.6)
line(ax, pts[:-2], 'resultat', lw=1.6); arrow(ax, pts[-3], pts[-1], 'resultat', lw=1.6)
text(ax, 68, 5, 'quart de tour horaire', 'resultat', 's')
text(ax, 78, 28, r'$-90°$', 'resultat', 's')
save(fig, '74-110')
