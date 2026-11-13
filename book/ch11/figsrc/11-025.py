import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
c, x0 = 4, 4
for r, (n, y) in enumerate([(2, 38), (5, 14)]):
    for i in range(3 * n):
        box(ax, x0 + i * c, y, c, 7, 'varie', lw=0.6, r=0.3)
    for p in range(n):
        box(ax, x0 + p * 3 * c - 0.3, y - 1.5, 3 * c + 0.6, 10, 'sujet', fill=False, lw=1.0, r=0.3)
    text(ax, x0, y + 13, f'{n} yards', 'sujet', 's', ha='left')
    text(ax, x0 + 3 * n * c + 4, y + 3.5, f'{3 * n} pieds', 'varie', 's', ha='left')
text(ax, 44, 51, '1 yard = 3 pieds', 'resultat', 'm', weight='bold')
text(ax, 44, 5, r'$6 \div 2 = 15 \div 5 = 3$', 'resultat', 'm')
save(fig, '11-025')
