import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
a = 0.35
kt, kx = 10.2, 18          # 1 rad = 10,2 mm ; 1 m = 18 mm
ox, oy = 16, 14
arrow(ax, (ox - 3, oy), (ox + 2 * math.pi * kt + 6, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, oy + 2.35 * kx), 'fixe', lw=0.8)
pts = [(ox + kt * t, oy + kx * a * (t - math.sin(t))) for t in [2 * math.pi * i / 400 for i in range(401)]]
line(ax, pts, 'sujet', lw=1.4)
text(ax, ox + 6, oy + 2.35 * kx + 3, 'x en m', 'fixe', 's')
text(ax, 30, 50, 'x = f(t)', 'sujet', 'l')
text(ax, 30, 44, 'résultat de la règle f en t', 'sujet', 's')
for t, lab, v in [(0, 'départ', '0'), (math.pi, 'demi-tour', '1,10'), (2 * math.pi, 'tour', '2,20')]:
    px = ox + kt * t
    py = oy + kx * a * (t - math.sin(t))
    ax.plot([px, px], [oy - 1.2, oy + 1.2], color=COL['fixe'], lw=0.8)
    text(ax, px, oy - 4.5, lab, 'varie', 's')
    disc(ax, px, py, 1.1, 'varie')
    if t > 0:
        text(ax, ox - 5.2, py, v, 'resultat', 's')
        line(ax, [(ox, py), (px, py)], 'resultat', lw=0.8, dash=True)
        line(ax, [(px, oy), (px, py)], 'varie', lw=0.8, dash=True)
text(ax, ox + 10, oy + 3.5, '0', 'resultat', 's') if False else None
save(fig, '40-089')
