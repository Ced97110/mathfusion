import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
cx, cy, R = 44, 45, 32
def pos(i, r, n=26):
    a = math.radians(90 - i * 360 / n); return (cx + r * math.cos(a), cy + r * math.sin(a))
def arc(i0, i1, r, role):
    pts = [pos(i0 + (i1 - i0) * k / 24, r) for k in range(25)]
    line(ax, pts, role, lw=1.3); arrow(ax, pts[-3], pts[-1], role, lw=1.3)
mark = {24: 'Y', 25: 'Z', 0: 'A', 1: 'B'}
for i in range(26):
    x, y = pos(i, R)
    disc(ax, x, y, 2.0 if i in mark else 0.9, ('sujet' if i == 0 else 'autre') if i in mark else 'fixe')
for i, ch in mark.items():
    x, y = pos(i, R + 5); text(ax, x, y, ch, 'sujet' if i == 0 else 'autre', 's')
arc(24, 27, R - 8, 'varie')
arc(6, 10, R - 8, 'fixe')
text(ax, cx + 22, cy - 24, 'sens horaire', 'fixe', 's')
text(ax, cx, cy + 2, 'avancer de 3 crans', 'varie', 'm')
text(ax, cx, cy - 6, 'Y → Z → A → B', 'encre', 's')
save(fig, '53-012')
