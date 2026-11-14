import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

assert 2 * 3 * 5 == 30 and 2 * 3 * 0 == 0
fig, ax = canvas(66)
xs = [8, 28, 48]
for x, v in zip(xs, [2, 3, 5]):
    disc(ax, x, 56, 4.6, 'sujet', label='%d' % v, size='m')
text(ax, 18, 56, '×', 'fixe', 'l'); text(ax, 38, 56, '×', 'fixe', 'l')
text(ax, 58, 56, '=', 'fixe', 'l')
box(ax, 64, 50, 20, 12, 'sujet', label=r'$a_3=30$', size='s', weight='bold')
text(ax, 44, 66, r'$a_3=r_1r_2r_3$', 'sujet', 's') if False else None
text(ax, 44, 41, r'dans $x^3-a_1x^2+a_2x-a_3$ :', 'fixe', 's')
box(ax, 26, 24, 36, 11, 'varie', label=r'$-a_3=-30$', size='s', weight='bold')
text(ax, 44, 17, 'le terme sans x', 'varie', 's')
text(ax, 44, 8, 'racine 0 : 0 × 3 × 5 = 0, a₃ = 0', 'fixe', 's')
save(fig, '65-050')
