import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(60)
def row(y, name, vals, role, last):
    text(ax, 4, y + 4, name, role, 's', ha='left')
    for i, v in enumerate(vals):
        x = 28 + i * 15
        r = last if i == len(vals) - 1 else role
        box(ax, x, y, 12, 8, r, fill=v != '…', label=v, size='s')
        if i < len(vals) - 1: arrow(ax, (x + 12.2, y + 4), (x + 14.8, y + 4), 'varie', lw=0.8)
row(42, 'ordre 1', ['0', '0'], 'sujet', 'resultat')
row(24, 'ordre 12', ['5', '10', '…', '0'], 'sujet', 'resultat')
row(6, 'ordre ∞', ['1', '2', '…', '≠ 0'], 'autre', 'limite')
save(fig, '46-095')
