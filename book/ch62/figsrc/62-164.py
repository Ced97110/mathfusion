import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
# haut : x^4 - 1, deux choix pour l'image de i, le reste suit
text(ax, 2, 95, r'$x^4-1$', 'autre', 'm', ha='left')
box(ax, 28, 80, 32, 10, 'autre', label=r'image de $i$', size='s')
arrow(ax, (38, 80), (24, 70), 'autre', lw=1.0)
arrow(ax, (50, 80), (64, 70), 'autre', lw=1.0)
box(ax, 14, 60, 20, 10, 'resultat', label=r'$i$', size='m')
box(ax, 54, 60, 20, 10, 'resultat', label=r'$-i$', size='m')
text(ax, 44, 54, 'le reste suit : 2 en tout', 'resultat', 's')
line(ax, [(2, 48), (86, 48)], 'fixe', dash=True)
# bas : x^3 - 2, trois choix puis deux choix
text(ax, 2, 44, r'$x^3-2$', 'sujet', 'm', ha='left')
box(ax, 28, 32, 32, 10, 'sujet', label=r'image de $\sqrt[3]{2}$', size='s')
text(ax, 62, 37, '3 choix', 'sujet', 's', ha='left')
labs = [r'$\sqrt[3]{2}$', r'$j\sqrt[3]{2}$', r'$j^2\sqrt[3]{2}$']
cs = [16, 44, 72]
n = 0
for c, l in zip(cs, labs):
    arrow(ax, (44 + (c - 44) * 0.3, 32), (c, 27), 'sujet', lw=1.0)
    box(ax, c - 11, 17, 22, 10, 'sujet', label=l, size='s')
    for d in (-4.5, 4.5):
        arrow(ax, (c + d * 0.4, 17), (c + d, 11.5), 'varie', lw=0.8)
        disc(ax, c + d, 9, 2.2, 'resultat')
        n += 1
assert n == 6 == 3 * 2
text(ax, 86, 2.5, r'2 choix pour $j$ : 6 en tout', 'varie', 's', ha='right')
save(fig, '62-164')
