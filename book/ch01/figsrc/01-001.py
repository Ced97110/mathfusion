import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(16, 'sujet'), (45, 'autre'), (74, 'autre')]
for (x, r), s in zip(cols, ['combien ?', 'quelle place ?', 'quel nom ?']):
    text(ax, x, 65, s, r, 'm')
# 14 boîtes, 2 rangées de 7
for row, y in enumerate([36, 39.6]):
    for i in range(7):
        box(ax, 3.4 + 3.6 * i, y, 3, 3, 'sujet', r=0.3, lw=0.6)
brace(ax, 3.4, 28, 35, 'sujet', label='14')
# 14 lignes de la liste
for k in range(1, 15):
    y = 58 - 2 * (k - 1)
    box(ax, 33, y, 17, 1.4, 'autre' if k == 14 else 'fixe', r=0.3, lw=0.6)
text(ax, 54, 32.7, '14e', 'autre', 's')
box(ax, 63, 38, 22, 14, 'autre', label='bus 14', size='l')
for (x, r), s in zip(cols, ['quantité', 'rang', 'étiquette']):
    text(ax, x, 20, s, r, 'm')
text(ax, 16, 13, '= un nombre', 'resultat', 's')
text(ax, 45, 13, 'pas une quantité', 'autre', 's')
text(ax, 74, 13, 'pas une quantité', 'autre', 's')
save(fig, '01-001')
