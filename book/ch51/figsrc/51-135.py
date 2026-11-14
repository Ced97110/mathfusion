import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
items = [(3, 32, r'$\mathbb{Z}/7$', 'char $=7$', '7 fois 1 donne 0', 'sujet'),
         (45, 32, r'$\mathbb{Z}/6$', 'char $=6$', '6 fois 1 donne 0', 'sujet'),
         (3, 4, r'$\mathbb{Z}$', 'char $=0$', 'jamais 0', 'autre'),
         (45, 4, r'$\mathbb{Q}$', 'char $=0$', 'jamais 0', 'autre')]
for x, y, name, val, sub, role in items:
    box(ax, x, y, 40, 24, role)
    text(ax, x + 20, y + 19, name, role, 'l')
    text(ax, x + 20, y + 11, val, role, 'l', weight='bold')
    text(ax, x + 20, y + 4, sub, role, 's')
save(fig, '51-135')
