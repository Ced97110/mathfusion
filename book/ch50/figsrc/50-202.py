import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 23, 63, 'ℤ/4ℤ', 'sujet', 'l', weight='bold'); text(ax, 67, 63, 'ℤ/2ℤ × ℤ/2ℤ', 'autre', 'l', weight='bold')
text(ax, 23, 57, 'rotations du carré', 'fixe', 's'); text(ax, 67, 57, r'sous-groupe de $A_4$', 'fixe', 's')
s = 8.0; cxs = [7 + 10.5 * i for i in range(4)]
corner = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # marker after 0, 1/4, 1/2, 3/4 turn (counterclockwise)
for cx, lab, (mx, my) in zip(cxs, ['$e$', '1/4', '1/2', '3/4'], corner):
    cy = 40
    poly(ax, [(cx - s / 2, cy - s / 2), (cx + s / 2, cy - s / 2), (cx + s / 2, cy + s / 2), (cx - s / 2, cy + s / 2)], 'sujet')
    disc(ax, cx + mx * 2.4, cy + my * 2.4, 1.2, 'varie')
    text(ax, cx, 31, lab, 'encre', 's')
text(ax, 23, 18, '4 quarts de tour : retour', 'sujet', 's')
e = (67, 46); xs = [52, 67, 82]
disc(ax, *e, 2.0, 'fixe'); text(ax, 61.5, 46, r'$e$', 'encre', 's')
for x in xs:
    disc(ax, x, 28, 2.0, 'autre')
    L = math.hypot(x - e[0], 28 - e[1]); u = ((x - e[0]) / L, (28 - e[1]) / L)
    arrow(ax, (e[0] + u[0] * 3, e[1] + u[1] * 3), (x - u[0] * 3, 28 - u[1] * 3), 'varie', both=True)
text(ax, 67, 18, 'les 3 autres : ordre 2', 'autre', 's')
save(fig, '50-202')
