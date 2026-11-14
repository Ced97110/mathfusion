import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
P = {'t': (40, 54, 'resultat', '6'), 'l': (20, 34, 'sujet', '3'), 'r': (60, 34, 'autre', '2'), 'b': (40, 14, 'fixe', '1')}
for p, q in (((34, 54), (20, 38.5)), ((46, 54), (60, 38.5)), ((20, 29.5), (34, 14)), ((60, 29.5), (46, 14))):
    line(ax, [p, q], 'fixe')
for k, (x, y, r, n) in P.items():
    box(ax, x - 8, y - 4.5, 16, 9, r, label=n, size='l', weight='bold')
text(ax, 67, 54, 'engendré par les deux', 'resultat', 's', ha='left') if False else text(ax, 66, 54, 'engendré par les deux', 'resultat', 's')
text(ax, 20, 24, 'multiples de 4', 'sujet', 's')
text(ax, 60, 24, 'multiples de 6', 'autre', 's')
text(ax, 66, 14, 'partie commune', 'fixe', 's')
text(ax, 44, 4, 'nombre d\'éléments dans chaque case', 'fixe', 's') if False else None
save(fig, '48-202')
