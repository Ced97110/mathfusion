import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

R = [1, 2, 3]
fig, ax = canvas(76)
text(ax, 44, 72, r'$s_k=r_1^k+r_2^k+r_3^k$', 'sujet', 'l', weight='bold')
text(ax, 15, 64, r'$r_1^k$', 'fixe', 's'); text(ax, 31, 64, r'$r_2^k$', 'fixe', 's'); text(ax, 47, 64, r'$r_3^k$', 'fixe', 's')
for k in (1, 2, 3):
    y = 58 - 17 * k + 8
    tot = 0
    for i, r in enumerate(R):
        v = r ** k; tot += v
        box(ax, 8 + 16 * i, y, 14, 10, 'sujet', label='%d' % v, size='s')
        if i < 2:
            text(ax, 8 + 16 * i + 15, y + 5, '+', 'fixe', 'm')
    assert tot == [6, 14, 36][k - 1]
    arrow(ax, (57, y + 5), (62, y + 5), 'fixe', lw=0.8)
    box(ax, 63, y, 22, 10, 'resultat', label=r'$s_%d=%d$' % (k, tot), size='s', weight='bold')
text(ax, 44, 5, 'une somme par exposant k', 'fixe', 's')
save(fig, '65-052')
