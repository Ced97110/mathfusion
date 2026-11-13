import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
for x0, role, lab in ((6, 'sujet', 'S'), (60, 'autre', 'T')):
    box(ax, x0, 50, 22, 20, role)
    text(ax, x0 + 11, 74, r'$%s$' % lab, role, 'm')
    for k in range(3): disc(ax, x0 + 11, 55 + 5 * k, 1.6, role)
for k in range(3): arrow(ax, (30, 55 + 5 * k), (58, 55 + 5 * k), 'varie')
text(ax, 44, 79, r'une bijection de $S$ sur $T$', 'varie', 's')
arrow(ax, (44, 46), (44, 38), 'varie'); text(ax, 48, 42, 's’écrit', 'varie', 's', ha='left')
text(ax, 44, 28, r'$|S| = |T|$', 'resultat', 'xl')
text(ax, 44, 16, r'$|S|$ : nombre d’éléments de $S$', 'sujet', 's')
text(ax, 44, 8, r'$|T|$ : nombre d’éléments de $T$', 'autre', 's')
save(fig, '43-103')
