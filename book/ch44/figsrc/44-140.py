import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [26, 42, 58, 74]; s = 11
text(ax, 2, 54, 'heures', 'sujet', 's', ha='left'); text(ax, 2, 24, 'rotations', 'autre', 's', ha='left')
labs = ['1', r'$r$', r'$r^2$', r'$r^3$']
for k, x in enumerate(xs):
    disc(ax, x, 54, 4.2, 'sujet', label=str(k))
    a = 90 * k; c = math.cos(math.radians(a)); sn = math.sin(math.radians(a))
    Q = lambda dx, dy: (x + dx * c - dy * sn, 28 + dx * sn + dy * c)
    poly(ax, [Q(-s/2, -s/2), Q(s/2, -s/2), Q(s/2, s/2), Q(-s/2, s/2)], 'autre')
    px, py = Q(-s/2 + 2.2, s/2 - 2.2); disc(ax, px, py, 1.6, 'varie')
    text(ax, x, 15, labs[k], 'autre', 'm')
    arrow(ax, (x, 49), (x, 36), 'fixe', both=True)
    if k < 3:
        arrow(ax, (x + 5, 58), (xs[k + 1] - 5, 58), 'varie', curve=-0.5)
text(ax, 50, 63, '+ 1 heure ↔ ¼ tour', 'varie', 's')
text(ax, 44, 6, r'$3 + 2 = 1$  ↔  $r^3\,r^2 = r$', 'resultat', 'm')
save(fig, '44-140')
