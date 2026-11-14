import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

assert 3 * 4 == 12 and 12 * 26 == 312 and 312 // 26 == 12

def grid(ax, x, y, cols, rows, c, role, hl_row=None, hl_role='varie'):
    for r in range(rows):
        for k in range(cols):
            rr = hl_role if r == hl_row else role
            ax.add_patch(Rectangle((x + k * c, y + (rows - 1 - r) * c), c, c, fc=FILL[rr], ec=COL[rr], lw=0.3, zorder=2))

fig, ax = canvas(100)
grid(ax, 4, 74, 4, 3, 5, 'sujet')
text(ax, 15, 92, '4 décalages', 'sujet', 's')
text(ax, 30, 81.5, r'$3 \times 4 = 12$ clés', 'sujet', 'm', ha='left')
text(ax, 30, 75.5, '3 multiplicateurs', 'fixe', 's', ha='left')
gx, gy, c = 7, 22, 3.0
grid(ax, gx, gy, 26, 12, c, 'sujet', hl_row=4)
text(ax, gx + 13 * c, gy + 12 * c + 3, '26 décalages', 'sujet', 's')
text(ax, 3, gy + 6 * c, '12 multiplicateurs', 'sujet', 's', rot=90)
text(ax, 44, 13, r'$12 \times 26 = 312$ clés', 'resultat', 'l', weight='bold')
text(ax, 44, 5, 'une ligne orange : 26 clés, comme César', 'varie', 's')
save(fig, '53-060')
