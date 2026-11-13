import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(64)
text(ax, 22, 59, 'côté gauche', 'sujet', 's'); text(ax, 66, 59, 'côté droit', 'varie', 's')
s = 26
def P(x0, u, v): return (x0 + u * s, 24 + v * s)
for k, x0 in enumerate([3, 31, 59]):
    box(ax, x0, 24, s, s, 'fixe', fill=False)
    if k == 0:
        line(ax, [P(x0, .05, .95), P(x0, .95, .05)], 'sujet', lw=1.6)
        line(ax, [P(x0, .1, .05), P(x0, .95, .9)], 'varie', lw=1.6)
        disc(ax, *P(x0, .525, .475), 1.2, 'resultat')
        text(ax, x0 + .525 * s + 4, 24 + .475 * s + 3, '$S$', 'resultat', 's')
    elif k == 1:
        line(ax, [P(x0, .05, .95), P(x0, .85, .15)], 'sujet', lw=1.6)
        line(ax, [P(x0, .2, .95), P(x0, .95, .2)], 'varie', lw=1.6)
    else:
        line(ax, [P(x0, .1, .9), P(x0, .9, .1)], 'sujet', lw=3.2)
        line(ax, [P(x0, .1, .9), P(x0, .9, .1)], 'varie', lw=1.0)
for x0, t, c, r in [(3, 'une solution', 'se croisent', 'resultat'), (31, 'aucune', 'écart constant', 'limite'), (59, 'toutes', "l'une sur l'autre", 'resultat')]:
    text(ax, x0 + s / 2, 16, t, r, 'm', weight='bold'); text(ax, x0 + s / 2, 8, c, 'fixe', 's')
save(fig, '16-131')
