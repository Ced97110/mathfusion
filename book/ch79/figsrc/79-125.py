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
fig, ax = canvas(78)
box(ax, 4, 65, 14, 9, 'sujet', label='4'); text(ax, 24, 69.5, r'$\leq$', 'sujet', 'l'); box(ax, 30, 65, 14, 9, 'sujet', label='12')
box(ax, 56, 65, 28, 9, 'autre', label=r'$c = 30$')
box(ax, 2, 50, 38, 9, 'sujet', label=r'$12 \wedge (4 \vee 30)$', size='s')
box(ax, 48, 50, 38, 9, 'sujet', label=r'$4 \vee (12 \wedge 30)$', size='s')
box(ax, 2, 36, 38, 9, 'fixe', label='PPCM(4 ; 30) = 60', size='s'); box(ax, 2, 22, 38, 9, 'fixe', label='PGCD(12 ; 60) = 12', size='s')
box(ax, 48, 36, 38, 9, 'fixe', label='PGCD(12 ; 30) = 6', size='s'); box(ax, 48, 22, 38, 9, 'fixe', label='PPCM(4 ; 6) = 12', size='s')
box(ax, 2, 6, 38, 9, 'resultat', label='12', size='l'); box(ax, 48, 6, 38, 9, 'resultat', label='12', size='l')
for x in (21, 67):
    for a, b in ((49.5, 45.5), (35.5, 31.5), (21.5, 15.5)): arrow(ax, (x, a), (x, b), 'varie')
text(ax, 44, 10.5, '=', 'resultat', 'l')
save(fig, '79-125')
