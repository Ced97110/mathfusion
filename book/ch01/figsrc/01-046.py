import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
box(ax, 20, 52, 48, 18, 'fixe', fill=False, dash=True)
text(ax, 44, 65, '0 étagère de 6 boîtes', 'fixe', 's')
text(ax, 44, 57, '0 × 6 = 0', 'resultat', 'l', weight='bold')
box(ax, 3, 18, 22, 20, 'sujet', fill=False, dash=True, lw=1.2)
text(ax, 14, 42, 'point de départ', 'sujet', 's', weight='bold')
text(ax, 14, 12, '0 × 3 = 0', 'sujet', 'm')
box(ax, 33, 18, 22, 20, 'fixe', fill=False)
box(ax, 63, 18, 22, 20, 'fixe', fill=False)
for x in (38, 43, 48):
    box(ax, x, 26, 4, 4, 'varie', r=0.3, lw=0.6)
for x in (68, 73, 78):
    box(ax, x, 23, 4, 4, 'fixe', r=0.3, lw=0.6)
    box(ax, x, 29, 4, 4, 'varie', r=0.3, lw=0.6)
for x0 in (26, 56):
    arrow(ax, (x0, 28), (x0 + 6, 28), 'varie')
    text(ax, x0 + 3, 33, '+ 3', 'varie', 's')
text(ax, 44, 12, '1 × 3 = 3', 'resultat', 'm')
text(ax, 74, 12, '2 × 3 = 6', 'resultat', 'm')
save(fig, '01-046')
