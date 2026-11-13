import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
bx, bw = 2, 58
rows = [(66, 'sujet', '8x − 3y + 10 = 0'),
        (46, 'varie', '8r cos θ − 3r sin θ + 10 = 0'),
        (26, 'varie', 'r (8 cos θ − 3 sin θ) = −10'),
        (6, 'resultat', 'r = −10 / (8 cos θ − 3 sin θ)')]
for y, role, lab in rows:
    box(ax, bx, y, bw, 11, role, label=lab, size='s')
labs = ['x → r cos θ, y → r sin θ', 'r en facteur', 'diviser']
for i, lab in enumerate(labs):
    y = rows[i][0]
    arrow(ax, (10, y), (10, y - 9), 'varie')
    text(ax, 14, y - 4.5, lab, 'varie', 's', ha='left')
# la droite dans le plan, hors du pôle
s = 6.5
ox, oy = 76, 28
arrow(ax, (63, oy), (87, oy), 'fixe', lw=0.7)
arrow(ax, (ox, 20), (ox, 56), 'fixe', lw=0.7)
y0, y1 = -1.0, 4.0
line(ax, [(ox + s * (3 * y - 10) / 8, oy + s * y) for y in (y0, y1)], 'sujet', lw=1.4)
disc(ax, ox, oy, 1.1, 'fixe')
text(ax, ox + 3, oy - 3, 'O', 'fixe', 's')
text(ax, 75, 66, 'la droite ne passe', 'sujet', 's')
text(ax, 75, 61.5, 'pas par O', 'sujet', 's')
save(fig, '40-107')
