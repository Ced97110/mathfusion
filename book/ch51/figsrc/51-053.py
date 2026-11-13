import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(64)
text(ax, 22, 59, 'cadran à 7 heures', 'sujet', 'm'); text(ax, 66, 59, 'les entiers', 'fixe', 'm')
cx, cy, R = 22, 36, 14.5
pts = [(cx + R * math.cos(math.radians(90 - i * 360 / 7)), cy + R * math.sin(math.radians(90 - i * 360 / 7))) for i in range(7)]
for i, (px, py) in enumerate(pts):
    disc(ax, px, py, 3.4, 'resultat' if i == 0 else 'sujet', label=str(i), size='m')
for i in range(7):
    p, q = pts[i], pts[(i + 1) % 7]
    arrow(ax, (p[0] + (q[0] - p[0]) * .3, p[1] + (q[1] - p[1]) * .3), (p[0] + (q[0] - p[0]) * .7, p[1] + (q[1] - p[1]) * .7), 'varie')
f = numberline(ax, 50, 80, 34, 0, 4, labels=False, role='fixe', arrow_right=True)
disc(ax, f(0), 34, 3.0, 'resultat', label='0', size='m')
for v in range(4): arrow(ax, (f(v) + 1.5, 36), (f(v + 1) - 1.5, 36), 'varie', curve=-0.5)
text(ax, 22, 11, r'7 pas de +1 : retour à 0', 'sujet', 's'); text(ax, 22, 6, r'$\mathrm{char}=7$', 'sujet', 'l')
text(ax, 66, 11, 'jamais de retour à 0', 'fixe', 's'); text(ax, 66, 6, r'$\mathrm{char}=0$', 'fixe', 'l')
save(fig, '51-053')
