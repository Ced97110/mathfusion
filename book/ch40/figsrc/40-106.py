import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
s = 4.5
ox, oy = 30, 26
Cx, Cy = ox + 4 * s, oy + 4.5 * s
R = math.sqrt(36.25)
arrow(ax, (14, oy), (86, oy), 'fixe', lw=0.7)
line(ax, [(Cx + R * s * math.cos(t), Cy + R * s * math.sin(t)) for t in [2 * math.pi * i / 400 for i in range(401)]], 'sujet', lw=1.4)
th0 = math.atan2(8, -9)                    # 138,37° : 8 cos θ = −9 sin θ
dx, dy = math.cos(th0), math.sin(th0)
line(ax, [(ox - 8 * dx, oy - 8 * dy), (ox + 31 * dx, oy + 31 * dy)], 'varie', lw=1.6)
line(ax, [(ox + 9 * math.cos(a), oy + 9 * math.sin(a)) for a in [th0 * i / 60 for i in range(61)]], 'varie', lw=0.9)
disc(ax, ox, oy, 1.3, 'resultat')
text(ax, ox - 3, oy - 3.4, 'O', 'resultat', 's')
text(ax, 46, 32, 'θ₀ ≈ 138,4°', 'varie', 's')
text(ax, 6, 60, 'le long de ce rayon :', 'varie', 's', ha='left')
text(ax, 6, 55.5, 'r = 0', 'varie', 's', ha='left')
text(ax, 44, 16, '8 cos θ₀ ≈ −5,98', 'encre', 's')
text(ax, 44, 11, '9 sin θ₀ ≈ +5,98', 'encre', 's')
text(ax, 44, 5.5, 'somme = 0, donc r = 0', 'resultat', 's')
text(ax, 2, 80, 'r = 8 cos θ + 9 sin θ', 'encre', 'm', ha='left')
save(fig, '40-106')
