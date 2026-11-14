import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
for cx, b, p in [(16, '2', r'$2\times2\times2$'), (44, '5', r'$5\times5\times5$'), (72, '9', r'$9\times9\times9$')]:
    text(ax, cx - 1.5, 44, b, 'sujet', 'xl', weight='bold'); text(ax, cx + 3, 48, '3', 'fixe', 'l')
    text(ax, cx, 35, p, 'fixe', 's')
    arrow(ax, (44 + (cx - 44) * 0.55, 20), (cx, 31.5), 'sujet')
box(ax, 32, 6, 24, 13, 'sujet', label=r'$a^{3}$', size='l')
text(ax, 71, 12, 'a : nombre répété', 'sujet', 's')
text(ax, 18, 12, '3 ne change pas', 'fixe', 's')
save(fig, '14-015')
