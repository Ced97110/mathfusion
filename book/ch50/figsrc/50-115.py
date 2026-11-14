import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
r = 10; cy = 36; C30 = math.cos(math.radians(30))
def tri(cx, v):
    V = [(cx, cy + r), (cx - r * C30, cy - r / 2), (cx + r * C30, cy - r / 2)]
    poly(ax, V, 'fixe')
    M = (cx - (V[v][0] - cx) / 2, cy - (V[v][1] - cy) / 2)
    line(ax, [V[v], M], 'sujet', lw=1.8)
    return V
cxs = [18, 44, 70]
for i, (cx, n) in enumerate(zip(cxs, 'ABC')):
    V = tri(cx, i)
    text(ax, cx, cy - r / 2 - 4.5, r'$P_%s$' % n, 'sujet', 'm')
V = [(cxs[0], cy + r), (cxs[0] - r * C30, cy - r / 2), (cxs[0] + r * C30, cy - r / 2)]
text(ax, V[0][0], V[0][1] + 3, 'A', 'encre', 's')
text(ax, V[1][0] - 3, V[1][1] - 1, 'B', 'encre', 's')
text(ax, V[2][0] + 3, V[2][1] - 1, 'C', 'encre', 's')
brace(ax, 6, 82, 22, 'sujet', label=r'$\mathcal{S}=\{P_A,P_B,P_C\}$ : $k=3$ conjugués')
save(fig, '50-115')
