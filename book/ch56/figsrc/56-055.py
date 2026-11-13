import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
s = 18.0
r3 = math.sqrt(3)
ox, oy = 44.0, 52.0
P = lambda a, b: (ox + a * s, oy + b * r3 * s)
arrow(ax, (ox - 38, oy), (ox + 40, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 36), (ox, oy + 38), 'fixe', lw=0.6)
line(ax, [(ox + s * math.cos(a), oy + s * math.sin(a)) for a in [i * math.pi / 30 for i in range(61)]], 'resultat', lw=0.8, dash=True)
for a in range(-2, 3):
    for b in range(-1, 2):
        x, y = P(a, b)
        if (a, b) in ((1, 0), (-1, 0)):
            disc(ax, x, y, 2.0, 'resultat')
        elif (a, b) == (0, 0):
            disc(ax, x, y, 1.0, 'fixe')
        else:
            disc(ax, x, y, 1.0, 'fixe')
x, y = P(0.5, 0.5)
disc(ax, x, y, 2.0, 'limite', fill=False)
text(ax, P(1, 0)[0] + 2.5, oy + 3.5, '1', 'resultat', 's', ha='left')
text(ax, P(-1, 0)[0] - 2.5, oy + 3.5, '−1', 'resultat', 's', ha='right')
text(ax, x + 3, y + 5, r'$\frac{1}{2}+\frac{1}{2}\sqrt{3}\,i$', 'limite', 's', ha='left')
text(ax, 43, 95, 'cercle : norme 1', 'resultat', 's', ha='right')
text(ax, 2, 4, 'points entiers : seuls 1 et −1', 'resultat', 's', ha='left')
text(ax, 2, 9.5, 'norme 1 mais coefficients non entiers', 'limite', 's', ha='left')
save(fig, '56-055')
