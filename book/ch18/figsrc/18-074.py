import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c = 5
text(ax, 14.5, 61, r'$a=1$', 'sujet', 'l')
text(ax, 60, 61, r'$a=20$', 'varie', 'l')
ax.add_patch(Rectangle((12, 36), c, c, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
text(ax, 14.5, 45, r'$x^2$', 'sujet', 's')
text(ax, 14.5, 32, r'$x$', 'sujet', 's')
x0, y0 = 38, 26
for i in range(5):
    for j in range(4):
        ax.add_patch(Rectangle((x0 + i * c, y0 + j * c), c, c, ec=COL['varie'], fc=FILL['varie'], lw=0.6, zorder=2))
text(ax, 62, 52, r'$20x^2$', 'resultat', 'm')
brace(ax, x0, x0 + 5 * c, y0, 'fixe', label=r'$5x$')
text(ax, x0 - 4.5, y0 + 10, r'$4x$', 'fixe', 's')
save(fig, '18-074')
