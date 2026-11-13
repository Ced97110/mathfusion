import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# haut : le cercle (voisin) tourne autour d'un centre fixe
cx, cy, R = 24, 76, 12
line(ax, [(cx + R * math.cos(u), cy + R * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'autre', lw=1.3)
disc(ax, cx, cy, 1.0, 'fixe')
line(ax, [(cx, cy), (cx + R * math.cos(0.9), cy + R * math.sin(0.9))], 'autre', lw=1.0)
disc(ax, cx + R * math.cos(0.9), cy + R * math.sin(0.9), 1.2, 'autre')
text(ax, 62, 86, 'cercle', 'autre', 'l')
text(ax, 62, 79.5, 'le centre est fixe', 'fixe', 's')
text(ax, 62, 71, 'x = 4 cos t', 'autre', 's')
text(ax, 62, 65.5, 'y = 4 sin t', 'autre', 's')
line(ax, [(2, 57), (86, 57)], 'fixe', lw=0.5, dash=True)
# bas : la cycloïde, le centre avance
a = 0.35
s = 34
ox, oy = 6, 8
X = lambda t: ox + s * a * (t - math.sin(t))
Y = lambda t: oy + s * a * (1 - math.cos(t))
line(ax, [(2, oy), (86, oy)], 'fixe', lw=0.8)
line(ax, [(X(2 * math.pi * i / 400), Y(2 * math.pi * i / 400)) for i in range(401)], 'sujet', lw=1.4)
r = s * a
t = math.pi / 2
Cx, Cy = ox + r * t, oy + r
line(ax, [(Cx + r * math.cos(u), Cy + r * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'fixe', lw=0.9)
disc(ax, Cx - r, Cy, 1.2, 'sujet')
line(ax, [(Cx, Cy), (Cx - r, Cy)], 'sujet', lw=1.0)
disc(ax, Cx, Cy, 0.9, 'fixe')
arrow(ax, (ox + r * t + 4, Cy), (ox + r * 2 * math.pi, Cy), 'varie', lw=1.1)
text(ax, 50, Cy - 3.8, 'le centre avance', 'varie', 's')
text(ax, 62, 50, 'cycloïde', 'sujet', 'l')
text(ax, 62, 43, 'x = at − a sin t', 'sujet', 's')
text(ax, 62, 37.5, 'y = a − a cos t', 'sujet', 's')
save(fig, '40-100')
