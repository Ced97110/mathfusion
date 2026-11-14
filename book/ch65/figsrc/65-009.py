import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
Y = 38
px = lambda v: 44 + 17 * v
line(ax, [(px(-2.3), Y), (px(2.3), Y)], 'fixe')
roots = [(1, 1.53, '1,53'), (2, 0.35, '0,35'), (3, -1.88, '−1,88')]
for k, v, lab in roots:
    disc(ax, px(v), Y, 3.3, 'sujet', label=f'$r_{k}$', size='s')
    text(ax, px(v), Y - 6.2, lab, 'sujet', 's')
r = 3.3
# r1 -> r2 et r2 -> r3 au-dessus (vers la gauche : courbure positive)
arrow(ax, (px(1.53) - 1, Y + r), (px(0.35) + 1, Y + r), 'varie', curve=0.6)
arrow(ax, (px(0.35) - 1, Y + r), (px(-1.88) + 1, Y + r), 'varie', curve=0.4)
# r3 -> r1 en dessous (vers la droite : courbure positive)
arrow(ax, (px(-1.88), Y - r - 5.5), (px(1.53), Y - r - 5.5), 'varie', curve=0.3)
text(ax, px(0.94), Y + 11, r'$\sigma$', 'varie', 'l')
text(ax, px(-0.75), Y + 11.5, r'$\sigma$', 'varie', 'l')
text(ax, px(-0.17), Y - 23, r'$\sigma$', 'varie', 'l')
text(ax, 44, 3, 'trois flèches : un circuit fermé', 'varie', 's')
save(fig, '65-009')
