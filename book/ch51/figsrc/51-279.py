import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'une équation à deux inconnues', 'fixe', 's')
box(ax, 3, 46, 14, 12, 'sujet', label='$2$', size='l')
text(ax, 24, 52, '$x\\ +$', 'encre', 'l')
box(ax, 34, 46, 14, 12, 'sujet', label='$3$', size='l')
text(ax, 55, 52, '$y$', 'encre', 'l')
text(ax, 75, 52, 'coefficients', 'sujet', 's')
text(ax, 44, 34, 'ils peuvent venir de :', 'varie', 's')
for x, lab in ((4, '$\\mathbb{R}$'), (32, '$\\mathbb{Z}$'), (60, 'cadran')):
    box(ax, x, 12, 24, 14, 'varie', label=lab, size='m')
save(fig, '51-279')
