import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for y, m in [(66, 3), (48, 4), (30, 5)]:
    text(ax, 2, y, f'par {m}', 'encre', 'm', ha='left')
    for i in range(7):
        x = 22 + i * 6.4 + (i // m) * 3
        box(ax, x, y - 3, 6, 6, 'sujet' if i < (7 // m) * m else 'varie')
    text(ax, 75, y, f'reste {7 % m}', 'varie', 's', ha='left')
box(ax, 12, 8, 64, 10, 'resultat', label='liste de 7 : (1, 3, 2)')
save(fig, '52-249')
