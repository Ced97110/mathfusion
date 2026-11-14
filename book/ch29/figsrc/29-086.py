import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, R = 8, 38, 58
poly(ax, [(cx, cy)] + arcp(cx, cy, R, -6, 6, 10), 'fixe')
line(ax, arcp(cx, cy, R, -6, 6, 10), 'varie', lw=1.8)
line(ax, [(cx, cy), (cx + R, cy)], 'sujet', lw=1.2)
text(ax, 36, 43.5, 'r = 500 m', 'sujet', 's')
text(ax, 24, 33.5, 'angle 12°', 'fixe', 's')
text(ax, 70, 38, 's ≈ 104,7 m', 'varie', 's', ha='left')
xs = [3, 31.5, 60]
labs = ['12° ≈ 0,2094 rad', '500 × 0,2094', '≈ 104,7 m']
roles = ['varie', 'sujet', 'resultat']
caps = ['en radians', 's = r × θ', "longueur de l'arc"]
for i in range(3):
    box(ax, xs[i], 12, 25, 10, roles[i], label=labs[i], size='s')
    text(ax, xs[i] + 12.5, 7.5, caps[i], roles[i], 's')
for i in range(2):
    arrow(ax, (xs[i] + 25.2, 17), (xs[i + 1] - 0.2, 17), 'encre')
save(fig, '29-086')
