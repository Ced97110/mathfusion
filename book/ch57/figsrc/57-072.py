import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'trois situations, une lettre', 'fixe', 's')
for x, s in [(2, 'flèches du plan'), (31, "couples d'entiers"), (60, 'points du plan')]:
    box(ax, x, 38, 26, 9, 'varie', label=s, size='s')
    arrow(ax, (x + 13, 37.5), (44 + (x - 31) * 0.4, 27), 'fixe')
box(ax, 20, 10, 48, 16, 'sujet', label='$M$', size='l')
text(ax, 44, 4, 'on peut les additionner', 'sujet', 's')
save(fig, '57-072')
