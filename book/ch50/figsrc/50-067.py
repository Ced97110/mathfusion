import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tri(cx, cy, R, axis, role):
    c30 = math.cos(math.radians(30))
    V = {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}
    poly(ax, [V['A'], V['B'], V['C']], 'fixe')
    v = V[axis]
    line(ax, [(cx + 1.3 * (v[0] - cx), cy + 1.3 * (v[1] - cy)), (cx - 0.85 * (v[0] - cx), cy - 0.85 * (v[1] - cy))], role, lw=1.8)
    return V
fig, ax = canvas(84)
R = 10
disc(ax, 44, 41, 41, 'sujet', fill=False, lw=1.0)
ax.patches[-1].set_linestyle('--')
pos = {'A': (44, 63), 'B': (17, 28), 'C': (71, 28)}
for k, (cx, cy) in pos.items():
    V = tri(cx, cy, R, k, 'sujet')
V = tri(44, 63, R, 'A', 'sujet')
for k, (dx, dy) in {'A': (-2.8, 1.2), 'B': (-2.6, -1.2), 'C': (2.6, -1.2)}.items():
    text(ax, V[k][0] + dx, V[k][1] + dy, k, 'fixe', 's')
text(ax, 58, 66, r'$\{e,\ s_A\}$', 'sujet', 's', ha='left')
text(ax, 20, 11, r'$\{e,\ s_B\}$', 'sujet', 's')
text(ax, 68, 11, r'$\{e,\ s_C\}$', 'sujet', 's')
text(ax, 44, 44, r'$\Sigma$ : l’orbite', 'sujet', 'm', weight='bold')
arrow(ax, (36, 56), (20, 41), 'varie', curve=0.2, lw=1.3)
arrow(ax, (30, 20), (58, 20), 'varie', lw=1.3)
arrow(ax, (68, 41), (52, 56), 'varie', curve=0.2, lw=1.3)
text(ax, 25, 53, '$r$', 'varie', 'm', weight='bold')
text(ax, 44, 23.5, '$r$', 'varie', 'm', weight='bold')
text(ax, 63, 53, '$r$', 'varie', 'm', weight='bold')
save(fig, '50-067')
