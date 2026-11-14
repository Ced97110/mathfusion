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

fig, ax = canvas(70)
line(ax, [(22, 26), (22, 50)], 'sujet', lw=1.8); line(ax, [(8, 38), (36, 38)], 'fixe', lw=1.8)
line(ax, [(22, 35), (25, 35), (25, 38)], 'resultat')
text(ax, 22, 56, 'droites perpendiculaires', 'encre', 's')
text(ax, 22, 12, 'deux droites : 90°', 'sujet', 's')
P = mk((66, 30), 4.5)
poly(ax, [P(-2.6, -2.6, 0), P(2.6, -2.6, 0), P(2.6, 2.6, 0), P(-2.6, 2.6, 0)], 'fixe', lw=0.6)
dirs = [(1, 0, 0), (0, 1, 0), unit((1, 1, 0)), unit((1, -1, 0))]
for d in dirs: line(ax, [P(*add((0, 0, 0), d, -2.4)), P(*add((0, 0, 0), d, 2.4))], 'varie', lw=1.0)
line(ax, [P(0, 0, 0), P(0, 0, 5)], 'sujet', lw=2.0)
for d in (dirs[0], dirs[1], dirs[3]): rmark(ax, P, (0, 0, 0), d, (0, 0, 1), 0.9)
dot(ax, P(0, 0, 0), 'sujet', 1.1)
lab(ax, P, (0, 0, 5), r'$d$', 3, 1, 'sujet'); lab(ax, P, (0, 0, 0), r'$O$', 3.5, -3.2, 'sujet')
text(ax, 66, 8, 'droite et plan :', 'sujet', 's'); text(ax, 66, 4, '90° avec toutes par $O$', 'sujet', 's')
save(fig, '27-026')
