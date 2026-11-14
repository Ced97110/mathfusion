import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 7; y0 = 22
x = 4
for s in (1, 2, 2):
    ax.add_patch(Rectangle((x, y0), s * u, s * u, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    text(ax, x + s * u / 2, y0 + s * u / 2, f'{s}²', 'sujet', 'm')
    x += s * u + 6
text(ax, 4 + 7 + 3, y0 + 18.5, '+', 'fixe', 'l') if False else None
ax.add_patch(Rectangle((60, y0), 3 * u, 3 * u, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
text(ax, 60 + 10.5, y0 + 10.5, '9', 'resultat', 'l')
text(ax, 56.5, y0 + 10.5, '=', 'fixe', 'l')
text(ax, 60 + 10.5, y0 - 4, 'côté 3', 'resultat', 's')
text(ax, 26, y0 - 4, '1 + 4 + 4 = 9', 'sujet', 's')
text(ax, 44, 48, r'$\|x\| = 3$', 'resultat', 'l')
save(fig, '73-140')
