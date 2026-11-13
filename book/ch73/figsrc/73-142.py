import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
ox, oy, k = 30, 30, 7
Pt = lambda x, y: (ox + k * x, oy + k * y)
line(ax, [Pt(-4, 0), Pt(5.8, 0)], 'varie', 1.6)
line(ax, [Pt(0, -3.5), Pt(0, 3.5)], 'fixe', 0.5)
text(ax, *Pt(5.6, 0.7), r'$B(0)$', 'varie', 's')
for a in (100, 135, 160):
    t = math.radians(a); line(ax, [(ox, oy), (ox + 22 * math.cos(t), oy + 22 * math.sin(t))], 'fixe', 0.6, dash=True)
text(ax, 14, 6, 'un miroir par angle', 'fixe', 's')
for (x, y), lab in [((3, 2), '(3, 2)'), ((5, 1), '(5, 1)')]:
    disc(ax, *Pt(x, y), 1.0, 'sujet'); disc(ax, *Pt(x, -y), 1.0, 'resultat')
    arrow(ax, Pt(x, y - 0.2), Pt(x, -y + 0.2), 'varie', 0.7)
text(ax, *Pt(2.0, 2.0), '(3, 2)', 'sujet', 's'); text(ax, *Pt(2.0, -2.0), '(3, −2)', 'resultat', 's')
text(ax, *Pt(5.9, 1.9), '(5, 1)', 'sujet', 's'); text(ax, *Pt(5.9, -1.9), '(5, −1)', 'resultat', 's')
save(fig, '73-142')
