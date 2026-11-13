import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(56)
x0, w = 22, 10
text(ax, 11, 49, 'ℤ/6ℤ', 'sujet', 's')
for k in range(6):
    text(ax, x0 + k * w + w / 2, 49, str(k), 'encre', 's')
rows = [('+1', set(range(6)), 'resultat', '6 heures'), ('+5', set(range(6)), 'resultat', '6 heures'), ('+2', {0, 2, 4}, 'limite', '3 heures')]
for i, (name, vis, role, cnt) in enumerate(rows):
    y = 33 - i * 14
    text(ax, 11, y + 4, name, 'varie', 'm')
    for k in range(6):
        box(ax, x0 + k * w + 0.5, y, w - 1, 8, 'sujet' if k in vis else 'fixe', fill=k in vis)
    text(ax, 44, y - 3.2, cnt, role, 's')
save(fig, '46-087')
