import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(92)
text(ax, 22, 87, 'côté gauche', 'sujet', 's'); text(ax, 66, 87, 'côté droit', 'varie', 's')
a, b = (10, 56), (78, 76)
line(ax, [a, b], 'sujet', lw=3.2); line(ax, [a, b], 'varie', lw=1.0)
for u, t in [(.28, 'solution 2'), (.72, 'solution 5')]:
    p = (a[0] + u * 68, a[1] + u * 20); disc(ax, *p, 1.6, 'resultat'); text(ax, p[0], p[1] - 5, t, 'resultat', 's')
text(ax, 44, 46, 'deux points, une droite', 'encre', 'm')
text(ax, 44, 36, 'seules issues possibles', 'fixe', 's')
for i, (t, r) in enumerate([('une', 'resultat'), ('aucune', 'resultat'), ('toutes', 'resultat'), ('deux', 'limite')]):
    box(ax, 3 + i * 21.5, 18, 19, 12, r, t, 's', dash=(r == 'limite'))
text(ax, 3 + 3 * 21.5 + 9.5, 11, 'impossible', 'limite', 's')
save(fig, '16-135')
