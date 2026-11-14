import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
xm = 44  # axe de symétrie commun
s, t = (-1 + math.sqrt(5)) / 2, (-1 - math.sqrt(5)) / 2
r5 = math.sqrt(5)
# ligne du haut : s et t, symétriques autour de -1/2 (échelle 24 mm par unité)
y1, y2 = 62, 22
def X1(v): return xm + 24 * (v + 0.5)
def X2(u): return xm + 12 * u
arrow(ax, (4, y1), (84, y1), 'fixe', lw=0.7)
arrow(ax, (4, y2), (84, y2), 'fixe', lw=0.7)
line(ax, [(xm, y2 - 6), (xm, y1 + 8)], 'fixe', dash=True)
disc(ax, X1(s), y1, 1.8, 'sujet'); disc(ax, X1(t), y1, 1.8, 'autre')
disc(ax, X2(r5), y2, 1.8, 'sujet'); disc(ax, X2(-r5), y2, 1.8, 'autre')
text(ax, X1(s), y1 + 5, r'$s$', 'sujet', 'l'); text(ax, X1(t), y1 + 5, r'$t$', 'autre', 'l')
text(ax, X2(r5), y2 - 5, r'$\sqrt{5}$', 'sujet', 'm'); text(ax, X2(-r5), y2 - 5, r'$-\sqrt{5}$', 'autre', 'm')
arrow(ax, (X1(s) - 3, y1 - 3), (X1(t) + 3, y1 - 3), 'varie', both=True, curve=0.0)
text(ax, xm, y1 - 7, r'$\sigma_2$', 'varie', 'm')
arrow(ax, (X2(r5) - 3, y2 + 3), (X2(-r5) + 3, y2 + 3), 'varie', both=True)
text(ax, xm, y2 + 7, r'$\sigma_2$', 'varie', 'm')
line(ax, [(X1(s), y1 - 2.5), (X2(r5), y2 + 2.5)], 'fixe', lw=0.6, dash=True)
line(ax, [(X1(t), y1 - 2.5), (X2(-r5), y2 + 2.5)], 'fixe', lw=0.6, dash=True)
text(ax, 80, 42, r'$2s + 1$', 'fixe', 's', ha='right')
text(ax, 44, 78, r'$H$ normal : $G$ commutatif', 'resultat', 'm')
text(ax, 44, 8, r'$\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q}) \cong G/H$ : 2 éléments', 'sujet', 's')
save(fig, '63-172')
