import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def sq(cx, cy, k, role='varie'):
    th = math.radians(90 * k + 45)
    pts = [(cx + 6 * math.cos(th + j * math.pi / 2), cy + 6 * math.sin(th + j * math.pi / 2)) for j in range(4)]
    poly(ax, pts, role)
    disc(ax, (pts[0][0] + cx) / 2, (pts[0][1] + cy) / 2, 1.3, 'sujet')
cx = [16, 44, 72]
for x, s, r in zip(cx, ['rotations', 'heures', 'nombres'], ['varie', 'sujet', 'autre']):
    text(ax, x, 73, s, r, 'm')
sq(16, 56, 1); sq(16, 18, 2)
box(ax, 37, 51, 14, 10, 'sujet', label='1'); box(ax, 37, 13, 14, 10, 'sujet', label='2')
box(ax, 65, 51, 14, 10, 'autre', label='$i$'); box(ax, 65, 13, 14, 10, 'autre', label='$-1$')
for x in cx:
    arrow(ax, (x, 46), (x, 29), 'varie')
    text(ax, x + 3, 37.5, '2 fois', 'varie', 's', ha='left')
line(ax, [(24, 56), (36, 56)], 'fixe', dash=True); line(ax, [(52, 56), (64, 56)], 'fixe', dash=True)
line(ax, [(24, 18), (36, 18)], 'fixe', dash=True); line(ax, [(52, 18), (64, 18)], 'fixe', dash=True)
text(ax, 44, 4, 'autres éléments, même structure', 'resultat', 's')
save(fig, '45-219')
