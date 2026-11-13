import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 7; gx = 12; gy = 8
for i in range(5):
    for j in range(4):
        box(ax, gx + j * u, gy + i * u, u, u, 'varie' if i == 4 else 'sujet', lw=0.5, r=0.1)
brace(ax, gx, gx + 4 * u, gy + 5 * u, 'fixe', label='4', down=False)
arrow(ax, (7, gy), (7, gy + 5 * u), 'fixe', both=True); text(ax, 4, gy + 2.5 * u, '5', 'encre', 'm')
text(ax, 64, 38, '1 rangée = 4 carrés', 'varie', 's'); arrow(ax, (50, 38), (gx + 4 * u + 1, gy + 4.5 * u), 'varie')
text(ax, 64, 26, '5 rangées', 'sujet', 's')
text(ax, 64, 14, r'$4 \times 5 = 20$ carrés', 'resultat', 'm')
save(fig, '10-058')
