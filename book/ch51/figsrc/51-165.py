import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def mat(x, y, w, h, rows, role, dash=False):
    box(ax, x, y, w, h, role, dash=dash)
    for r, s in enumerate(rows):
        text(ax, x + w / 2, y + h * (0.7 - 0.4 * r), s, role, 'm')
mat(30, 54, 28, 14, ['2  0', '0  1'], 'sujet')
text(ax, 62, 61, r'$\det = 2$', 'sujet', 's', ha='left')
box(ax, 2, 4, 40, 40, 'limite', fill=False)
box(ax, 46, 4, 40, 40, 'resultat', fill=False)
text(ax, 22, 39, 'parmi les entiers', 'limite', 's')
text(ax, 66, 39, 'parmi les réels', 'resultat', 's')
arrow(ax, (36, 54), (22, 45), 'varie')
arrow(ax, (52, 54), (66, 45), 'varie')
mat(12, 16, 20, 14, ['½  0', '0  1'], 'limite', dash=True)
mat(56, 16, 20, 14, ['½  0', '0  1'], 'resultat')
text(ax, 22, 9, "½ n'est pas entier", 'limite', 's')
text(ax, 66, 9, 'inverse : 2 est inversible', 'resultat', 's')
save(fig, '51-165')
