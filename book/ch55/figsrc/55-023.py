import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'fonction constante $a=2$', 'sujet', 'm')
for y, n, d in ((52, 'Ana', False), (36, 'Bob', False), (20, 'Chi', False), (4, 'nouvel élève', True)):
    box(ax, 4, y, 26, 10, 'fixe', label=n, size='s', dash=d)
    arrow(ax, (30, y + 5), (58, 33), 'sujet')
box(ax, 58, 26, 26, 14, 'resultat', label='2', size='l')
text(ax, 71, 21, 'toujours 2', 'resultat', 's')
save(fig, '55-023')
