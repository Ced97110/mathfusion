import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# L = 11, a = 5 : 5 x 11 = 55 ; b = 3 -> 58 -> reste 6 ; b = 0 -> 55 -> reste 3
box(ax, 22, 62, 44, 11, 'fixe', label='5 × 11 = 55')
for x, b, mid, rest in [(2, 3, '58', 'reste 6'), (46, 0, '55', 'reste 3')]:
    cx = x + 20
    arrow(ax, (44 + (cx - 44) * 0.6, 62), (cx, 54), 'varie')
    box(ax, x, 42, 40, 11, 'varie', label=f'$b$ = {b} : on obtient {mid}')
    arrow(ax, (cx, 42), (cx, 32), 'fixe')
    text(ax, cx + 9, 37, 'mod 26', 'fixe', 's')
    box(ax, x, 20, 40, 11, 'resultat', label=rest, weight='bold')
text(ax, 44, 10, '$b$ décale le résultat après ×', 'sujet', 's', weight='bold')
save(fig, '53-046')
