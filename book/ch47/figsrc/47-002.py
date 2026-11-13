import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 59, 'Symétries : la moitié sont des rotations', 'encre', 'm')
box(ax, 8, 48, 6, 4, 'sujet', r=0.3); text(ax, 17, 50, 'rotations', 'sujet', 's', ha='left')
box(ax, 44, 48, 6, 4, 'fixe', r=0.3); text(ax, 53, 50, 'retournements', 'fixe', 's', ha='left')
c = 4.0
for row, (name, n) in enumerate([('triangle', 6), ('carré', 8), ('hexagone', 12)]):
    y = 36 - row * 13
    text(ax, 3, y + 2, name, 'encre', 's', ha='left')
    for i in range(n):
        role = 'sujet' if i < n // 2 else 'fixe'
        box(ax, 20 + i * c, y, c, 4, role, r=0.2, lw=0.6)
    text(ax, 20 + 12 * c + 2, y + 2, f'{n // 2} sur {n}', 'resultat', 's', ha='left')
save(fig, '47-002')
