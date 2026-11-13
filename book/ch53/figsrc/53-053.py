import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

reached = {(2 * k) % 26 for k in range(26)}
assert all(r % 2 == 0 for r in reached) and 1 not in reached

fig, ax = canvas(58)
w, x0, y, h = 3.2, 2.4, 28, 7
for v in range(26):
    role = 'limite' if v == 1 else ('varie' if v in reached else 'fixe')
    box(ax, x0 + v * w, y, w, h, role, r=0.3, lw=0.5)
    if v in (0, 1, 2, 25):
        text(ax, x0 + (v + 0.5) * w, y - 3, str(v), role if v == 1 else 'fixe', 's')
box(ax, 2, 44, 44, 11, 'limite', label='1 est impair :\njamais atteint', size='s')
arrow(ax, (x0 + 1.5 * w, 44), (x0 + 1.5 * w, y + h + 0.5), 'limite', lw=0.8)
box(ax, 40, 4, 46, 11, 'varie', label=r'$a = 2$ : les restes de $2 \times k$' + '\nsont toujours pairs', size='s')
arrow(ax, (x0 + 12.5 * w, 15), (x0 + 12.5 * w, y - 0.5), 'varie', lw=0.8)
save(fig, '53-053')
