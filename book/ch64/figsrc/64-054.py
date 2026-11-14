import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx, cy, s = 24, 46, 13
V = {1: (cx - s, cy - s), 2: (cx + s, cy - s), 3: (cx + s, cy + s), 4: (cx - s, cy + s)}
poly(ax, [V[1], V[2], V[3], V[4]], 'sujet')
e = 4
for a, b in [((cx - s - e, cy - s - e), (cx + s + e, cy + s + e)), ((cx + s + e, cy - s - e), (cx - s - e, cy + s + e)),
             ((cx, cy - s - e), (cx, cy + s + e)), ((cx - s - e, cy), (cx + s + e, cy))]:
    line(ax, [a, b], 'autre', lw=0.8, dash=True)
ang = [math.radians(a) for a in range(30, 321, 10)]
pts = [(cx + 6 * math.cos(t), cy + 6 * math.sin(t)) for t in ang]
line(ax, pts, 'varie', lw=1.1)
arrow(ax, pts[-3], pts[-1], 'varie', lw=1.1)
off = {1: (-4, -4), 2: (4, -4), 3: (4, 4), 4: (-4, 4)}
for k in V:
    text(ax, V[k][0] + off[k][0], V[k][1] + off[k][1], str(k), 'sujet', 'm')
text(ax, cx, 20, '4 rotations', 'varie', 's')
text(ax, cx, 13, '4 axes de symétrie', 'autre', 's')
box(ax, 54, 14, 32, 54, 'fixe', label=None)
text(ax, 70, 62, r'$S_4$ : 24', 'encre', 'm')
box(ax, 58, 24, 24, 24, 'sujet', label=r'$D_4$ : 8', size='m')
text(ax, 70, 8, r'$D_4\subset S_4$', 'sujet', 'm')
text(ax, 70, 55, 'permutations', 'fixe', 's')
save(fig, '64-054')
