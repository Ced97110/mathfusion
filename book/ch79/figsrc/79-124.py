import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def edge(ax, p, q, r=0.0, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def nd(ax, p, l, role='fixe', r=3.4):
    disc(ax, p[0], p[1], r, role, label=l)
def lat60(ax, o, u, role):
    P = {(i, j, k): iso(j, k, i, o, u) for i in range(3) for j in range(2) for k in range(2)}
    for c in P:
        for d in range(3):
            n = list(c); n[d] += 1; n = tuple(n)
            if n in P: edge(ax, P[c], P[n], 1.3)
    for c in P: nd(ax, P[c], None, role, 1.3)
def cube8(ax, o, u, role):
    P = {(a, b, c): iso(a, b, c, o, u) for a in range(2) for b in range(2) for c in range(2)}
    for c in P:
        for d in range(3):
            n = list(c); n[d] += 1; n = tuple(n)
            if n in P: edge(ax, P[c], P[n], 1.3)
    for c in P: nd(ax, P[c], None, role, 1.3)
def diamond(ax, cx, y0, role):
    pts = [(cx, y0), (cx-9, y0+11), (cx, y0+11), (cx+9, y0+11), (cx, y0+22)]
    for m in pts[1:4]: edge(ax, pts[0], m, 1.3); edge(ax, m, pts[4], 1.3)
    for p in pts: nd(ax, p, None, role, 1.3)
def pent(ax, cx, y0, role):
    P = [(cx, y0), (cx-8, y0+8), (cx-8, y0+18), (cx+9, y0+12), (cx, y0+24)]
    for a, b in [(0,1),(1,2),(2,4),(0,3),(3,4)]: edge(ax, P[a], P[b], 1.3)
    for p in P: nd(ax, p, None, role, 1.3)
fig, ax = canvas(58)
lat60(ax, (15, 22), 7, 'resultat'); cube8(ax, (44, 22), 9, 'resultat'); diamond(ax, 73, 22, 'limite')
for cx, t in ((15, 'diviseurs de 60'), (44, 'parties de 3 stylos'), (73, 'diamant')): text(ax, cx, 14, t, 'encre', 's')
text(ax, 15, 7, 'D vraie', 'resultat', 's'); text(ax, 44, 7, 'D vraie', 'resultat', 's'); text(ax, 73, 7, 'D fausse', 'limite', 's')
brace(ax, 4, 54, 49, 'resultat', label='distributif', down=False)
save(fig, '79-124')
