import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'on résout une seule fois', 'varie', 'm', weight='bold')
box(ax, 14, 50, 60, 12, 'sujet', label=r'$l = (P - 2w)\,/\,2$', size='l')
for cx, inp, out in [(23, r'$P$ = 20, $w$ = 3', r'$l$ = 7'), (65, r'$P$ = 30, $w$ = 5', r'$l$ = 10')]:
    arrow(ax, (cx + (6 if cx < 44 else -6), 50), (cx, 40), 'varie')
    box(ax, cx - 20, 28, 40, 11, 'varie', label=inp, size='m')
    arrow(ax, (cx, 28), (cx, 19), 'varie')
    box(ax, cx - 14, 6, 28, 12, 'resultat', label=out, size='l')
text(ax, 44, 45, 'puis on remplace', 'fixe', 's')
save(fig, '16-116')
