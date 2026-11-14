import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(63)
c = 9.0
def grid(x0, y0, n, role, fillrole):
    for i in range(n):
        for j in range(n):
            ax.add_patch(Rectangle((x0 + i*c, y0 + j*c), c, c, ec=COL[role], fc=FILL[fillrole], lw=0.8, zorder=2))
grid(4, 18, 3, 'fixe', 'fixe')
grid(42, 18, 4, 'sujet', 'sujet')
text(ax, 4 + 13.5, 14, '3 × 3 = 9', 'fixe', 'm')
text(ax, 4 + 13.5, 9, 'trop petit', 'fixe', 's')
text(ax, 42 + 18, 14, '4 × 4 = 16', 'resultat', 'm', weight='bold')
text(ax, 42 + 18, 9, 'exact : côté 4 m', 'resultat', 's')
text(ax, 42 + 18, 18 + 36 + 3.5, '16 m²', 'sujet', 'm')
text(ax, 42 + 18 + 22, 18 + 18, '4', 'sujet', 'm')
save(fig, '22-001')
