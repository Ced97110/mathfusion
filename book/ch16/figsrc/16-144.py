import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role="fixe", label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(66)
s = 26
P = lambda x0, u, v: (x0 + u * s, 30 + v * s)
specs = [(3, 'x + y = 5\nx − y = 1', 'une solution', 'resultat'), (31, 'x + y = 5\nx + y = 6', 'aucune', 'limite'),
         (59, 'x + y = 5\n2(x + y) = 10', 'infinité', 'resultat')]
for k, (x0, eq, out, r) in enumerate(specs):
    box(ax, x0, 30, s, s, 'fixe', fill=False)
    if k == 0:
        line(ax, [P(x0, .05, .95), P(x0, .95, .05)], 'sujet', lw=1.6); line(ax, [P(x0, .1, .05), P(x0, .95, .9)], 'varie', lw=1.6)
        disc(ax, *P(x0, .525, .475), 1.2, 'resultat')
    elif k == 1:
        line(ax, [P(x0, .05, .95), P(x0, .85, .15)], 'sujet', lw=1.6); line(ax, [P(x0, .2, .95), P(x0, .95, .2)], 'varie', lw=1.6)
    else:
        line(ax, [P(x0, .1, .9), P(x0, .9, .1)], 'sujet', lw=3.2); line(ax, [P(x0, .1, .9), P(x0, .9, .1)], 'varie', lw=1.0)
    text(ax, x0 + s / 2, 20, eq, 'fixe', 's'); text(ax, x0 + s / 2, 7, out, r, 'm', weight='bold')
text(ax, 22, 61, '(3 ; 2)', 'resultat', 's') if False else None
save(fig, '16-144')
