import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# ligne de départ et raccourci 3 × 4 encadré
text(ax, 19, 84, '2 +', 'encre', 'l')
box(ax, 26, 80, 20, 8, 'varie', label='3 × 4', size='l')
text(ax, 68, 84, 'sans dépli : 14 ou 20', 'limite', 's')
arrow(ax, (36, 80), (36, 63.2), 'varie', lw=1.6)
text(ax, 60, 71.5, 'étape : déplier 3 × 4', 'varie', 's')
# ligne dépliée 2 + 4 + 4 + 4
text(ax, 13, 58, '2 +', 'encre', 'l')
box(ax, 22, 53, 52, 10, 'varie', fill=False)
for x, t in [(30, '4'), (39, '+'), (48, '4'), (57, '+'), (66, '4')]:
    text(ax, x, 58, t, 'varie', 'l')
# 2 pains
for x in (8.5, 13):
    box(ax, x, 40, 3.5, 3.5, 'sujet', r=0.3)
# 3 lots de 4 œufs
for x in (30, 48, 66):
    for y in (48, 44, 40, 36):
        disc(ax, x, y, 1.5, 'varie')
brace(ax, 8, 70, 31, 'fixe', label='une seule opération : +', down=True, size='s')
box(ax, 32, 6, 24, 10, 'resultat', label='= 14', size='l', weight='bold')
save(fig, '04-057')
