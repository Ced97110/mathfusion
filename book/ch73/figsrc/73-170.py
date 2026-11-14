import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 24, 74, r'$F_3$ : 3 éléments', 'encre', 'm'); text(ax, 64, 74, r'$F_5$ : 5 éléments', 'encre', 'm')
text(ax, 24, 66, 'nombre → son inverse', 'fixe', 's'); text(ax, 64, 66, 'nombre → son inverse', 'fixe', 's')
def pair(cx, y, a, b, r):
    disc(ax, cx - 9, y, 4, r, label=a); disc(ax, cx + 9, y, 4, r, label=b); arrow(ax, (cx - 4.6, y), (cx + 4.6, y), 'fixe')
for y, a in [(52, '1'), (36, '2')]: pair(24, y, a, a, 'limite')
pair(64, 52, '2', '3', 'resultat'); pair(64, 36, '3', '2', 'resultat')
text(ax, 24, 22, 'égal à lui-même', 'limite', 's'); text(ax, 64, 22, 'inverse différent', 'resultat', 's')
text(ax, 24, 13, r'$d^2=1$', 'limite', 'l'); text(ax, 64, 13, r'$d^2\neq 1$', 'resultat', 'l')
save(fig, '73-170')
