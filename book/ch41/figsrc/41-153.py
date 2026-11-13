import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 3.6
# v = deux copies de u mises bout à bout
o = (12, 6)
arrow(ax, o, (o[0] + 3 * s, o[1] + 4 * s), 'sujet', lw=1.6)
arrow(ax, (o[0] + 3 * s + 3, o[1] + 4 * s), (o[0] + 6 * s + 3, o[1] + 8 * s), 'sujet', lw=1.6)
arrow(ax, (o[0] - 3, o[1]), (o[0] + 6 * s - 3, o[1] + 8 * s), 'autre', lw=1.2)
text(ax, 17, 62, r'$u=\langle 3,\ 4\rangle$', 'sujet', 's')
text(ax, 17, 56, r'$v=\langle 6,\ 8\rangle$', 'autre', 's')
text(ax, 17, 50, r'$v=2u$', 'autre', 's')
box(ax, 42, 46, 44, 24, 'resultat')
text(ax, 64, 64, r'$3\times 6+4\times 8$', 'resultat', 's')
text(ax, 64, 57, r'$=18+32=50$', 'resultat', 's')
box(ax, 42, 12, 44, 24, 'fixe')
text(ax, 64, 30, r'$\|u\|=5,\ \|v\|=10$', 'fixe', 's')
text(ax, 64, 23, r'$5\times 10=50$', 'fixe', 's')
arrow(ax, (64, 46), (64, 36), 'resultat', lw=0.9)
save(fig, '41-153')
