import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
yb = 28
box(ax, 4, yb, 12, 10, 'sujet', label='4', size='l')
box(ax, 20, yb, 12, 10, 'varie', label='+', size='l')
text(ax, 38, yb + 5, '(', 'autre', 'xl'); text(ax, 70, yb + 5, ')', 'autre', 'xl')
box(ax, 42, yb, 10, 10, 'autre', label=r'$-$', size='l')
box(ax, 55, yb, 10, 10, 'autre', label='2', size='l')
for c, t, r in ((10, 'nombre', 'sujet'), (26, 'opération', 'varie'), (47, 'signe', 'autre'), (60, 'nombre', 'autre')):
    text(ax, c, yb - 4, t, r, 's')
brace(ax, 36, 72, yb - 8, 'autre', r'nombre négatif $-2$')
text(ax, 44, 46, 'quatre plus négatif deux', 'encre', 'm')
save(fig, '13-028')
