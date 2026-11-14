import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
a = 0.35
s = 34            # 1 m = 34 mm
ox, oy = 5, 28
arrow(ax, (2, oy), (86, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, oy + 28), 'fixe', lw=0.8)
pts = []
for i in range(401):
    t = 2 * math.pi * i / 400
    pts.append((ox + s * a * (t - math.sin(t)), oy + s * a * (1 - math.cos(t))))
line(ax, pts, 'sujet', lw=1.3)
for t, lab, dx, dy in [(0, '(0 ; 0)', 4, -4.5), (math.pi, '(1,10 ; 0,70)', 0, 4.5), (2 * math.pi, '(2,20 ; 0)', -2, -4.5)]:
    px, py = ox + s * a * (t - math.sin(t)), oy + s * a * (1 - math.cos(t))
    disc(ax, px, py, 1.1, 'varie')
    text(ax, px + dx, py + dy, lab, 'varie', 's')
# t commande x et y
box(ax, 6, 3, 10, 9, 'varie', label='t', size='m')
box(ax, 34, 7, 22, 9, 'sujet', label='x = f(t)', size='s')
box(ax, 62, 7, 22, 9, 'sujet', label='y = g(t)', size='s')
arrow(ax, (16, 9), (34, 11), 'varie')
arrow(ax, (16, 6), (62, 9), 'varie', curve=0.15)
text(ax, 45, 20.5, 'x en m', 'fixe', 's') if False else None
save(fig, '40-086')
