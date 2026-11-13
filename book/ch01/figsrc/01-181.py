import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 3, 26, 81, 24, 'sujet', fill=False)
for y, s in [(46, 'règle 1'), (38, 'règle 2'), (30, 'règle 3')]:
    text(ax, 16, y, s, 'sujet', 's')
for y in (34, 42):
    line(ax, [(32, y), (84, y)], 'fixe', lw=0.5)
for x in (32, 45, 58, 71, 84):
    line(ax, [(x, 14), (x, 50)], 'fixe', lw=0.5)
cols = [38.5, 51.5, 64.5, 77.5]
for x, s in zip(cols, ['match 1', 'match 2', 'match 3', 'autre jeu']):
    text(ax, x, 54, s, 'encre', 's')
brace(ax, 32, 71, 57, 'resultat', label='vérifient la liste', down=False)
def coche(x, y):
    line(ax, [(x - 2, y), (x - 0.6, y - 1.5), (x + 2, y + 1.5)], 'resultat', lw=1.2)
for x in cols[:3]:
    for y in (46, 38, 30): coche(x, y)
coche(cols[3], 46); coche(cols[3], 30)
text(ax, 16, 18, 'résultat démontré', 'resultat', 's')
for x in (33, 46, 59):
    box(ax, x, 14, 11, 8, 'resultat')
text(ax, 51.5, 7, 'vaut pour chaque match', 'resultat', 's')
line(ax, [(75.5, 36), (79.5, 40)], 'limite', lw=1.2); line(ax, [(75.5, 40), (79.5, 36)], 'limite', lw=1.2)
box(ax, 72, 14, 11, 8, 'limite', fill=False, dash=True, label='?', size='m')
save(fig, '01-181')
