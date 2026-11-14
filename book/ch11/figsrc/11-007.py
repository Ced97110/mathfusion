import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
c = 7.0; gx, gy = 3, 18
for i in range(5):
    for j in range(3):
        ax.add_patch(Rectangle((gx + i * c, gy + j * c), c, c, ec=COL['sujet'], fc=FILL['sujet'], lw=0.5, zorder=2))
ax.add_patch(Rectangle((gx, gy), 2 * c, 2 * c, ec=COL['varie'], fc='none', lw=1.8, zorder=3))
text(ax, gx + 2.5 * c, 12, '5 sur 3 : 15 carreaux de 1 cm', 'sujet', 's')
bx = 56
for i in range(2):
    for j in range(2):
        ax.add_patch(Rectangle((bx + i * c, 29 + j * c), c, c, ec=COL['sujet'], fc=FILL['varie'], lw=0.5, zorder=2))
ax.add_patch(Rectangle((bx, 29), 2 * c, 2 * c, ec=COL['varie'], fc='none', lw=1.8, zorder=3))
text(ax, bx + c, 47, '1 carré de 2 cm', 'varie', 's')
text(ax, bx + c, 25, '= 4 carreaux', 'varie', 's')
box(ax, 8, 1.5, 72, 6, 'resultat', label='15 ÷ 4 = 3,75 carrés de 2 cm', size='s')
save(fig, '11-007')
