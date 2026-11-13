import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(84)
# titres de colonne
text(ax, 23, 80, 'exposant', 'sujet', 's')
text(ax, 65, 80, 'signe fois', 'autre', 's')
# haut-gauche : 2³ = 2 × 2 × 2 = 8 (deux blocs de 2 × 2)
text(ax, 23, 73, r'$2^{3}$ = 2 × 2 × 2', 'sujet', 'm')
for cx in [11, 17, 29, 35]:
    for cy in [67, 61]:
        disc(ax, cx, cy, 2, 'sujet')
text(ax, 23, 54, '8', 'resultat', 'l')
# haut-droite : 2 × 3 = 6 (deux rangées de 3)
text(ax, 65, 73, '2 × 3', 'autre', 'm')
for cx in [59, 65, 71]:
    for cy in [67, 61]:
        disc(ax, cx, cy, 2, 'autre')
text(ax, 65, 54, '6', 'autre', 'l')
text(ax, 44, 64, '≠', 'varie', 'l')
# bas-gauche : 3² = 3 × 3 = 9 (trois rangées de 3)
text(ax, 23, 47, r'$3^{2}$ = 3 × 3', 'sujet', 'm')
for cx in [17, 23, 29]:
    for cy in [41, 35, 29]:
        disc(ax, cx, cy, 2, 'sujet')
text(ax, 23, 22, '9', 'resultat', 'l')
# bas-droite : 3 × 2 = 6 (trois rangées de 2)
text(ax, 65, 47, '3 × 2', 'autre', 'm')
for cx in [62, 68]:
    for cy in [41, 35, 29]:
        disc(ax, cx, cy, 2, 'autre')
text(ax, 65, 22, '6', 'autre', 'l')
text(ax, 44, 35, '≠', 'varie', 'l')
text(ax, 44, 10, 'en haut : nombre de facteurs', 'varie', 's')
save(fig, '04-027')
