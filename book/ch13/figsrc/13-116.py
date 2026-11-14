import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ox, oy, c = 14, 10, 11
for a in range(6):
    for b in range(5):
        ax.plot([ox + a * c], [oy + b * c], 'o', ms=1.6, color=COL['fixe'], zorder=2)
arrow(ax, (ox - 3, oy), (ox + 5 * c + 4, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 3), (ox, oy + 4 * c + 4), 'fixe', lw=0.7)
for n, aend in [(2, 5), (1, 5), (0, 4), (-1, 3)]:
    a0 = max(n, 0)
    p = (ox + a0 * c, oy + (a0 - n) * c); q = (ox + aend * c, oy + (aend - n) * c)
    line(ax, [p, q], 'sujet', lw=1.2)
    text(ax, q[0] + 2.6, q[1] + 2.2, str(n).replace('-', '−'), 'sujet', 'm', weight='bold')
    disc(ax, p[0], p[1], 1.6, 'varie')
for n, lab in [(2, '(2, 0)'), (1, '(1, 0)'), (0, '(0, 0)')]:
    text(ax, ox + n * c, oy - 5, lab, 'varie', 's')
text(ax, ox - 7, oy + c, '(0, 1)', 'varie', 's')
arrow(ax, (80, 48), (80, 20), 'resultat', lw=1.2)
text(ax, 80, 52, 'plus petit', 'resultat', 's'); text(ax, 80, 15, 'plus grand', 'resultat', 's')
text(ax, 44, 72, r'$-1<0<1<2$', 'resultat', 'l', weight='bold')
text(ax, 44, 66.5, 'nombre = premier $-$ second', 'sujet', 's')
save(fig, '13-116')
