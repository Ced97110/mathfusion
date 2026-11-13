import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, s = 10, 12, 7.3   # a = 1 ; 1 unité = 7,3 mm

# axes
arrow(ax, (3, oy), (87, oy), 'fixe', lw=0.8)
arrow(ax, (ox, 4), (ox, 30), 'fixe', lw=0.8)
# droite y = a
line(ax, [(ox - 3, oy + s), (86, oy + s)], 'resultat', lw=1.0, dash=True)
text(ax, 22, oy + s + 3.2, 'y = a', 'resultat', 's')
# spirale r = a/θ de θ = 0,1 à π (x = cos θ/θ, y = sin θ/θ)
pts = []
n = 600
for i in range(n + 1):
    t = 0.1 + (math.pi - 0.1) * i / n
    pts.append((ox + s * math.cos(t) / t, oy + s * math.sin(t) / t))
line(ax, pts, 'sujet', lw=1.3)
px, py = ox + s * math.cos(0.1) / 0.1, oy + s * math.sin(0.1) / 0.1
disc(ax, px, py, 1.0, 'varie')
text(ax, 63, oy + 22, 'θ = 0,1 : y ≈ 0,998', 'varie', 's')
arrow(ax, (66, oy + 19.5), (px - 1, py + 1.2), 'varie', lw=0.7)
text(ax, ox - 3, oy - 3, 'O', 'fixe', 's')
text(ax, 4, 46, 'y = r sin θ = a sin θ / θ', 'encre', 'm', ha='left')
text(ax, 4, 39.5, 'sin θ ≈ θ  donc  y ≈ a', 'resultat', 'm', ha='left')
save(fig, '40-083')
