import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for cx, s in zip([16, 44, 72], ['i', 'j', 'k']):
    box(ax, cx - 12, 36, 24, 12, 'sujet', label=rf'${s}^2={s}\times {s}$')
    arrow(ax, (cx, 36), (cx, 27.8), 'varie')
    box(ax, cx - 8, 16, 16, 11, 'resultat', label=r'$-1$', size='l')
brace(ax, 6, 82, 13, 'resultat', label=r'toujours $-1$')
save(fig, '51-174')
