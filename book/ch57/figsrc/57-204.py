import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def grid(ox, oy, s=7.0):
    pts = []
    for x in range(4):
        for y in range(3):
            pts.append((ox + x * s, oy + y * s))
    return pts
L = grid(8, 20)
for i, (px, py) in enumerate(L):
    if i == 0: disc(ax, px, py, 2.2, 'sujet')
    else: disc(ax, px, py, 1.2, 'fixe', fill=False)
text(ax, 18, 52, 'sous-module {(0 ; 0)}', 'sujet', 's')
text(ax, 18, 7, r'le plus petit dans $\mathbb{Z}^2$', 'sujet', 's')
R = grid(54, 20)
box(ax, 48, 14, 34, 33, 'resultat', dash=True, fill=False)
for px, py in R: disc(ax, px, py, 1.6, 'resultat')
text(ax, 65, 52, r'$\mathbb{Z}^2/\mathbb{Z}^2=0$', 'resultat', 's')
text(ax, 65, 7, 'une seule classe', 'resultat', 's')
save(fig, '57-204')
