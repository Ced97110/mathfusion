import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
cx, cy, h = 30, 68, 13.0
poly(ax, [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)], 'sujet')
# axes of the 4 reflections
dc = h * math.sqrt(2)
for sx in (1, -1):
    for t0, t1 in ((-dc - 7, -dc - 3.2), (-dc + 3.2, dc - 3.2), (dc + 3.2, dc + 7)):
        line(ax, [(cx + t0 / math.sqrt(2), cy + sx * t0 / math.sqrt(2)), (cx + t1 / math.sqrt(2), cy + sx * t1 / math.sqrt(2))], 'varie', dash=True)
line(ax, [(cx, cy - h - 5), (cx, cy + h + 5)], 'varie', dash=True)
line(ax, [(cx - h - 5, cy), (cx + h + 5, cy)], 'varie', dash=True)
corner = {1: (cx - h, cy + h), 2: (cx + h, cy + h), 3: (cx + h, cy - h), 4: (cx - h, cy - h)}
for c, p in corner.items():
    disc(ax, p[0], p[1], 2.4, 'sujet', label=str(c), size='s')
arrow(ax, (cx - 5, cy + 6), (cx + 5, cy + 6), 'sujet', curve=-0.5)
text(ax, 70, 76, '4 rotations', 'sujet', 's')
text(ax, 70, 62, '4 réflexions', 'varie', 's')
text(ax, 70, 55, '(axes en pointillés)', 'varie', 's')
sc = 2.2
text(ax, 44, 38, r'nombre de permutations des sommets', 'encre', 's')
for i, (nm, n, role) in enumerate([(r'$C$', 4, 'sujet'), (r'$D$', 8, 'sujet'), (r'$S_4$', 24, 'fixe')]):
    y = 26 - i * 10
    text(ax, 6, y + 3.5, nm, role, 'm')
    box(ax, 14, y, n * sc, 7, role, r=0.6)
    text(ax, 14 + n * sc + 3, y + 3.5, str(n), role, 's', ha='left')
save(fig, '65-080')
