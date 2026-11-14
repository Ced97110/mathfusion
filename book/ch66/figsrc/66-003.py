import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(58)
cy, r = 33, 12
for cx, n, name, sub, ok in [(15, 5, 'pentagone', 'se construit', True),
                              (44, 7, 'heptagone', 'personne n\'a réussi', False),
                              (73, 9, 'ennéagone', 'personne n\'a réussi', False)]:
    disc(ax, cx, cy, r, 'fixe', fill=False)
    pts = [P(cx, cy, r, 90 + 360 * i / n) for i in range(n)]
    if ok: poly(ax, pts, 'resultat')
    else: line(ax, pts + [pts[0]], 'fixe', dash=True)
    for p in pts: disc(ax, p[0], p[1], 1.2, 'resultat' if ok else 'varie')
    text(ax, cx, cy + r + 4, r'$n=%d$' % n, 'varie')
    text(ax, cx, cy - r - 6, name + ' :\n' + sub, 'resultat' if ok else 'fixe', 's')
save(fig, '66-003')
