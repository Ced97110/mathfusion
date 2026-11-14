import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
dims = [1, 2, 4, 8, 16]
for i, d in enumerate(dims):
    y = 6 + 13 * i
    w = 4 * d
    role = 'fixe' if i == 0 else ('resultat' if i == 4 else 'sujet')
    box(ax, 44 - w / 2, y, w, 7, role, label=str(d), size='m')
    if i < 4:
        arrow(ax, (44, y + 7.5), (44, y + 12.5), 'varie')
        text(ax, 49, y + 10, '×2', 'varie', 's')
text(ax, 44, 76, 'φ(17) = 16 = 2⁴', 'encre', 'l')
text(ax, 44, 71, '4 étages : 4 racines carrées', 'sujet', 's')
save(fig, '66-102')
