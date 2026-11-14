import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 10, 55, 'point (1, 2)', 'encre', 's')
text(ax, 47, 76, 'fonction', 'encre', 's')
text(ax, 77, 76, 'sortie', 'encre', 's')
c1 = (10, 45); c2 = (10, 29)
box(ax, 2, c1[1] - 5, 16, 10, 'sujet', label=r'$s_1 = 1$', size='s')
box(ax, 2, c2[1] - 5, 16, 10, 'sujet', label=r'$s_2 = 2$', size='s')
rows = [('fixe', 'constante 2 : ignore tout', '2'), ('sujet', r'projection 1 : $s_1$', '1'),
        ('autre', r'somme $s_1 + s_2$', '1 + 2 = 0'), ('sujet', r'projection 2 : $s_2$', '2')]
ys = [64, 48, 32, 16]
for (role, lab, out), y in zip(rows, ys):
    box(ax, 26, y - 6, 38, 12, role, label=lab, size='s', dash=(role == 'fixe'))
    arrow(ax, (64.5, y), (67.5, y), 'fixe')
    box(ax, 68, y - 6, 18, 12, role, label=out, size='s')
# la constante ignore le point : aucune flèche ne l'atteint
arrow(ax, (18.5, c1[1]), (25.5, ys[1]), 'varie', lw=1.4)
arrow(ax, (18.5, c1[1] - 1), (25.5, ys[2] + 1), 'autre')
arrow(ax, (18.5, c2[1] + 1), (25.5, ys[2] - 1), 'autre')
arrow(ax, (18.5, c2[1]), (25.5, ys[3]), 'varie', lw=1.4)
save(fig, '55-046')
