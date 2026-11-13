import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
pitch = 6.9; x0 = 2.6
for i in range(12):
    x = x0 + i*pitch
    box(ax, x, 22, 6.2, 9, 'varie', fill=False, dash=True, r=0.5)
    box(ax, x + 0.6, 23.3, 5, 6.4, 'sujet', label=str(i), size='s', r=0.4, lw=0.6)
brace(ax, x0, x0 + 12*pitch - 0.7, 21, 'varie', label='12 classes de 1 élément')
text(ax, 44, 40, 'une classe = un seul nombre', 'varie', 's')
text(ax, 44, 4, r'$G/\{0\}$ garde les 12 éléments de $G$', 'resultat', 's')
save(fig, '47-198')
