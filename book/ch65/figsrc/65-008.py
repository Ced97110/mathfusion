import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
items = [('d’abord', 'calculer le groupe $G_f$'),
         ('ensuite', 'coefficients en lettres : $S_n$'),
         ('enfin', 'coefficients entiers : $S_n$ aussi')]
y0 = 66
for k, (a, b) in enumerate(items):
    y = y0 - k * 22
    box(ax, 18, y, 68, 14, 'sujet', label=b, size='s')
    text(ax, 9, y + 7, a, 'varie', 's')
    if k < 2:
        arrow(ax, (52, y), (52, y - 8), 'varie')
arrow(ax, (52, 22), (52, 14), 'varie')
box(ax, 18, 2, 68, 12, 'varie', label='au degré 5, une formule ?', size='s', dash=True)
save(fig, '65-008')
