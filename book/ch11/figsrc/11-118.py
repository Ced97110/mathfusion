import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 6; yb = 26
data = [(1, '3,14', 11), (2, '12,56', 33), (3, '28,26', 67)]
for r, A, cx in data:
    disc(ax, cx, yb+r*u, r*u, 'sujet')
    line(ax, [(cx, yb+r*u), (cx+r*u, yb+r*u)], 'varie', lw=1.2)
    text(ax, cx, yb-4.5, f'r = {r}', 'varie', 's')
    text(ax, cx, yb-9.5, f'A = {A}', 'sujet', 's')
    text(ax, cx, yb-14.5, f'A ÷ r² = 3,14', 'fixe', 's')
text(ax, 44, 68, 'A ÷ r² reste 3,14 (≈ π)', 'fixe', 's')
save(fig, '11-118')
