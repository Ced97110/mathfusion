import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

V = {'A': (4, 0, 0), 'B': (0, 0, 0), 'C': (0, 3, 0), 'D': (4, 3, 0), 'E': (4, 0, 2), 'F': (0, 0, 2), 'G': (0, 3, 2), 'H': (4, 3, 2)}
HID = {('C', 'D'), ('D', 'A'), ('D', 'H')}
EDGES = [('A','B'),('B','C'),('C','D'),('D','A'),('E','F'),('F','G'),('G','H'),('H','E'),('A','E'),('B','F'),('C','G'),('D','H')]
def mk(origin, u): return lambda x, y, z: iso(x, y, z, origin, u)
def add(p, q, k=1.0): return tuple(a + k * b for a, b in zip(p, q))
def unit(v):
    m = math.sqrt(sum(c * c for c in v)); return tuple(c / m for c in v)
def pave(ax, P, role='fixe', lw=0.7):
    for a, b in EDGES: line(ax, [P(*V[a]), P(*V[b])], role, lw=lw, dash=((a, b) in HID or (b, a) in HID))
def seg(ax, P, a, b, role, lw=1.7, dash=False): line(ax, [P(*V[a]), P(*V[b])], role, lw=lw, dash=dash)
def tri(ax, P, names, role, fill=True, lw=1.0): poly(ax, [P(*V[n]) for n in names], role, fill=fill, lw=lw)
def lab(ax, P, p, s, dx, dy, role='encre', size='m'):
    x, y = P(*p); return text(ax, x + dx, y + dy, s, role, size)
def rmark(ax, P, o, a, b, k, role='resultat'):
    p1 = add(o, a, k); p2 = add(p1, b, k); p3 = add(o, b, k)
    line(ax, [P(*p1), P(*p2), P(*p3)], role, lw=0.8)
def arc3(ax, P, o, a, b, r, role, lw=0.8, n=16):
    pts = []
    for i in range(n + 1):
        t = i / n; v = [(1 - t) * x + t * y for x, y in zip(a, b)]; pts.append(P(*add(o, unit(v), r)))
    line(ax, pts, role, lw=lw)
def leg(ax, items, x, y, dy=4.6):
    for i, (role, s) in enumerate(items):
        line(ax, [(x, y - i * dy), (x + 7, y - i * dy)], role, lw=1.8)
        text(ax, x + 9, y - i * dy, s, role, 's', ha='left')
def dot(ax, p, role, r=0.9): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], lw=0.5, zorder=4))

fig, ax = canvas(72); P = mk((28, 38), 6)
poly(ax, [P(-0.5, -0.5, 0), P(4.6, -0.5, 0), P(4.6, 3.6, 0), P(-0.5, 3.6, 0)], 'fixe', lw=0.6)
X, Y, Z = (4, 0, 0), (0, 3, 0), (2.8, 0.9, 0); S, S2, O = (0, 0, 3), (0, 0, -3), (0, 0, 0)
line(ax, [P(*O), P(*X)], 'fixe', lw=1.2); line(ax, [P(*O), P(*Y)], 'fixe', lw=1.2)
line(ax, [P(*O), P(*add(O, unit(Z), 4.3))], 'varie', lw=1.5)
line(ax, [P(*X), P(*Y)], 'fixe', lw=0.9)
for q in (X, Y): line(ax, [P(*q), P(*S)], 'fixe', lw=0.6); line(ax, [P(*q), P(*S2)], 'fixe', lw=0.6, dash=True)
line(ax, [P(*S2), P(*S)], 'sujet', lw=2.0)
line(ax, [P(*Z), P(*S)], 'resultat', lw=1.4); line(ax, [P(*Z), P(*S2)], 'resultat', lw=1.4)
for q, r in ((S, 'autre'), (S2, 'autre'), (O, 'sujet'), (X, 'fixe'), (Y, 'fixe'), (Z, 'resultat')): dot(ax, P(*q), r, 1.0)
lab(ax, P, S, r'$S$', 0, 3.2); lab(ax, P, S2, r'$S^{\prime}$', 0, -3.4); lab(ax, P, O, r'$O$', 3.2, -2.4)
lab(ax, P, X, r'$X$', 3, 0.5); lab(ax, P, Y, r'$Y$', -3, 0.8); lab(ax, P, Z, r'$Z$', -0.5, 3.4, 'resultat')
lab(ax, P, add(O, unit(Z), 4.3), r'$w$', 3, 1.5, 'varie')
z, s, s2, o = (62, 38), (76, 56), (76, 20), (76, 38)
poly(ax, [z, s, s2], 'resultat', lw=1.2); line(ax, [s2, s], 'sujet', lw=2.0); line(ax, [z, o], 'varie', lw=1.5)
line(ax, [(74, 38), (74, 40), (76, 40)], 'encre')
text(ax, 59, 38, r'$Z$', 'resultat'); text(ax, 79, 56, r'$S$', 'autre'); text(ax, 79, 20, r'$S^{\prime}$', 'autre')
text(ax, 4, 11, r'départ : $d\perp u$ et $d\perp v$', 'sujet', 's', ha='left')
text(ax, 4, 6.5, r'étape : $ZS=ZS^{\prime}$', 'resultat', 's', ha='left')
text(ax, 4, 2, r'arrivée : $d\perp w$', 'varie', 's', ha='left')
save(fig, '27-031')
