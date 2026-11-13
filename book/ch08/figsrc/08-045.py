import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
w = 6.4; x0 = 12
for d in range(10):
    r = 'fixe' if d < 5 else 'resultat'
    ax.add_patch(Rectangle((x0 + d * w, 22), w, 9, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))
    text(ax, x0 + d * w + w / 2, 26.5, str(d), r, 'm')
text(ax, 44, 46, 'chiffre suivant', 'encre', 's')
line(ax, [(x0 + 5 * w, 20), (x0 + 5 * w, 36)], 'varie', lw=1.4, dash=True)
text(ax, x0 + 5 * w, 39, 'milieu 32,115', 'varie', 's')
brace(ax, x0 + 0.3, x0 + 5 * w - 0.3, 21, 'fixe', '0 à 4 : vers 32,11')
brace(ax, x0 + 5 * w + 0.3, x0 + 10 * w - 0.3, 21, 'resultat', '5 à 9 : vers 32,12')
save(fig, '08-045')
