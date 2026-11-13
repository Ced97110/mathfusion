import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 54, 61, 'horloge à 3', 'sujet', 'm')
text(ax, 15, 61, 'horloge à 2', 'autre', 'm') if False else None
cx = [34, 52, 70]; ry = [38, 20]
for j, x in enumerate(cx):
    disc(ax, x, 53, 3.6, 'sujet', label=str(j), size='s')
text(ax, 14, 46, 'horloge à 2', 'autre', 's')
for i, y in enumerate(ry):
    disc(ax, 14, y, 3.6, 'autre', label=str(i), size='s')
    for j, x in enumerate(cx):
        box(ax, x - 8, y - 6, 16, 12, 'resultat', label=f'({j} ; {i})', size='s')
text(ax, 44, 6, r'$2 \times 3 = 6$ paires', 'resultat', 'm')
save(fig, '48-199')
