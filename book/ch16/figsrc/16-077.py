import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$4x-7=9$', 'encre', 'l')
for cx, role, lab in ((14, 'sujet', r'$x$'), (44, 'fixe', r'$4x$'), (74, 'resultat', '9')):
    box(ax, cx - 9, 21, 18, 10, role, label=lab, size='l')
arrow(ax, (24, 26), (34, 26), 'varie'); arrow(ax, (54, 26), (64, 26), 'varie')
text(ax, 29, 33, '× 4', 'varie', 'm'); text(ax, 59, 33, '− 7', 'varie', 'm')
text(ax, 29, 14, 'opération 1', 'fixe', 's'); text(ax, 59, 14, 'opération 2', 'fixe', 's')
save(fig, '16-077')
