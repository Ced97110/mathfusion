import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 4, 60, 80, 10, 'resultat', label='plan, dimension 2 : 3 vecteurs liés', size='s')
text(ax, 44, 54, 'sans dimension donnée :', 'limite', 's')
x0, y0, W_, H_ = 12, 12, 40, 30
sc = H_ / 1.3
arrow(ax, (x0, y0), (x0 + W_ + 4, y0), 'fixe', lw=0.8)
arrow(ax, (x0, y0), (x0, y0 + H_ + 8), 'fixe', lw=0.8)
ts = [i / 20 for i in range(21)]
line(ax, [(x0 + t * W_, y0 + 1.0 * sc) for t in ts], 'sujet', lw=1.4)
line(ax, [(x0 + t * W_, y0 + t * sc) for t in ts], 'varie', lw=1.4)
line(ax, [(x0 + t * W_, y0 + t * t * sc) for t in ts], 'autre', lw=1.4)
text(ax, x0 + 9, y0 + sc + 3.3, '1', 'sujet', 's')
text(ax, x0 + 0.45 * W_ - 3, y0 + 0.45 * sc + 4, '$x$', 'varie', 's')
text(ax, x0 + 0.85 * W_ + 3.5, y0 + 0.7225 * sc - 4, '$x^2$', 'autre', 's')
text(ax, x0 + W_ + 6, y0 - 0.5, '$x$', 'fixe', 's')
text(ax, 70, 46, 'fonctions continues', 'fixe', 's')
text(ax, 70, 38, '1, x, x² : indépendantes', 'sujet', 's')
text(ax, 70, 31, 'puis x³, x⁴, … sans fin', 'autre', 's')
text(ax, 70, 22, 'aucune borne n', 'limite', 'm')
save(fig, '58-290')
