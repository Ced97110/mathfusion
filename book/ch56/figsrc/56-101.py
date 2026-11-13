import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
ideals = [48, 24, 12, 6, 3, 3, 3]
pts = [2, 3, 5, 9, 17, 17, 17]
xs = [12 + 11 * i for i in range(7)]
yb = 18
line(ax, [(4, yb), (84, yb)], 'fixe', lw=0.6)
for i, (x, d, n) in enumerate(zip(xs, ideals, pts)):
    ax.add_patch(Rectangle((x - 4, yb), 8, n * 0.65, ec=COL['varie' if i < 4 else 'resultat'],
                           fc=FILL['varie' if i < 4 else 'resultat'], lw=0.8, zorder=2))
    text(ax, x, yb - 3.5, f'({d})', 'sujet', 's')
top = yb + 17 * 0.65
line(ax, [(xs[4], top), (xs[6] + 6, top)], 'resultat', lw=0.7, dash=True)
text(ax, xs[4], top + 3.5, r'$N$', 'resultat', 's')
text(ax, 70, top + 7.5, 'plus de changement', 'resultat', 's')
text(ax, 26, 40, "chaque idéal s'agrandit", 'varie', 's')
text(ax, 44, 52, r'$I_1 \subseteq I_2 \subseteq I_3 \subseteq \cdots$ devient constante', 'encre', 'm')
save(fig, '56-101')
