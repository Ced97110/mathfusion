import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
x0, dx = 28, 9.4
# ligne 1 : horloge à 12 heures, un sous-groupe par diviseur
y = 50
text(ax, 44, y + 17, 'horloge à 12 heures : 6 et 6', 'resultat', 's')
for i, d in enumerate([1, 2, 3, 4, 6, 12]):
    box(ax, x0 + dx * i, y + 6, 7.6, 7, 'sujet', label=str(d), size='s', r=0.6)
    box(ax, x0 + dx * i, y - 6, 7.6, 7, 'resultat', r=0.6)
    line(ax, [(x0 + dx * i + 3.8, y + 6), (x0 + dx * i + 3.8, y + 1)], 'fixe')
# ligne 2 : mélanges de 3 cartes, sous-groupes d'ordres 1, 2, 2, 2, 3, 6
y = 12
text(ax, 44, y + 17, 'mélanges de 3 cartes : 4 et 6', 'limite', 's')
divs = {0: 1, 2: 2, 4: 3, 5: 6}
for i, d in divs.items():
    box(ax, x0 + dx * i, y + 6, 7.6, 7, 'sujet', label=str(d), size='s', r=0.6)
orders = [1, 2, 2, 2, 3, 6]
link = {0: [0], 2: [1, 2, 3], 4: [4], 5: [5]}
for i, js in link.items():
    for j in js:
        line(ax, [(x0 + dx * i + 3.8, y + 6), (x0 + dx * j + 3.8, y + 1)], 'fixe')
for j, o in enumerate(orders):
    role = 'limite' if j in (1, 3) else 'resultat'
    box(ax, x0 + dx * j, y - 6, 7.6, 7, role, label=('2' if o == 2 else None), size='s', r=0.6)
text(ax, 14, 50 + 9.5, 'diviseurs', 'sujet', 's')
text(ax, 14, 50 - 2.5, 'sous-groupes', 'fixe', 's')
save(fig, '46-262')
