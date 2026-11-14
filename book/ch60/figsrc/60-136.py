import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
x0, ytop, cw, ch = 3, 66, 11.5, 9
for i in range(4):
    for j in range(2):
        role = 'sujet' if j == 0 else 'varie'
        box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, label=f'({i}, {j})', size='s', r=0.5)
    box(ax, x0 - 0.7, ytop - (i + 1) * ch - 0.2, 2 * cw + 1.4, ch + 0.4, 'fixe', fill=False, dash=True, lw=0.9, r=0.6)
text(ax, x0 + cw, ytop + 4, 'G : 8 cases', 'encre', 's')
arrow(ax, (29, 48), (40, 48), 'fixe')
text(ax, 34.5, 53, 'sur H', 'fixe', 's')
cx, cy, R, r = 65, 40, 14, 5.8
names = ['0 + H', r'$g + H$', r'$2g + H$', r'$3g + H$']
pos = []
for k in range(4):
    a = math.radians(90 - 90 * k)
    pos.append((cx + R * math.cos(a), cy + R * math.sin(a)))
for k, (x, y) in enumerate(pos):
    disc(ax, x, y, r, 'sujet', label=names[k], size='s')
for k in range(4):
    (x1, y1), (x2, y2) = pos[k], pos[(k + 1) % 4]
    a1 = math.atan2(y2 - y1, x2 - x1)
    arrow(ax, (x1 + (r + 0.6) * math.cos(a1), y1 + (r + 0.6) * math.sin(a1)),
          (x2 - (r + 0.6) * math.cos(a1), y2 - (r + 0.6) * math.sin(a1)), 'varie', curve=-0.25)
text(ax, cx, cy + 2, '+ g', 'varie', 's')
text(ax, cx, cy - 2.5, 'ordre 4', 'sujet', 's', weight='bold')
text(ax, cx, ytop + 4, 'G/H : 4 classes', 'encre', 's')
save(fig, '60-136')
