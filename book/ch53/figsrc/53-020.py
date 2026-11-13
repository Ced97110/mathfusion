import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
cx, cy, R = 44, 44, 30
def pos(i, r, n=26):
    a = math.radians(90 - i * 360 / n); return (cx + r * math.cos(a), cy + r * math.sin(a))
def arc(i0, i1, r, role):
    pts = [pos(i0 + (i1 - i0) * k / 24, r) for k in range(25)]
    line(ax, pts, role, lw=1.3); arrow(ax, pts[-3], pts[-1], role, lw=1.3)
mark = {3: 'D', 0: 'A', 23: 'X', 24: 'Y', 25: 'Z'}
for i in range(26):
    x, y = pos(i, R)
    disc(ax, x, y, 2.0 if i in mark else 0.9, 'sujet' if i in mark else 'fixe')
for i, ch in mark.items():
    x, y = pos(i, R + 5); text(ax, x, y, ch, 'sujet', 's')
arc(2.9, 0.1, R - 9, 'varie'); arc(-0.1, -2.9, R - 16, 'varie')
x, y = pos(1.5, R - 15); text(ax, x, y, '− 3', 'varie', 's')
x, y = pos(-1.5, R - 22); text(ax, x, y, '− 3', 'varie', 's')
text(ax, cx, cy, 'retrancher 3 :\nsens inverse', 'encre', 'm')
save(fig, '53-020')
