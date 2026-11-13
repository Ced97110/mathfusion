import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tri(cx, cy, R, axis, role):
    c30 = math.cos(math.radians(30))
    V = {'A': (cx, cy + R), 'B': (cx - R * c30, cy - R / 2), 'C': (cx + R * c30, cy - R / 2)}
    poly(ax, [V['A'], V['B'], V['C']], 'fixe')
    v = V[axis]
    line(ax, [(cx + 1.3 * (v[0] - cx), cy + 1.3 * (v[1] - cy)), (cx - 0.85 * (v[0] - cx), cy - 0.85 * (v[1] - cy))], role, lw=1.8)
fig, ax = canvas(84)
box(ax, 4, 52, 80, 28, 'sujet')
text(ax, 44, 75, r'$N(H)$', 'sujet', 'm', weight='bold')
box(ax, 24, 55, 40, 14, 'autre', label=r'$H = \{e,\ s_A\}$', size='s')
text(ax, 44, 46, r'chaque $h$ de $H$ garde $H$ :', 'varie', 's')
tri(14, 28, 8, 'A', 'autre')
text(ax, 14, 14, r'$H$', 'autre', 's')
arrow(ax, (27, 28), (60, 28), 'varie', lw=1.3)
text(ax, 43.5, 33, r'conjuguer par $s_A$', 'varie', 's')
tri(74, 28, 8, 'A', 'resultat')
text(ax, 74, 14, r'$s_A H s_A^{-1} = H$', 'resultat', 's')
save(fig, '50-075')
