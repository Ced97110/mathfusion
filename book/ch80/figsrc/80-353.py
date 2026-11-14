import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
text(ax, 24, 53, 'somme', 'sujet', 's')
text(ax, 50, 53, 'on retire', 'limite', 's')
text(ax, 72, 53, 'reste', 'resultat', 's')
def minus(y): line(ax, [(34.5, y), (39.5, y)], 'encre', lw=1.2)
def equals(y):
    line(ax, [(62, y + 1), (67, y + 1)], 'encre', lw=1.2); line(ax, [(62, y - 1), (67, y - 1)], 'encre', lw=1.2)
y = 38
text(ax, 8, y, 'Léa', 'encre', 'm')
for x in (18, 24): disc(ax, x, y, 2.8, 'sujet')
minus(y); disc(ax, 44, y, 2.8, 'limite'); equals(y)
disc(ax, 74, y, 2.8, 'resultat')
text(ax, 44, y - 7, r'$A\cap B$', 'limite', 's')
text(ax, 74, y - 7, '1 fois', 'resultat', 's')
y = 14
text(ax, 8, y, 'Paul', 'encre', 'm')
for x in (18, 24, 30): disc(ax, x, y, 2.8, 'sujet')
minus(y)
for x in (44, 50, 56): disc(ax, x, y, 2.8, 'limite')
equals(y)
disc(ax, 74, y, 2.8, 'limite', fill=False)
text(ax, 50, y - 7, r'$A\cap B$, $A\cap C$, $B\cap C$', 'limite', 's')
text(ax, 74, y - 7, '0 fois : trop', 'limite', 's')
save(fig, '80-353')
