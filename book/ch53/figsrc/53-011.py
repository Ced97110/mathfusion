import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
cx, cy, R = 44, 45, 32
def pos(i, r, n=26):
    a = math.radians(90 - i * 360 / n); return (cx + r * math.cos(a), cy + r * math.sin(a))
def arc(i0, i1, r, role):
    pts = [pos(i0 + (i1 - i0) * k / 24, r) for k in range(25)]
    line(ax, pts, role, lw=1.3); arrow(ax, pts[-3], pts[-1], role, lw=1.3)
for i in range(26):
    x, y = pos(i, R)
    disc(ax, x, y, 2.0 if i in (0, 3, 23) else 0.9, 'sujet' if i in (0, 3, 23) else 'fixe')
for i, ch in [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (23, 'X'), (24, 'Y'), (25, 'Z')]:
    x, y = pos(i, R + 5); text(ax, x, y, ch, 'sujet' if i in (0, 3, 23) else 'encre', 's')
for i, nb in [(0, '0'), (3, '3'), (23, '23')]:
    x, y = pos(i, R - 6); text(ax, x, y, nb, 'fixe', 's')
arc(0.1, 2.9, R - 16, 'varie'); arc(23.1, 25.9, R - 9, 'varie')
x, y = pos(1.5, R - 22); text(ax, x, y, '+3', 'varie', 's')
x, y = pos(24.5, R - 15); text(ax, x, y, '+3', 'varie', 's')
text(ax, cx, cy + 3, r'$f(p) = p + 3$', 'sujet', 'l')
text(ax, cx, cy - 5, '23 + 3 = 26 → 0', 'resultat', 's')
save(fig, '53-011')
