import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ring(cx, cy, R, n):
    return [(cx + R * math.sin(2 * math.pi * k / n), cy + R * math.cos(2 * math.pi * k / n)) for k in range(n)]

def hop(ax, p, q, r, role='varie', curve=0.0, lw=0.8):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r), role, lw=lw, curve=curve)

fig, ax = canvas(60)
def strip(y, vals, role, title, cyc):
    text(ax, 44, y + 11, title, role, 's')
    w = 10
    for i, v in enumerate(vals):
        x = 4 + i * 12
        box(ax, x, y, w, 8, role if v != '…' else 'fixe', fill=v != '…', label=v, size='s')
        if i < len(vals) - 1: arrow(ax, (x + w + 0.2, y + 4), (x + 11.8, y + 4), 'varie', lw=0.8)
    return
strip(34, ['0', '4', '8', '0', '4', '8', '…'], 'sujet', 'ℤ/12ℤ, pas 4 : les valeurs reviennent', 1)
brace(ax, 4, 4 + 3 * 12 - 2, 33, 'sujet', label='se répète', depth=1.6)
strip(8, ['0', '1', '2', '3', '4', '5', '…'], 'autre', 'ℤ, pas 1 : aucune ne revient', 0)
save(fig, '46-092')
