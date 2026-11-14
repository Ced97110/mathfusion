import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cols = [(3, 'sujet', '3', r'$3^7$', '3', r'$a=3$'), (47, 'autre', '14', r'$14^7$', '0', r'$a=14$')]
for x, r, a, ap, rem, ttl in cols:
    text(ax, x + 19, 54, ttl, r, 'm', weight='bold')
    box(ax, x, 36, 17, 10, r, label=a, size='m')
    box(ax, x + 21, 36, 17, 10, r, label=ap, size='m')
    box(ax, x, 12, 17, 10, 'resultat', label=f'reste {rem}', size='s')
    box(ax, x + 21, 12, 17, 10, 'resultat', label=f'reste {rem}', size='s')
    text(ax, x + 19, 17, '=', 'resultat', 'xl')
    arrow(ax, (x + 8.5, 35.5), (x + 8.5, 22.5), 'fixe')
    arrow(ax, (x + 29.5, 35.5), (x + 29.5, 22.5), 'fixe')
save(fig, '47-197')
