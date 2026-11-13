import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 21, 46, 'sans départ fixé', 'limite', 's'); text(ax, 66, 46, 'départ fixé', 'resultat', 's')
for sx, sy in [(4, 8), (14, 26), (24, 10)]:
    disc(ax, sx, sy, 1.2, 'fixe')
    arrow(ax, (sx + 1, sy), (sx + 12, sy), 'varie'); arrow(ax, (sx + 12, sy), (sx + 12, sy + 8), 'varie'); disc(ax, sx + 12, sy + 8, 1.4, 'limite')
text(ax, 21, 2.5, '3 arrivées différentes', 'limite', 's')
ox, oy = 52, 12
disc(ax, ox, oy, 1.4, 'sujet'); text(ax, ox - 3, oy - 3.5, r'$O$', 'sujet', 'm')
arrow(ax, (ox + 1, oy), (ox + 20, oy), 'varie'); arrow(ax, (ox + 20, oy), (ox + 20, oy + 13), 'varie'); disc(ax, ox + 20, oy + 13, 1.6, 'resultat')
text(ax, 66, 2.5, 'une seule arrivée', 'resultat', 's')
line(ax, [(44, 6), (44, 44)], 'fixe', dash=True)
save(fig, '19-016')
