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

fig, ax = canvas(64)
poly(ax, [(4, 6), (84, 6), (84, 30), (4, 30)], 'fixe', lw=0.6)
line(ax, [(4, 30), (84, 30)], 'fixe', lw=1.6)
line(ax, [(34, 8), (34, 52)], 'sujet', lw=1.8)
disc(ax, 34, 48, 1.5, 'sujet'); disc(ax, 34, 12, 1.5, 'autre'); disc(ax, 34, 30, 1.2, 'encre')
arrow(ax, (46, 30), (46, 48), 'resultat', both=True); arrow(ax, (46, 30), (46, 12), 'resultat', both=True)
text(ax, 52, 39, '3 m', 'resultat', 'm', ha='left'); text(ax, 52, 21, '3 m', 'resultat', 'm', ha='left')
text(ax, 38, 51, r'$S$', 'sujet'); text(ax, 38, 11, r'$S^{\prime}$', 'autre', 'l'); text(ax, 29, 33.5, r'$O$')
text(ax, 29, 54, r'$d$', 'sujet'); text(ax, 78, 34, 'sol', 'fixe', 's')
text(ax, 70, 56, r'$OS=OS^{\prime}$', 'resultat', 'l')
save(fig, '27-032')
