import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 12, 52, 64, 12, 'sujet', label=r'$x_1^2+x_2^2+x_1+x_2$', size='l')
parts = [(3, 'degré 2', r'$x_1^2+x_2^2$'), (47, 'degré 1', r'$x_1+x_2$')]
for x, d, f in parts:
    cx = x + 19
    arrow(ax, (cx, 52), (cx, 38), 'fixe')
    text(ax, cx + 2, 45, d, 'fixe', 's', ha='left')
    box(ax, x, 26, 38, 12, 'sujet', label=f, size='m')
    text(ax, cx, 20, r'on échange $x_1\leftrightarrow x_2$', 'varie', 's')
    text(ax, cx, 13, 'inchangé', 'resultat', 'm', weight='bold')
save(fig, '55-095')
