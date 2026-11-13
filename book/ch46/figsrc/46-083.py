import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(80)
text(ax, 44, 76, 'Groupe cyclique : tout est puissance de a', 'sujet', 's')
box(ax, 4, 52, 36, 11, 'sujet', label=r'$a^m \cdot a^n$')
box(ax, 48, 52, 36, 11, 'sujet', label=r'$a^n \cdot a^m$')
box(ax, 22, 36, 44, 11, 'resultat', label=r'$a^{m+n}$ dans les deux cas')
hop(ax, (22, 52), (36, 47), 0.3, 'resultat')
hop(ax, (66, 52), (52, 47), 0.3, 'resultat')
text(ax, 44, 28, 'Trois cartes : l\'ordre change', 'autre', 's')
box(ax, 4, 6, 36, 17, 'autre', label='1↔2 puis 1↔3\nla carte 1 va en 2', size='s')
box(ax, 48, 6, 36, 17, 'limite', label='1↔3 puis 1↔2\nla carte 1 va en 3', size='s')
text(ax, 44, 14.5, r'$\neq$', 'limite', 'l')
save(fig, '46-083')
