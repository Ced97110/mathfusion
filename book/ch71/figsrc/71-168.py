import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 18
def panel(cx, a, b, role, la, lb, lab, right):
    cy = 30
    P = lambda p: (cx + p[0] * u, cy + p[1] * u)
    arrow(ax, P(a), P(a)) if False else None
    arrow(ax, (cx, cy), P(a), role, lw=1.3); arrow(ax, (cx, cy), P(b), role, lw=1.3)
    if right:
        s = 3.2; line(ax, [(cx + s * 0.707, cy + s * 0.707 - 0), (cx + s * 1.414, cy), (cx + s * 0.707, cy - s * 0.707)], 'resultat', lw=0.8)
    else:
        arc = [(cx + 5 * math.cos(math.radians(t)), cy + 5 * math.sin(math.radians(t))) for t in range(0, 121, 5)]
        line(ax, arc, 'limite', lw=0.9)
    return P
Pl = panel(22, (1, 0), (-0.6, 1), 'sujet', '', '', '', False)
Pr = panel(66, (1, 1), (1, -1), 'resultat', '', '', '', True)
text(ax, 22, 60, 'Lagrange, 1re courbe', 'sujet', 's')
text(ax, 66, 60, 'base choisie', 'resultat', 's')
text(ax, 31, 25, r'$(1,\ 0)$', 'sujet', 's')
text(ax, 10, 53, r'$(-\frac{3}{5},\ 1)$', 'sujet', 's')
text(ax, 80, 52, r'$u_1 = (1,\ 1)$', 'resultat', 's', ha='right')
text(ax, 80, 8, r'$u_2 = (1,\ -1)$', 'resultat', 's', ha='right')
text(ax, 22, 6, 'orthogonales pour $B$\npas perpendiculaires', 'limite', 's')
text(ax, 66, 17, 'perpendiculaires', 'resultat', 's')
save(fig, '71-168')
