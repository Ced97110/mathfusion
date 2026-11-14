import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
a = 0.35
kt, ky = 10.2, 40          # 1 rad = 10,2 mm ; 1 m = 40 mm
ox, oy = 16, 12
arrow(ax, (ox - 3, oy), (ox + 2 * math.pi * kt + 6, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, oy + 36), 'fixe', lw=0.8)
pts = [(ox + kt * t, oy + ky * a * (1 - math.cos(t))) for t in [2 * math.pi * i / 400 for i in range(401)]]
line(ax, pts, 'sujet', lw=1.4)
text(ax, ox + 6, oy + 39, 'y en m', 'fixe', 's')
text(ax, 72, 46, 'y = g(t)', 'sujet', 'l')
text(ax, 72, 40.5, 'règle g, autre que f', 'sujet', 's')
for t, lab, v in [(0, 'départ', '0'), (math.pi, 'demi-tour', '0,70'), (2 * math.pi, 'tour', '0')]:
    px = ox + kt * t
    py = oy + ky * a * (1 - math.cos(t))
    ax.plot([px, px], [oy - 1.2, oy + 1.2], color=COL['fixe'], lw=0.8)
    text(ax, px, oy - 4.5, lab, 'varie', 's')
    disc(ax, px, py, 1.1, 'varie')
    text(ax, ox - 5.2 if t == math.pi else px, py + (0 if t == math.pi else 4.5), v, 'resultat', 's')
    if t == math.pi:
        line(ax, [(ox, py), (px, py)], 'resultat', lw=0.8, dash=True)
        line(ax, [(px, oy), (px, py)], 'varie', lw=0.8, dash=True)
save(fig, '40-090')
