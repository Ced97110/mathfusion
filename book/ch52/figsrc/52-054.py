import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'$k = 0$ : on calcule $q \times 0$', 'fixe', 's')
for i, q in enumerate([-2, 0, 5]):
    y = 36 - i * 12
    box(ax, 4, y, 16, 8, 'varie', label=r'$q = %d$' % q, size='s')
    arrow(ax, (20, y + 4), (56, 24), 'fixe')
box(ax, 56, 18, 28, 12, 'resultat', label='{0}', size='l')
text(ax, 70, 11, 'toujours 0', 'resultat', 's')
text(ax, 70, 35, 'idéal nul', 'sujet', 's')
save(fig, '52-054')
