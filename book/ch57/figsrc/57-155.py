import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
xs = [14, 34, 54, 74]
top = [2, 3, 4, 5]; bot = [6, 9, 12, 15]
box(ax, 3, 2, 82, 38, 'resultat', fill=False, dash=True)
text(ax, 44, 41.3, 'arrivée', 'resultat', 's', weight='bold')
for x, a, b in zip(xs, top, bot):
    disc(ax, x, 66, 3.6, 'sujet', label=str(a), size='m')
    disc(ax, x, 27, 3.6, 'resultat', label=str(b), size='m')
    arrow(ax, (x, 62.2), (x, 31), 'varie', lw=1.0)
text(ax, 44, 48.5, r'$\times 3$', 'varie', 'm')
text(ax, 6, 72, 'départ', 'encre', 'm', ha='left', weight='bold')
text(ax, 44, 14, '6 + 9 = 15 : encore dans l’image', 'resultat', 's')
text(ax, 44, 7, '2 × 6 = 12 : encore dans l’image', 'resultat', 's')
save(fig, '57-155')
