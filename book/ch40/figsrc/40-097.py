import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
a = 0.35
s = 35                     # 1 m = 35 mm
ox, oy = 8, 12
R = s * a                  # 12,25 mm
t = math.pi                # demi-tour
Cx, Cy = ox + s * a * t, oy + R
line(ax, [(2, oy), (86, oy)], 'fixe', lw=1.0)
# longueur OI posée sur le sol
line(ax, [(ox, oy), (Cx, oy)], 'varie', lw=2.0)
# roue
line(ax, [(Cx + R * math.cos(u), Cy + R * math.sin(u)) for u in [2 * math.pi * i / 200 for i in range(201)]], 'fixe', lw=1.0)
# arc IM qui a touché le sol : demi-cercle gauche de I (bas) à M (haut)
line(ax, [(Cx + R * math.cos(math.pi * 1.5 - u), Cy + R * math.sin(math.pi * 1.5 - u)) for u in [math.pi * i / 100 for i in range(101)]], 'varie', lw=2.0)
line(ax, [(Cx, Cy), (Cx, oy)], 'fixe', lw=0.8, dash=True)
line(ax, [(Cx, Cy), (Cx, Cy + R)], 'fixe', lw=0.8, dash=True)
disc(ax, Cx, Cy, 0.9, 'fixe')
disc(ax, ox, oy, 1.0, 'varie')
disc(ax, Cx, oy, 1.0, 'varie')
disc(ax, Cx, Cy + R, 1.1, 'varie')
text(ax, ox - 1, oy - 4, 'O', 'varie', 's')
text(ax, Cx, oy - 4, 'I', 'varie', 's')
text(ax, Cx + 3.3, Cy + R + 1.8, 'M', 'varie', 's')
text(ax, Cx + 3.8, Cy + 2, 'C', 'fixe', 's')
text(ax, (ox + Cx) / 2, oy - 4.5, 'OI = 1,10 m', 'varie', 's')
text(ax, Cx - R - 2.5, Cy + 3, 'arc IM', 'varie', 's', ha='right')
text(ax, Cx - R - 16, Cy + 1, '0,35 × π ≈ 1,10 m', 'varie', 's') if False else None
text(ax, 72, 40, 'C est en', 'fixe', 's') if False else None
text(ax, 72, 36, 'C = (1,10 ; 0,35)', 'encre', 's')
text(ax, 72, 30, 'a = 0,35 m', 'fixe', 's')
text(ax, 72, 24, 'OI = arc IM = a t', 'varie', 's')
save(fig, '40-097')
