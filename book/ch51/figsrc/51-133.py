import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, 'cadran à 7 heures', 'fixe', 'm')
for i, (r, role, prod) in enumerate([(1, 'sujet', '7'), (3, 'autre', '21'), (5, 'autre', '35')]):
    y = 42 - 18 * i
    box(ax, 4, y, 18, 9, role, label=r'$r=%d$' % r)
    text(ax, 47, y + 4.5, r'$7\times%d=%s=0$' % (r, prod), role, 'm')
    box(ax, 72, y, 14, 9, 'resultat', label='0', size='l')
    if i < 2:
        arrow(ax, (13, y), (13, y - 9), 'varie')
text(ax, 50, 37.5, 'le test avec 1 suffit', 'varie', 's')
text(ax, 50, 19.5, 'il donne les autres', 'varie', 's')
save(fig, '51-133')
