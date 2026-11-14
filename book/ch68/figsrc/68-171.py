import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
c, x0, y0 = 5.2, 16, 12
for i in range(8):
    for k in range(4):
        ax.add_patch(Rectangle((x0 + k * c, y0 + i * c), c, c, ec=COL['sujet'], fc=FILL['sujet'], lw=0.7, zorder=2))
brace(ax, x0, x0 + 4 * c, y0 + 8 * c + 1, 'fixe', label='4 mots', down=False)
arrow(ax, (10, y0), (10, y0 + 8 * c), 'fixe', both=True)
text(ax, 5, y0 + 4 * c, '8 lignes', 'fixe', 's', rot=90)
text(ax, 64, 42, r'$8 \times 4 = 32$ cases', 'encre', 'm')
text(ax, 64, 34, r'$2^5 = 32$ mots de 5 bits', 'resultat', 'm')
text(ax, 64, 26, 'chaque mot : une case', 'resultat', 's')
save(fig, '68-171')
