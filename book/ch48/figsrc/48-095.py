import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'sous-groupes de $\mathbb{Z}/6\mathbb{Z}$ : 4', 'sujet', 's', weight='bold')
for j in range(6):
    text(ax, 31 + 10*j, 55, str(j), 'fixe', 's')
for i, d in enumerate([1, 2, 3, 6]):
    y = 42 - i * 11
    text(ax, 12, y + 3.5, f'diviseur {d}', 'autre', 's')
    for j in range(6):
        ok = j % d == 0
        box(ax, 26 + 10*j, y, 10, 7, 'sujet' if ok else 'fixe', fill=ok, lw=0.6, r=0.5)
text(ax, 44, 3, '4 diviseurs de 6 = 4 sous-groupes', 'resultat', 's')
save(fig, '48-095')
