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

fig, ax = canvas(56); P = mk((24, 12), 6.2)
pave(ax, P)
tri(ax, P, 'ACGE', 'fixe'); tri(ax, P, 'ACG', 'sujet', lw=1.2)
seg(ax, P, 'A', 'G', 'varie', lw=1.3)
lab(ax, P, V['A'], r'$A$', 3, 0); lab(ax, P, V['C'], r'$C$', -3, 0); lab(ax, P, V['G'], r'$G$', -3, 2)
text(ax, 26, 5, 'feuille dans la boîte', 'fixe', 's')
a, c, g = (55, 18), (82, 18), (82, 18 + 27 * 0.4)
poly(ax, [a, c, g], 'sujet', lw=1.2)
line(ax, [(c[0] - 3, c[1]), (c[0] - 3, c[1] + 3), (c[0], c[1] + 3)], 'resultat')
for p, s, d in ((a, r'$A$', (-3, -1)), (c, r'$C$', (2, -3)), (g, r'$G$', (0, 3.5))): text(ax, p[0] + d[0], p[1] + d[1], s)
arrow(ax, (48, 30), (53, 30), 'varie')
text(ax, 68, 5, 'à plat : même forme', 'sujet', 's')
save(fig, '27-021')
