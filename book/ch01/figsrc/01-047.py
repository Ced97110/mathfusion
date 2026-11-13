import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
text(ax, 44, 59, '4 lignes de 3 boîtes', 'encre', 'm', weight='bold')
for r, (y, t) in enumerate(zip((8, 15.5, 23), ('3', '6', '9'))):
    for x in (6, 13.5, 21):
        box(ax, x, y, 6, 6, 'fixe', r=0.4, lw=0.6)
    text(ax, 33, y + 3, t, 'fixe', 's')
for x in (6, 13.5, 21):
    box(ax, x, 30.5, 6, 6, 'varie', r=0.4, lw=0.6)
text(ax, 17, 43, 'ligne 4 : + 3', 'varie', 's', weight='bold')
text(ax, 33, 33.5, '12', 'resultat', 'm', weight='bold')
text(ax, 63, 46, '4 = suivant de 3', 'sujet', 'm')
text(ax, 63, 36, '4 × 3 = 3 × 3 + 3', 'varie', 'm')
text(ax, 63, 26, '3 × 3 = 9', 'fixe', 'm')
text(ax, 63, 16, '9 + 3 = 12', 'resultat', 'l', weight='bold')
save(fig, '01-047')
