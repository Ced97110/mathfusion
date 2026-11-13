import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
text(ax, 44, 63, r'$ed=1+k\,\varphi(n)$', 'sujet', 'l')
u = 84 / 81
y, h = 34, 9
ax.add_patch(Rectangle((2, y), u, h, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
for j in range(2):
    x = 2 + u + 40 * u * j
    ax.add_patch(Rectangle((x, y), 40 * u, h, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    text(ax, x + 20 * u, y + h / 2, '40', 'sujet', 'm')
text(ax, 14, 50, 'retirer 1', 'varie', 's')
arrow(ax, (10, 48), (2.6, y + h + 0.6), 'varie')
brace(ax, 2 + u, 86, y + h, 'sujet', label='80 ÷ 40 : k = 2 blocs', down=False)
brace(ax, 2, 86, y, 'fixe', label='e × d = 3 × 27 = 81')
text(ax, 44, 14, '487 × 191 = 1 + 151 × 616', 'encre', 's')
save(fig, '53-137')
