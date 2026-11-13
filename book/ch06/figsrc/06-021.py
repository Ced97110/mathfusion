import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, roles):
    pw = w / len(roles)
    for i, r in enumerate(roles):
        ax.add_patch(Rectangle((x + i * pw, y), pw, h, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))

fig, ax = canvas(62)
text(ax, 44, 57, 'même haut : 3 parts prises', 'encre', 'm')
for y, n, res in [(34, 4, '15 cm'), (12, 5, '12 cm')]:
    bar(ax, 20, y, 52, 10, ['sujet'] * 3 + ['fixe'] * (n - 3))
    text(ax, 10, y + 8.5, '3', 'sujet', 'l'); line(ax, [(6, y + 5), (14, y + 5)], 'encre'); text(ax, 10, y + 1.5, str(n), 'varie', 'l')
    text(ax, 80, y + 5, res, 'resultat', 'm')
text(ax, 44, 4, 'le bas change la taille', 'varie', 's')
save(fig, '06-021')
