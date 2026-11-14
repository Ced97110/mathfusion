import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 4.6
def panel(cx, cy, vecs, labels):
    line(ax, [(cx - 3.4 * s, cy), (cx + 3.4 * s, cy)], 'fixe', lw=0.5)
    line(ax, [(cx, cy - 3.4 * s), (cx, cy + 3.4 * s)], 'fixe', lw=0.5)
    pts = [(cx + a * s, cy + b * s) for a, b in vecs]
    (pu, pv, pw) = pts
    line(ax, [pu, pw], 'fixe', dash=True); line(ax, [pv, pw], 'fixe', dash=True)
    for p, r in zip(pts, ['sujet', 'autre', 'resultat']):
        arrow(ax, (cx, cy), p, r, lw=1.3)
    for (x, y, t, r, ha) in labels:
        text(ax, x, y, t, r, 's', ha=ha)
text(ax, 22, 66, 'départ', 'encre', 'l', weight='bold'); text(ax, 66, 66, 'arrivée', 'encre', 'l', weight='bold')
panel(22, 34, [(2, 1), (-1, 2), (1, 3)],
      [(33.5, 38.5, r'$(2\,;\,1)$', 'sujet', 'left'), (16.5, 45.5, r'$(-1\,;\,2)$', 'autre', 'right'),
       (27.5, 52, r'$(1\,;\,3)$', 'resultat', 'left')])
panel(66, 34, [(-1, 2), (-2, -1), (-3, 1)],
      [(67, 45.5, r'$(-1\,;\,2)$', 'sujet', 'left'), (58, 27, r'$(-2\,;\,-1)$', 'autre', 'right'),
       (52, 41, r'$(-3\,;\,1)$', 'resultat', 'left')])
arrow(ax, (38.5, 34), (49.5, 34), 'varie', lw=1.3)
text(ax, 44, 56, 'quart de tour', 'varie', 's')
text(ax, 44, 8, 'la somme est envoyée sur la somme', 'resultat', 's')
save(fig, '57-151')
