import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
s = 7; x0 = 19.5; y0 = 20
for i in range(7):
    for j in range(3):
        box(ax, x0 + i * s, y0 + j * s, s, s, 'fixe', lw=0.4, r=0.1)
ax.add_patch(Rectangle((x0, y0), 7 * s, 3 * s, ec=COL['sujet'], fc='none', lw=2.6, zorder=4))
text(ax, x0 + 3.5 * s, y0 + 3 * s + 3.5, '7 m', 'sujet', 'm')
text(ax, x0 + 3.5 * s, y0 - 3.5, '7 m', 'sujet', 'm')
text(ax, x0 - 5, y0 + 1.5 * s, '3 m', 'sujet', 'm')
text(ax, x0 + 7 * s + 5, y0 + 1.5 * s, '3 m', 'sujet', 'm')
text(ax, 44, 63, 'clôture : le tour', 'sujet', 'l')
text(ax, 44, 11, '3 + 7 + 3 + 7 = 20 m', 'sujet', 'l')
text(ax, 44, 4, "dedans : 21 carrés (l'aire)", 'fixe', 's')
save(fig, '16-003')
