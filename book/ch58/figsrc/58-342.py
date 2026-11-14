import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# le quotient range les stocks en deux classes : poids pair (bleu) ou impair (orange)
ux = 9.0
ox, oy = 10, 14
N = 5
arrow(ax, (ox - 3, oy), (ox + N * ux + 5, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 3), (ox, oy + N * ux + 5), 'fixe', lw=0.7)
for x in range(N + 1):
    for y in range(N + 1):
        px, py = ox + x * ux, oy + y * ux
        if (x, y) in ((1, 0), (0, 1)): continue
        disc(ax, px, py, 1.4, 'sujet' if (x + y) % 2 == 0 else 'varie')
a, b = (ox + 1 * ux, oy), (ox, oy + ux)
disc(ax, a[0], a[1], 2.2, 'varie')
disc(ax, b[0], b[1], 2.2, 'varie')
arrow(ax, (b[0] + 3, b[1] - 1.5), (a[0] - 1.5, a[1] + 3.5), 'resultat', lw=1.4, both=True)
text(ax, a[0] + 5, a[1] + 5.5, r'$(1, 0)$', 'varie', 's', ha='left')
text(ax, b[0] + 4.5, b[1] + 4, r'$(0, 1)$', 'varie', 's', ha='left')
text(ax, 69, 56, 'différence', 'resultat', 's')
text(ax, 69, 51, r'$(1, -1)$ : poids 0', 'resultat', 's')
text(ax, 69, 44, 'même classe', 'resultat', 'm', weight='bold')
disc(ax, 58, 30, 1.8, 'sujet'); text(ax, 62, 30, 'poids pair', 'sujet', 's', ha='left')
disc(ax, 58, 24, 1.8, 'varie'); text(ax, 62, 24, 'poids impair', 'varie', 's', ha='left')
text(ax, 44, 76, 'Quotient : deux classes', 'sujet', 'm', weight='bold')
save(fig, '58-342')
