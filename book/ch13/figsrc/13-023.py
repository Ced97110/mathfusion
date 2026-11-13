import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 18
f = numberline(ax, 8, 70, y, -3, 3, every=3, arrow_right=False)
box(ax, f(-3) - 3, y + 6, f(0) - f(-3) - 3, 9, 'autre', label=r'gauche : $-$', size='s')
box(ax, f(0) + 6, y + 6, f(3) - f(0) + 3, 9, 'sujet', label=r'droite : $+$', size='s')
line(ax, [(f(0), y + 1.5), (f(0), y + 15)], 'fixe', dash=True)
disc(ax, f(0), y, 2.0, 'resultat')
text(ax, f(0), y - 11, '0 : aucun signe', 'resultat', 'm', weight='bold')
save(fig, '13-023')
