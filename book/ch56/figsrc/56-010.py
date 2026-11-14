import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 18, 33, 9
s5 = 5 ** 0.5
for a in range(-1, 7):
    for b in (-1, 0, 1):
        if (a, b) in ((2, 0), (3, 0), (6, 0), (1, 1), (1, -1), (0, 0)):
            continue
        disc(ax, ox + a * u, oy + b * s5 * u, 0.7, 'fixe')
disc(ax, ox, oy, 2 ** 0.5 * u, 'limite', fill=False, lw=1.0)
disc(ax, ox, oy, 3 ** 0.5 * u, 'limite', fill=False, lw=1.0)
# distances de 0 à 2 et à 1 + √−5
line(ax, [(ox, oy), (ox + 2 * u, oy)], 'sujet', lw=1.2)
line(ax, [(ox, oy), (ox + u, oy + s5 * u)], 'autre', lw=1.2)
disc(ax, ox, oy, 1.4, 'encre')
text(ax, ox - 1, oy - 4, '0', 'encre', 's')
for a, role, lab in [(2, 'sujet', '2 : norme 4'), (3, 'sujet', '3 : norme 9'), (6, 'resultat', '6')]:
    disc(ax, ox + a * u, oy, 1.5, role)
text(ax, ox + 2 * u, oy - 4.5, '2 : norme 4', 'sujet', 's')
text(ax, ox + 3.6 * u, oy + 4.5, '3 : norme 9', 'sujet', 's')
text(ax, ox + 6 * u, oy - 4.5, '6', 'resultat', 's')
disc(ax, ox + u, oy + s5 * u, 1.5, 'autre')
disc(ax, ox + u, oy - s5 * u, 1.5, 'autre')
text(ax, ox + u + 10, oy + s5 * u + 4, '1 + √−5 : norme 6', 'autre', 's')
text(ax, ox + u + 10, oy - s5 * u - 4, '1 − √−5 : norme 6', 'autre', 's')
text(ax, ox + 4.7 * u, oy + 13, 'norme 3', 'limite', 's')
line(ax, [(ox + 3.7 * u, oy + 13), (ox + 8.6, oy + 13)], 'limite', lw=0.5)
text(ax, ox + 4.7 * u, oy - 9.5, 'norme 2', 'limite', 's')
line(ax, [(ox + 3.7 * u, oy - 9.5), (ox + 9, oy - 9)], 'limite', lw=0.5)
save(fig, '56-010')
