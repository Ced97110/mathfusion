import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
k = 0.01                                    # mm par mètre
g = 20.0
box(ax, 2, 66, 84, 10, 'sujet', label=r'$h = d\,\sin\alpha\,\sin\beta\,/\,\sin(\beta-\alpha)$', size='s')
# base 1 000 m -> h 1 976 m ; base 2 000 m -> h 3 951 m
for x0, d, h, dl, hl in [(8, 1000, 1975.55, 'd = 1 000 m', 'h ≈ 1 976 m'), (46, 2000, 3951.1, 'd = 2 000 m', 'h ≈ 3 951 m')]:
    box(ax, x0, g, 7, h * k, 'resultat')
    text(ax, x0 + 3.5, g + h * k + 3, hl, 'resultat', 's', weight='bold')
    box(ax, x0, g - 8, d * k, 4, 'fixe')
    text(ax, x0 + d * k / 2 + 2, g - 12, dl, 'fixe', 's', weight='bold')
arrow(ax, (20, 38), (42, 38), 'varie', curve=-0.3)
text(ax, 31, 44.5, '× 2', 'varie', 'm', weight='bold')
text(ax, 31, 34, 'mêmes angles', 'fixe', 's')
save(fig, '38-034')
