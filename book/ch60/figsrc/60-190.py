import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'A réelle, polynôme λ² + 1', 'encre', 's')
for sgn in (-1, 1):
    xx = 22 + sgn * 11
    line(ax, [(xx - sgn * 1.5, 56), (xx, 56), (xx, 40), (xx - sgn * 1.5, 40)], 'sujet', lw=0.9)
for (dx, dy, s) in ((-5, 4, '0'), (5, 4, '−1'), (-5, -4, '1'), (5, -4, '0')):
    text(ax, 22 + dx, 48 + dy, s, 'sujet', 'l')
text(ax, 22, 33, 'pas de forme de Jordan sur ℝ', 'limite', 's')
# graphe de lambda^2 + 1
ox, oy, sx, sy = 62, 26, 8, 3.2
arrow(ax, (ox - 20, oy), (ox + 22, oy), 'fixe', lw=0.8)
text(ax, ox + 22, oy - 3, 'λ', 'fixe', 's')
pts = [(ox + x * sx, oy + sy * (x * x + 1)) for x in [i / 20 * 4 - 2 for i in range(21)]]
line(ax, pts, 'sujet', lw=1.3)
text(ax, ox, oy + 11.5, 'λ² + 1', 'sujet', 's')
text(ax, 64, 19, 'aucune racine réelle', 'limite', 's')
text(ax, 44, 8, 'sur ℂ : racines i et −i', 'resultat', 's')
save(fig, '60-190')
