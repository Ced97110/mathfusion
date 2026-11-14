import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
L = [(0, 0), (2, 0), (2, 0.7), (0.7, 0.7), (0.7, 2), (0, 2)]
u = 6
def draw(cx, cy, f, role):
    poly(ax, [(cx + f(x, y)[0]*u, cy + f(x, y)[1]*u) for x, y in L], role)
    disc(ax, cx, cy, 0.8, 'encre')
draw(6, 34, lambda x, y: (x, y), 'fixe')
draw(48, 34, lambda x, y: (-y, x), 'resultat')
draw(62, 34, lambda x, y: (x, -y), 'limite')
text(ax, 12, 17, 'départ', 'fixe', 's')
text(ax, 42, 17, 'quart de tour', 'resultat', 's')
text(ax, 69, 17, 'miroir horizontal', 'limite', 's')
text(ax, 42, 12.5, r'$\det=1$', 'resultat', 's')
text(ax, 69, 12.5, r'$\det=-1$', 'limite', 's')
text(ax, 42, 6, r'dans $SO(2)$', 'resultat', 's')
text(ax, 69, 6, r'pas dans $SO(2)$', 'limite', 's')
save(fig, '74-094')
