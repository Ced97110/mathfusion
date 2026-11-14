import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# horloge à 2 heures : 2·1 = 0 (un tour complet) et 0·1 = 0 (on reste) : l'heure 0 s'écrit de deux façons
r = 10
def clock(cx, cy):
    disc(ax, cx, cy, r, 'fixe', fill=False, lw=1.0)
    disc(ax, cx, cy + r, 2.2, 'resultat', label='0', size='s')
    disc(ax, cx, cy - r, 2.2, 'autre', label='1', size='s')
clock(22, 34)
clock(66, 34)
# gauche : deux pas de 1, un tour complet
arrow(ax, (22 + 2.6, 34 + r - 2.0), (22 + 2.6, 34 - r + 2.0), 'varie', lw=1.3, curve=-0.45)
arrow(ax, (22 - 2.6, 34 - r + 2.0), (22 - 2.6, 34 + r - 2.0), 'varie', lw=1.3, curve=-0.45)
text(ax, 22, 34, '1 + 1', 'varie', 's')
text(ax, 22, 12, r'$2 \cdot 1 = 0$', 'varie', 'm', weight='bold')
text(ax, 66, 34, 'aucun pas', 'fixe', 's')
text(ax, 66, 12, r'$0 \cdot 1 = 0$', 'fixe', 'm', weight='bold')
text(ax, 44, 60, 'deux façons d’obtenir 0', 'resultat', 'm', weight='bold')
save(fig, '58-013')
