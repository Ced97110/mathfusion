import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c = (20, 38)
a = math.radians(30)
P = (c[0] + 34 * math.cos(a), c[1] + 34 * math.sin(a))
line(ax, [(6, 38), (56, 38)], 'fixe', lw=0.6)
line(ax, [c, P], 'fixe', lw=1.0)
def pt(r, deg): return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))
def arc(r, a1, role):
    pts = [pt(r, a1 * j / 80) for j in range(81)]
    line(ax, pts, role, lw=1.2)
    sg = 1 if a1 > 0 else -1
    arrow(ax, pt(r, a1 - 4 * sg), pt(r, a1), role, lw=1.2)
arc(8, 30, 'resultat')
arc(13, 390, 'varie')
arc(18, -330, 'autre')
disc(ax, *P, 1.5, 'fixe')
text(ax, P[0], P[1] + 4.5, r'$P$ : 40 km', 'fixe', 's')
text(ax, 73, 40, '30° (gardé)', 'resultat', 's')
text(ax, 73, 32, '390° = 30° + 360°', 'varie', 's')
text(ax, 73, 24, '−330° = 30° − 360°', 'autre', 's')
text(ax, 44, 12, '(40 km, 30°) = (40 km, 390°)', 'encre', 's')
text(ax, 44, 4.5, '0° ≤ θ < 360° : garder 30°', 'resultat', 's')
save(fig, '39-037')
