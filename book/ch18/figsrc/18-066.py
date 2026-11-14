import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, y0, c = 29, 22, 6
for i in range(5):
    for j in range(4):
        ax.add_patch(Rectangle((x0 + i * c, y0 + j * c), c, c, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
text(ax, 44, 56, r'$c = p \times q$', 'sujet', 'l')
brace(ax, x0, x0 + 5 * c, y0, 'fixe', label=r'$q = 5$')
text(ax, x0 - 6, y0 + 12, r'$p = 4$', 'fixe', 's')
text(ax, 44, 9, r'$4 \times 5 = 20$ carreaux', 'resultat', 'm')
save(fig, '18-066')
