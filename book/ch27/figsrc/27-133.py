import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
u = 32.0; o = (8, 8)
dx, dy = 0.5 * u * math.cos(math.radians(30)), 0.5 * u * math.sin(math.radians(30))
def P(x, y, z): return (o[0] + x * u + y * dx, o[1] + z * u + y * dy)
V = dict(A=(0,0,0), B=(1,0,0), C=(1,1,0), D=(0,1,0), E=(0,0,1), F=(1,0,1), G=(1,1,1), H=(0,1,1))
edges = [('A','B'),('B','C'),('C','D'),('D','A'),('E','F'),('F','G'),('G','H'),('H','E'),('A','E'),('B','F'),('C','G'),('D','H')]
hidden = {('C','D'),('D','A'),('D','H')}
# base cube face fill for depth reading
poly(ax, [P(*V[k]) for k in 'EFGH'], 'sujet')
poly(ax, [P(*V[k]) for k in 'ABFE'], 'sujet')
poly(ax, [P(*V[k]) for k in 'BCGF'], 'sujet')
for a, b in edges:
    line(ax, [P(*V[a]), P(*V[b])], 'fixe', lw=0.7, dash=(a, b) in hidden)
O = P(.5, .5, .5); A_, B_, G_, H_ = P(*V['A']), P(*V['B']), P(*V['G']), P(*V['H'])
ax.add_patch(Polygon([O, A_, B_], closed=True, ec='none', fc=COL['varie'], alpha=0.45, zorder=2.6))
line(ax, [A_, G_], 'sujet', lw=1.6); line(ax, [B_, H_], 'autre', lw=1.6)
disc(ax, O[0], O[1], 0.9, 'varie')
def ang(p, q): return math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))
a0, a1 = ang(O, A_), ang(O, B_)
if a1 < a0: a1 += 360
r = 5
line(ax, [(O[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 12)), O[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 12))) for i in range(13)], 'varie', lw=1.2)
for k, d in (('A', (-2.5, -2.2)), ('B', (2.8, -1.8)), ('G', (2.8, 1.8)), ('H', (-2.8, 1.8))):
    q = P(*V[k]); text(ax, q[0] + d[0], q[1] + d[1], k, 'encre', 'm')
text(ax, O[0] - 3.2, O[1] + 1.8, 'O', 'encre', 'm')
text(ax, 71, 46, 'diagonale $AG$', 'sujet', 's')
text(ax, 71, 39, 'diagonale $BH$', 'autre', 's')
text(ax, 71, 14, 'angle en $O$ :', 'varie', 's'); text(ax, 71, 9.5, 'triangle $OAB$', 'varie', 's')
arrow(ax, (59, 17), (O[0] + 1.5, O[1] - 4.5), 'varie', lw=0.7)
save(fig, '27-133')
