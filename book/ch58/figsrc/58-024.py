import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# M = M1 ⊕ M2 : le plus dit « une somme existe », le cercle dit « une seule écriture »
y = 50
text(ax, 14, y, r'$M$', 'sujet', 'xl', weight='bold')
text(ax, 25, y, '=', 'encre', 'xl')
text(ax, 38, y, r'$M_1$', 'sujet', 'xl', weight='bold')
text(ax, 62, y, r'$M_2$', 'autre', 'xl', weight='bold')
cx = 50
disc(ax, cx, y, 4.2, 'resultat', fill=False, lw=1.5)
line(ax, [(cx - 2.4, y), (cx + 2.4, y)], 'sujet', lw=1.5)
line(ax, [(cx, y - 2.4), (cx, y + 2.4)], 'sujet', lw=1.5)
# deux sens
arrow(ax, (cx - 2, y - 6), (28, 31), 'sujet', lw=1.0)
arrow(ax, (cx + 2, y - 6), (72, 31), 'resultat', lw=1.0)
box(ax, 4, 15, 46, 15, 'sujet', label='le plus : tout élément\nest une somme', size='s')
box(ax, 52, 15, 34, 15, 'resultat', label='le cercle : une\nseule écriture', size='s')
text(ax, 44, 7, 'se lit : M égale M un somme directe M deux', 'fixe', 's')
save(fig, '58-024')
