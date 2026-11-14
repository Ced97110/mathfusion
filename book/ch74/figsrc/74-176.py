import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def pent(cx, cy, r, role, fill=True):
    pts = [(cx + r*math.cos(math.radians(90+72*i)), cy + r*math.sin(math.radians(90+72*i))) for i in range(5)]
    poly(ax, pts, role, fill=fill, lw=1.0); return pts
def grid(cx, cy, role='fixe'):
    for i in range(-2, 3):
        line(ax, [(cx-12, cy+i*6), (cx+12, cy+i*6)], role, lw=0.5)
        line(ax, [(cx+i*6, cy-12), (cx+i*6, cy+12)], role, lw=0.5)
cy = 34
pts = pent(15, cy, 10, 'resultat')
for p in pts: line(ax, [(15, cy), (15 + 1.25*(p[0]-15), cy + 1.25*(p[1]-cy))], 'resultat', dash=True, lw=0.6)
grid(44, cy, 'resultat')
grid(73, cy, 'fixe'); pent(73, cy, 10, 'limite', fill=False)
text(ax, 29.5, cy, '+', 'encre', 'xl'); text(ax, 58.5, cy, '=', 'encre', 'xl')
text(ax, 15, 12, 'ordre 5 seul :\n$D_5$ existe'.replace('$', '$'), 'resultat', 's')
text(ax, 44, 12, 'réseau seul :\nexiste', 'resultat', 's')
text(ax, 73, 12, 'ensemble :\nimpossible', 'limite', 's')
text(ax, 44, 52, 'l’obstacle vient de leur rencontre', 'encre', 's')
save(fig, '74-176')
