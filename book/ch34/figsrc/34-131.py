import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def tri(x0, y0, adj, opp, s, role):
    poly(ax, [(x0, y0), (x0 + adj * s, y0), (x0 + adj * s, y0 + opp * s)], role)
    ang = math.atan2(opp, adj); r = 4.5
    line(ax, [(x0 + r * math.cos(t * ang / 20), y0 + r * math.sin(t * ang / 20)) for t in range(21)], 'varie', lw=1.2)
rows = [(40, 4, 3, 3.0, 7, 24, 1.0, r'$A$ : 3-4-5', r'$2A$ : 7-24-25'),
        (7, 12, 5, 1.6, 119, 120, 0.2, r'$A$ : 5-12-13', r'$2A$ : 119-120-169')]
for (y0, a1, o1, s1, a2, o2, s2, c1, c2) in rows:
    tri(4, y0, a1, o1, s1, 'sujet'); tri(52, y0, a2, o2, s2, 'resultat')
    text(ax, 4, y0 - 3.5, c1, 'sujet', 's', ha='left')
    text(ax, 52, y0 - 3.5, c2, 'resultat', 's', ha='left')
    arrow(ax, (4 + a1 * s1 + 3, y0 + 8), (48, y0 + 8), 'varie')
    text(ax, 32, y0 + 12, 'angle double', 'varie', 's')
save(fig, '34-131')
