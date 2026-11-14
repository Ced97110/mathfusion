import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
box(ax, 2, 64, 16, 11, 'fixe', label=r'$b^2$'); box(ax, 24, 62, 30, 15, 'sujet', label=r'$D=b^2-4ac$', weight='bold')
box(ax, 60, 64, 12, 11, 'fixe', label=r'$\sqrt{D}$'); box(ax, 76, 64, 10, 11, 'fixe', label=r'$x$')
arrow(ax, (18.5, 69.5), (23.5, 69.5), 'fixe', ); arrow(ax, (54.5, 69.5), (59.5, 69.5), 'fixe'); arrow(ax, (72.5, 69.5), (75.5, 69.5), 'fixe')
text(ax, 39, 55, 'seul son signe décide', 'sujet', 's')
for i, (t, r, s) in enumerate([(r'$D>0$', 'resultat', r'$\sqrt{D}$ existe'), (r'$D=0$', 'resultat', r'$\sqrt{D}$ existe'), (r'$D<0$', 'limite', 'pas de racine')]):
    x = 2 + i*29.5
    box(ax, x, 30, 26, 11, r, label=t); text(ax, x+13, 22, s, r, 's')
    arrow(ax, (39, 52), (x+13, 41.5), 'fixe')
save(fig, '23-063')
