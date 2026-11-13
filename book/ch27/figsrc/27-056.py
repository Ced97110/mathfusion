import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 11
o = (39.3, 8)
P = lambda x, y, z: iso(x, y, z, o, u)
V = {'B': (0, 0, 0), 'A': (4, 0, 0), 'C': (0, 3, 0), 'D': (4, 3, 0),
     'F': (0, 0, 2), 'E': (4, 0, 2), 'G': (0, 3, 2), 'K': (4, 3, 2)}
def wire(role='fixe', lw=0.8):
    hidden = [('D', 'A'), ('D', 'C'), ('D', 'K')]
    edges = [('B', 'A'), ('B', 'C'), ('B', 'F'), ('A', 'E'), ('C', 'G'), ('F', 'E'), ('F', 'G'), ('E', 'K'), ('G', 'K')]
    for p, q in edges: line(ax, [P(*V[p]), P(*V[q])], role, lw=lw)
    for p, q in hidden: line(ax, [P(*V[p]), P(*V[q])], role, lw=lw * 0.8, dash=True)
wire('fixe', 0.7)
pa, pc, pg = P(*V['A']), P(*V['C']), P(*V['G'])
def ang(p): return math.atan2(p[1] - pa[1], p[0] - pa[0])
a1 = ang(pc); a2 = a1 + (ang(pg) - a1 + math.pi) % (2 * math.pi) - math.pi
r = 14
pts = [pa] + [(pa[0] + r * math.cos(a1 + (a2 - a1) * k / 12), pa[1] + r * math.sin(a1 + (a2 - a1) * k / 12)) for k in range(13)]
poly(ax, pts, 'sujet', lw=0.5)
line(ax, [pa, pc], 'sujet', lw=2.0)
line(ax, [pa, pg], 'sujet', lw=2.0)
for k in 'ACG': disc(ax, *P(*V[k]), 1.1, 'sujet')
text(ax, pa[0] + 3, pa[1] - 2.5, r'$A$', 'sujet', 'm')
text(ax, pc[0] - 3, pc[1] - 2.5, r'$C$', 'sujet', 'm')
text(ax, pg[0] - 3, pg[1] + 3, r'$G$', 'sujet', 'm')
text(ax, 6, 62, r'$\widehat{GAC}$', 'sujet', 'xl', ha='left')
text(ax, 6, 55.5, 'angle de sommet A', 'sujet', 's', ha='left')
mid = ((pa[0] + pg[0]) / 2, (pa[1] + pg[1]) / 2)
text(ax, mid[0] + 9, mid[1] + 8, 'câble', 'sujet', 's')
text(ax, (pa[0] + pc[0]) / 2 - 2, (pa[1] + pc[1]) / 2 - 7, 'diagonale du sol', 'sujet', 's', ha='right')
save(fig, '27-056')
