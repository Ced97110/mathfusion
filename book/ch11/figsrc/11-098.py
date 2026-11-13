import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 24, 40, 40, 12, 'sujet', label=r'$C$ = $\pi$ × $d$', size='l')
text(ax, 44, 57, 'formule : une lettre, $d$', 'sujet', 's')
for cx, v, calc in [(22, '7', '3,14 × 7'), (66, '10', '3,14 × 10')]:
    arrow(ax, (cx + (6 if cx < 44 else -6), 39), (cx, 27), 'varie')
    text(ax, cx + (-1 if cx < 44 else 1) * 11, 33, f'$d$ = {v}', 'varie', 's')
    box(ax, cx - 14, 15, 28, 11, 'fixe', label=calc)
text(ax, 44, 8, 'deux calculs, un par nombre', 'fixe', 's')
save(fig, '11-098')
