import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 20                    # 1 unité = 20 mm
ox, oy = 9, 32
arrow(ax, (3, oy), (56, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 29), (ox, oy + 29), 'fixe', lw=0.7)
pts = []
for i in range(361):
    t = 2 * math.pi * i / 360
    r = 1 + math.cos(t)
    pts.append((ox + s * r * math.cos(t), oy + s * r * math.sin(t)))
line(ax, pts, 'sujet', lw=1.3)
th = math.pi / 3
r = 1.5
px, py = ox + s * r * math.cos(th), oy + s * r * math.sin(th)   # (0,75 ; 1,30)
line(ax, [(ox, oy), (px, py)], 'varie', lw=1.1)
line(ax, [(px, oy), (px, py)], 'resultat', lw=1.0, dash=True)
line(ax, [(ox, oy), (px, oy)], 'resultat', lw=1.0, dash=True)
disc(ax, px, py, 1.2, 'sujet')
line(ax, [(ox + 6 * math.cos(a), oy + 6 * math.sin(a)) for a in [th * i / 20 for i in range(21)]], 'varie', lw=0.9)
text(ax, ox + 9.5, oy + 3.4, 'θ', 'varie', 's')
text(ax, ox + 6, oy + 14.5, 'r', 'varie', 'm')
text(ax, px, oy - 3.2, 'x', 'resultat', 's')
text(ax, px + 3.2, (oy + py) / 2 - 2, 'y', 'resultat', 's')
# colonne de droite
text(ax, 71, 56, 'r = f(θ) = 1 + cos θ', 'sujet', 's')
text(ax, 71, 47, 'θ = 60° : r = 1,5', 'varie', 's')
text(ax, 71, 38, 'x = f(θ) cos θ', 'resultat', 's')
text(ax, 71, 32, '= 1,5 × 0,5 = 0,75', 'resultat', 's')
text(ax, 71, 23, 'y = f(θ) sin θ', 'resultat', 's')
text(ax, 71, 17, '= 1,5 × 0,866 ≈ 1,30', 'resultat', 's')
text(ax, 71, 7, 'paramètre : θ', 'varie', 's')
save(fig, '40-095')
