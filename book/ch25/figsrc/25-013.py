import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

T = math.tan(math.radians(40))
fig, ax = canvas(100)
text(ax, 20, 91, 'tan 40°', 'sujet', 'l', weight='bold'); text(ax, 44, 91, '≈', 'fixe', 'l'); text(ax, 66, 91, '0,8391', 'resultat', 'l', weight='bold')
text(ax, 20, 81, 'tangente de 40°', 'sujet', 's'); text(ax, 44, 81, 'environ égal', 'fixe', 's')
text(ax, 66, 81, 'nombre attaché', 'resultat', 's'); text(ax, 66, 77.5, 'à l’angle', 'resultat', 's')
for x, r in [(20, 'sujet'), (44, 'fixe'), (66, 'resultat')]:
    arrow(ax, (x, 83.2), (x, 87.2), r, lw=0.7)
A = (10, 14); B = (50, 14); S = (50, 14 + 40 * T)
line(ax, [A, B], 'sujet', lw=1.6); line(ax, [B, S], 'varie', lw=1.6); line(ax, [A, S], 'fixe', dash=True)
line(ax, [(47, 14), (47, 17), (50, 17)], 'fixe', lw=0.7)
arc(ax, A, 9, 0, 40, 'sujet')
text(ax, 25, 17, '40°', 'sujet', 's'); text(ax, 30, 9, '20 m', 'sujet', 'm')
text(ax, 52, 32, 'hauteur ?', 'varie', 'm', ha='left')
text(ax, 71, 60, '20 × 0,8391', 'encre', 'm'); text(ax, 71, 54, '= 16,782', 'encre', 'm'); text(ax, 71, 47, '≈ 16,78 m', 'resultat', 'm', weight='bold')
save(fig, '25-013')
