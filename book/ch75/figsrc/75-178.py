import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 17, 56, 'trois groupes', 'sujet', 'm'); text(ax, 65, 56, 'trois algèbres de Lie', 'autre', 'm')
for i, n in enumerate(['$Sp$', '$O$', '$U$']):
    y = 36 - i*16
    box(ax, 6, y, 22, 11, 'sujet', label=n, size='l')
    box(ax, 44, y, 38, 11, 'autre', label='algèbre de Lie de ' + n, size='s')
    arrow(ax, (28.5, y+5.5), (43.5, y+5.5), 'varie')
save(fig, '75-178')
