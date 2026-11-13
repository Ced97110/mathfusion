import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
s = 10.0                      # mm par unité sur l'axe des a
r3 = math.sqrt(3)
ox, oy = 44.0, 33.0
P = lambda a, b: (ox + a * s, oy + b * r3 * s)
arrow(ax, (ox - 35, oy), (ox + 38, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 24), (ox, oy + 26), 'fixe', lw=0.7)
special = {(1, 1), (1, -1), (0, 1), (-3, 0)}
for a in range(-3, 4):
    for b in range(-1, 2):
        if (a, b) in special:
            continue
        x, y = P(a, b)
        disc(ax, x, y, 1.1, 'sujet')
x1, y1 = P(1, 1)
x2, y2 = P(1, -1)
xi, yi = P(0, 1)
xm, ym = P(-3, 0)
disc(ax, x1, y1, 1.8, 'varie'); disc(ax, x2, y2, 1.8, 'varie')
disc(ax, xi, yi, 1.8, 'resultat'); disc(ax, xm, ym, 1.8, 'resultat')
line(ax, [(x1, oy), (x1, y1)], 'fixe', dash=True)
arrow(ax, (xi - 1.5, yi + 1.2), (xm + 0.5, ym + 2.2), 'resultat', curve=0.35)
text(ax, x1 + 2.2, y1 + 3.2, r'$1+\sqrt{3}\,i$', 'varie', 's', ha='left')
text(ax, x2 + 2.2, y2 - 3.2, r'$1-\sqrt{3}\,i$', 'varie', 's', ha='left')
text(ax, xi + 2.5, yi + 3.2, r'$\sqrt{3}\,i$', 'resultat', 's', ha='left')
text(ax, xm, ym - 4, '−3', 'resultat', 's')
text(ax, 32, 42, r'$(\sqrt{3}\,i)^2=-3$', 'resultat', 's')
text(ax, x1 + 1, oy - 4, 'a = 1', 'fixe', 's', ha='left')
text(ax, ox - 2, oy - 4, '0', 'fixe', 's', ha='right')
text(ax, 44, 67, 'points $a+b\\sqrt{3}\\,i$, a et b entiers', 'sujet', 's')
save(fig, '56-050')
