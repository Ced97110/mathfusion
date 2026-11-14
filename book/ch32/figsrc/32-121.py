import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
cx, cy, r = 44, 56, 26
disc(ax, cx, cy, r, 'fixe', fill=False)
line(ax, [(cx - r - 3, cy), (cx + r + 3, cy)], 'fixe')
line(ax, [(cx, cy - r - 3), (cx, cy + r + 3)], 'sujet', lw=1.4)
yy = cy + r * math.sin(math.radians(210)); dx = r * math.cos(math.radians(30))
line(ax, [(cx - dx - 3, yy), (cx + dx + 3, yy)], 'autre', lw=1.2, dash=True)
for a, role in ((90, 'sujet'), (270, 'sujet'), (210, 'autre'), (330, 'autre')):
    px, py = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
    disc(ax, px, py, 1.9, role)
    ox, oy = {90: (0, 4), 270: (0, -4), 210: (-7, -1), 330: (7, -1)}[a]
    text(ax, px + ox, py + oy, f'{a}°', role, 's')
text(ax, 44, 15, 'cos x = 0 : 90°, 270°', 'sujet', 's')
text(ax, 44, 7, '1 + 2 sin x = 0 : 210°, 330°', 'autre', 's')
save(fig, '32-121')
