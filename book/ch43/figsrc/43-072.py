import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y = 34; X = {3: 14, 15: 44, 27: 74}
line(ax, [(6, y), (82, y)], 'fixe', lw=0.7)
box(ax, 6, 24, 44, 20, 'sujet', fill=False, lw=1.1); box(ax, 38, 24, 44, 20, 'autre', fill=False, lw=1.1, dash=True)
text(ax, 20, 49, r'classe de 3', 'sujet', 's'); text(ax, 68, 49, r'classe de 27', 'autre', 's')
for v, x in X.items(): disc(ax, x, y, 2.3, 'varie' if v == 15 else 'fixe'); text(ax, x, y - 6.5, str(v), 'varie' if v == 15 else 'fixe', 'm')
text(ax, 44, 58, 'le 15 est dans les deux', 'varie', 's')
arrow(ax, (44, 18), (44, 12), 'fixe') if False else None
box(ax, 8, 1, 72, 11, 'resultat'); text(ax, 44, 8.5, r'$27-3=24=2\times 12$', 'resultat', 'm'); text(ax, 44, 4.2, r'donc $\bar{3}=\bar{27}$', 'resultat', 'm')
save(fig, '43-072')
