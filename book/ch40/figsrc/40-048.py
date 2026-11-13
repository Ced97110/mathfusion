import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# r = a, a = 3 : tout angle donne un point à 3 du pôle -> cercle de centre O et de rayon 3 ; x² + y² = 9
fig, ax = canvas(76)
o = (30, 36); u = 8.5
def pt(r, deg): return (o[0] + u * r * math.cos(math.radians(deg)), o[1] + u * r * math.sin(math.radians(deg)))
line(ax, [pt(3, a) for a in range(0, 361, 3)], 'sujet', lw=1.5)
arrow(ax, (o[0] - 30, o[1]), (o[0] + 34, o[1]), 'fixe', lw=0.8)
for deg, role in [(0, 'varie'), (90, 'varie'), (200, 'varie')]:
    q = pt(3, deg)
    line(ax, [o, q], 'varie', lw=1.1)
    disc(ax, q[0], q[1], 1.4, 'varie')
disc(ax, o[0], o[1], 0.9, 'encre')
text(ax, o[0] + 3, o[1] - 3.5, 'O', 'encre', 's')
text(ax, pt(3, 0)[0] - 1, pt(3, 0)[1] + 5, r'0°', 'varie', 's')
text(ax, pt(3, 90)[0] + 6, pt(3, 90)[1] + 1, r'90°', 'varie', 's')
text(ax, pt(3, 200)[0] + 4, pt(3, 200)[1] - 5, r'200°', 'varie', 's')
text(ax, o[0] + 6, o[1] + 9, '3', 'sujet', 's')
text(ax, 44, 72, r'$r = a$, avec $a = 3$', 'sujet', 'm')
text(ax, 72, 56, '1. choisir $\\theta$', 'varie', 's')
text(ax, 72, 51, '2. avancer de 3', 'varie', 's')
text(ax, 72, 28, '$x^2 + y^2 = a^2$', 'sujet', 's')
text(ax, 72, 23, '$x^2 + y^2 = 9$', 'sujet', 's')
text(ax, 72, 17, 'Pythagore', 'fixe', 's')
save(fig, '40-048')
