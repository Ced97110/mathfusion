import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 14, 46, 60, 12, 'sujet', label=r'formule : $P = 2l + 2w$', size='l')
for cx, let, other in [(23, 'l', r'$P$, $w$'), (65, 'w', r'$P$, $l$')]:
    box(ax, cx - 20, 6, 40, 28, 'varie')
    text(ax, cx, 27, 'on cherche', 'varie', 's')
    text(ax, cx, 20, rf'inconnue : ${let}$', 'varie', 'l', weight='bold')
    text(ax, cx, 11, 'connues : ' + other, 'fixe', 's')
    arrow(ax, (cx + (cx - 44) * 0.3 + 0 if False else (30 if cx < 44 else 58), 46), (cx, 34.5), 'varie')
save(fig, '16-113')
