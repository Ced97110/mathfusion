import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'une seule écriture : $p+3$', 'sujet', 'l', weight='bold')
# L=11, E=4, R=17 ; p+3 = 14, 7, 20
cols = [(16, 'L', 11, 14), (44, 'E', 4, 7), (72, 'R', 17, 20)]
for cx, ch, p, s in cols:
    box(ax, cx - 11, 48, 22, 9, 'fixe', label=f'lettre {ch}')
    arrow(ax, (cx, 48), (cx, 41), 'fixe')
    box(ax, cx - 11, 31, 22, 9, 'sujet', label=f'$p$ = {p}')
    arrow(ax, (cx, 31), (cx, 24), 'varie')
    box(ax, cx - 11, 14, 22, 9, 'varie', label=f'$p+3$ = {s}')
text(ax, 44, 7, '$p$ n’est pas une lettre : un numéro', 'fixe', 's')
save(fig, '53-036')
