import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 24, 33, 17
P = lambda k: (cx + R * math.sin(math.radians(30 * k)), cy + R * math.cos(math.radians(30 * k)))
for k in range(12):
    x, y = P(k)
    if k % 3 == 0: disc(ax, x, y, 2.2, 'sujet')
    else: disc(ax, x, y, 1.0, 'fixe')
for k in (0, 3, 6, 9):
    x, y = P(k); ux, uy = (x - cx) / R, (y - cy) / R
    text(ax, x + ux * 5, y + uy * 5, str(k), 'sujet', 's')
for k in (0, 3, 6, 9):
    x0, y0 = P(k); x1, y1 = P(k + 3)
    arrow(ax, (x0 + (x1 - x0) * 0.2, y0 + (y1 - y0) * 0.2), (x0 + (x1 - x0) * 0.8, y0 + (y1 - y0) * 0.8), 'varie', lw=0.9)
text(ax, cx, cy, r'pas $3 = 12 ÷ 4$', 'varie', 's')
text(ax, 66, 61, r'$q$ : sous-groupe', 'encre', 's')
rows = [(1, '12'), (2, '6'), (3, '4'), (4, '3'), (6, '2'), (12, '1')]
for i, (q, e) in enumerate(rows):
    y = 52 - i * 8
    role = 'sujet' if q == 4 else 'fixe'
    box(ax, 50, y - 3.2, 32, 6.4, role, label=rf'$q={q}$ : $a^{{{e}}}$', size='s')
save(fig, '46-118')
