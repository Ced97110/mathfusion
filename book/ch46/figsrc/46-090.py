import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(60)
text(ax, 44, 56, 'S₃ : l’ordre des échanges compte', 'autre', 's')
box(ax, 2, 24, 14, 9, 'fixe', label='ABC', size='s')
rows = [(40, '1↔2', 'BAC', '1↔3', 'CAB', 'autre'), (12, '1↔3', 'CBA', '1↔2', 'BCA', 'varie')]
for y, s1, m, s2, e, role in rows:
    box(ax, 34, y - 4.5, 14, 9, role, label=m, size='s')
    box(ax, 70, y - 4.5, 16, 9, 'limite', label=e, size='s')
    hop(ax, (16, 30 if y > 20 else 27), (34, y), 0, role, 0.0, 0.9)
    arrow(ax, (48, y), (70, y), role, lw=0.9)
    text(ax, 25, y + (4 if y > 20 else -4), s1, role, 's')
    text(ax, 59, y + 3.5, s2, role, 's')
text(ax, 78, 26, r'$\neq$', 'limite', 'l')
text(ax, 78, 48.5, 'A en place 2', 'limite', 's')
text(ax, 78, 12 - 8, 'A en place 3', 'limite', 's')
save(fig, '46-090')
