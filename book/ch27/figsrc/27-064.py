import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
u = 11
o = (47, 8)
P = lambda x, y, z: iso(x, y, z, o, u)
V = {'B': (0, 0, 0), 'A': (4, 0, 0), 'C': (0, 3, 0), 'D': (4, 3, 0),
     'F': (0, 0, 2), 'E': (4, 0, 2), 'G': (0, 3, 2), 'K': (4, 3, 2)}
def wire(role='fixe', lw=0.8):
    hidden = [('D', 'A'), ('D', 'C'), ('D', 'K')]
    edges = [('B', 'A'), ('B', 'C'), ('B', 'F'), ('A', 'E'), ('C', 'G'), ('F', 'E'), ('F', 'G'), ('E', 'K'), ('G', 'K')]
    for p, q in edges: line(ax, [P(*V[p]), P(*V[q])], role, lw=lw)
    for p, q in hidden: line(ax, [P(*V[p]), P(*V[q])], role, lw=lw * 0.8, dash=True)
wire('fixe', 0.7)
p, q = 'C', 'G'
pp, pq = P(*V[p]), P(*V[q])
line(ax, [pp, pq], 'sujet', lw=3.0)
for k in (p, q): disc(ax, *P(*V[k]), 1.3, 'sujet')
mid = ((pp[0] + pq[0]) / 2, (pp[1] + pq[1]) / 2)
off = {'AB': (9, -5), 'BC': (-9, -5), 'CG': (-5, 0)}['CG']
text(ax, mid[0] + off[0], mid[1] + off[1], r'$h = 2$', 'sujet', 'xl')
text(ax, mid[0] + off[0], mid[1] + off[1] - 5, 'hauteur du pavé', 'sujet', 's')
text(ax, pp[0] + (3 if p != 'C' else -3), pp[1] - 3, p, 'sujet', 's')
text(ax, pq[0] + (3 if q == 'A' else -3), pq[1] + (-3 if q != 'G' else 3), q, 'sujet', 's')
save(fig, '27-064')
