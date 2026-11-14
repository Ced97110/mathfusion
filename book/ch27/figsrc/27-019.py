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

fig, ax = canvas(80); P = mk((36, 24), 9)
pave(ax, P)
seg(ax, P, 'A', 'B', 'fixe', lw=1.5); seg(ax, P, 'A', 'D', 'fixe', lw=1.5, dash=True)
seg(ax, P, 'A', 'C', 'sujet'); seg(ax, P, 'A', 'G', 'varie')
for t in (0.25, 0.5, 0.75):
    top = (4 - 4 * t, 3 * t, 2 * t); bot = (4 - 4 * t, 3 * t, 0)
    line(ax, [P(*top), P(*bot)], 'resultat', lw=0.9, dash=True); dot(ax, P(*top), 'varie'); dot(ax, P(*bot), 'sujet')
lab(ax, P, (2, 1.5, 0.5), r'1 m', 4.5, 0, 'resultat', 's')
lab(ax, P, V['A'], r'$A$', 3.5, 0); lab(ax, P, V['C'], r'$C$', -3.5, 0); lab(ax, P, V['G'], r'$G$', -3.5, 2)
lab(ax, P, V['B'], r'$B$', 0, -3.5); lab(ax, P, V['D'], r'$D$', 3.5, 1)
leg(ax, [('varie', r'câble $AG$'), ('sujet', r'$AC$ : juste sous le câble'), ('fixe', r'$AB$, $AD$ : pas sous le câble')], 4, 13)
save(fig, '27-019')
