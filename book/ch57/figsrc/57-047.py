import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
# ligne 1 : 18 + 27
box(ax, 2, 54, 38, 10, 'sujet', label='18', size='l')
text(ax, 44, 59, '+', 'fixe', 'l', weight='bold')
box(ax, 48, 54, 38, 10, 'autre', label='27', size='l')
# étape 1 : couper, seulement « respecter + »
arrow(ax, (21, 53.5), (21, 44.5), 'fixe', lw=1.0)
arrow(ax, (67, 53.5), (60, 44.5), 'fixe', lw=1.0)
text(ax, 44, 48.5, 'respecter +', 'fixe', 's')
cx = [13, 30, 52, 69]
box(ax, 2, 34, 84, 10, 'fixe')
row2 = [('8 +', 'fixe', 'normal'), ('10 +', 'varie', 'bold'), ('12 +', 'varie', 'bold'), ('15', 'fixe', 'normal')]
for c, (s, role, w) in zip(cx, row2):
    text(ax, c, 39, s, role, 'm', weight=w)
# étape 2 : regrouper, il faut mettre 12 avant 10
arrow(ax, (30, 33.5), (52, 15.5), 'varie', lw=1.8)
arrow(ax, (52, 33.5), (30, 15.5), 'varie', lw=1.8)
text(ax, 2, 25, 'seul usage de a + b = b + a', 'varie', 's', ha='left', weight='bold')
box(ax, 3, 4, 38, 10, 'resultat')
box(ax, 45, 4, 38, 10, 'resultat')
row3 = [('(8 +', 'fixe', 'normal'), ('12) +', 'varie', 'bold'), ('(10 +', 'varie', 'bold'), ('15)', 'fixe', 'normal')]
for c, (s, role, w) in zip(cx, row3):
    text(ax, c, 9, s, role, 'm', weight=w)
save(fig, '57-047')
