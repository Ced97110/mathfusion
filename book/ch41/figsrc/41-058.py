import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
xs = [2, 31, 60]
w = 26
heads = [('nombre 0', 'scalaire', 'autre'), ('vecteur nul', 'norme 0', 'sujet'), (r'vecteur $\langle 3;\ 4\rangle$', 'norme 5', 'autre')]
for x, (h1, h2, role) in zip(xs, heads):
    box(ax, x, 6, w, 38, role, fill=False, lw=0.8)
    text(ax, x + w / 2, 52, h1, role, 's')
    text(ax, x + w / 2, 10, h2, role, 's')
# 1 : le nombre 0, une seule valeur, pas de flèche
text(ax, xs[0] + w / 2, 27, '0', 'autre', 'xl', weight='bold')
# 2 : le vecteur nul, un point sans direction
c2 = (xs[1] + w / 2, 27)
line(ax, [(c2[0] - 10, c2[1]), (c2[0] + 10, c2[1])], 'fixe', lw=0.5)
line(ax, [(c2[0], c2[1] - 12), (c2[0], c2[1] + 12)], 'fixe', lw=0.5)
disc(ax, c2[0], c2[1], 1.3, 'sujet')
# 3 : un vecteur non nul, une flèche
c3 = (xs[2] + 5, 15)
k = 2.6
line(ax, [c3, (c3[0] + 20, c3[1])], 'fixe', lw=0.5)
line(ax, [c3, (c3[0], c3[1] + 26)], 'fixe', lw=0.5)
arrow(ax, c3, (c3[0] + 3 * k, c3[1] + 4 * k), 'autre', lw=1.8)
save(fig, '41-058')
