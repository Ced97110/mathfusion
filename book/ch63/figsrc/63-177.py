import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# plan complexe : u = racine sixième de 5 fois i ; u^2 = -cbrt5 ; u^3 = -sqrt5 i  (échelle 11 mm par unité)
ox, oy, k = 36, 42, 11
rad = [5 ** (n / 6) for n in (1, 2, 3)]  # |u|, |u^2|, |u^3|
pos = [(ox, oy + k * rad[0]), (ox - k * rad[1], oy), (ox, oy - k * rad[2])]
arrow(ax, (ox - 30, oy), (ox + 18, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 33), (ox, oy + 22), 'fixe', lw=0.6)
for n, (x, y) in enumerate(pos):
    line(ax, [(ox, oy), (x, y)], 'fixe', lw=0.5, dash=True)
# spirale : multiplier par u tourne d'un quart de tour
th = [math.radians(90 + d) for d in range(0, 181, 3)]
line(ax, [(ox + k * 5 ** ((1 + (a - math.radians(90)) / math.radians(90)) / 6) * math.cos(a), oy + k * 5 ** ((1 + (a - math.radians(90)) / math.radians(90)) / 6) * math.sin(a)) for a in th], 'varie', lw=0.9)
disc(ax, pos[0][0], pos[0][1], 1.6, 'sujet'); disc(ax, pos[1][0], pos[1][1], 1.6, 'resultat'); disc(ax, pos[2][0], pos[2][1], 1.6, 'resultat')
text(ax, pos[0][0] + 2.5, pos[0][1] + 1.5, r'$u$', 'sujet', 'm', ha='left')
text(ax, pos[1][0] + 1, pos[1][1] + 3.5, r'$u^2$', 'resultat', 'm', ha='left')
text(ax, pos[2][0] + 2.5, pos[2][1] - 1.5, r'$u^3$', 'resultat', 'm', ha='left')
text(ax, 48, 76, r'$u = \sqrt[6]{5}\; i$', 'sujet', 'm', ha='left')
text(ax, 50, 62, r'$u^2 = -\sqrt[3]{5}$', 'resultat', 's', ha='left')
text(ax, 50, 52, r'$u^3 = -\sqrt{5}\, i$', 'resultat', 's', ha='left')
text(ax, 48, 24, r'$\sqrt{5}\,i\,/\sqrt[3]{5} = u$', 'varie', 's', ha='left')
text(ax, 44, 4, 'deux inclusions : les corps sont égaux', 'resultat', 's')
save(fig, '63-177')
