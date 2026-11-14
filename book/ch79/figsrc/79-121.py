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
fig, ax = canvas(75)
box(ax, 2, 62, 38, 10, 'sujet', label=r'$4 \vee (6 \wedge 10)$', size='s')
box(ax, 48, 62, 38, 10, 'sujet', label=r'$(4 \vee 6) \wedge (4 \vee 10)$', size='s')
box(ax, 2, 46, 38, 9, 'fixe', label='PGCD(6 ; 10) = 2', size='s')
box(ax, 2, 30, 38, 9, 'fixe', label='PPCM(4 ; 2) = 4', size='s')
box(ax, 2, 12, 38, 10, 'resultat', label='4', size='l')
box(ax, 48, 46, 18, 12, 'fixe', label='PPCM(4 ; 6)\n= 12', size='s')
box(ax, 68, 46, 18, 12, 'fixe', label='PPCM(4 ; 10)\n= 20', size='s')
box(ax, 48, 30, 38, 9, 'fixe', label='PGCD(12 ; 20) = 4', size='s')
box(ax, 48, 12, 38, 10, 'resultat', label='4', size='l')
for a, b in ((61.5, 55.5), (45.5, 39.5), (29.5, 22.5)): arrow(ax, (21, a), (21, b), 'varie')
for x in (57, 77): arrow(ax, (x, 61.5), (x, 58.5), 'varie'); arrow(ax, (x, 45.5), (x, 39.5), 'varie') if x == 57 else arrow(ax, (x, 45.5), (x, 39.5), 'varie')
arrow(ax, (67, 29.5), (67, 22.5), 'varie')
text(ax, 44, 17, '=', 'resultat', 'l')
save(fig, '79-121')
