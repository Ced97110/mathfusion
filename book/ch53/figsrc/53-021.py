import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
cx, cy, R = 44, 48, 30
def pos(i, r, n=26):
    a = math.radians(90 - i * 360 / n); return (cx + r * math.cos(a), cy + r * math.sin(a))
def arc(i0, i1, r, role):
    pts = [pos(i0 + (i1 - i0) * k / 48, r) for k in range(49)]
    line(ax, pts, role, lw=1.3); arrow(ax, pts[-3], pts[-1], role, lw=1.3)
for i in range(26):
    x, y = pos(i, R)
    disc(ax, x, y, 2.0 if i in (0, 3) else 0.9, 'sujet' if i in (0, 3) else 'fixe')
for i, ch in [(0, 'A'), (3, 'D')]:
    x, y = pos(i, R + 5); text(ax, x, y, ch, 'sujet', 's')
arc(3, 0, R - 5, 'autre')
arc(3, 26, R - 12, 'varie')
x, y = pos(1.5, R - 11); text(ax, x, y, '− 3', 'autre', 's')
x, y = pos(14.5, R - 18); text(ax, x, y, '+ 23', 'varie', 's')
text(ax, cx, cy, '3 + 23 = 26 → 0', 'resultat', 's')
text(ax, 22, 8, 'reculer de 3', 'autre', 'm')
text(ax, 66, 8, 'avancer de 23', 'varie', 'm')
save(fig, '53-021')
