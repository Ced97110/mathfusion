import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx = [15, 44, 73]; pw = 27
for x, h in zip(cx, ['liste', 'couple', 'ensemble']):
    text(ax, x, 52, h, 'encre', 'm', weight='bold')
    box(ax, x - pw/2, 6, pw, 40, 'sujet' if h == 'ensemble' else 'fixe', fill=(h == 'ensemble'), dash=(h != 'ensemble'))
for y, t in zip([36, 26, 16], ['lait', 'pain', 'lait']):
    box(ax, cx[0] - 7, y - 4, 14, 8, 'fixe', label=t, size='s')
arrow(ax, (cx[0] + 9.5, 38), (cx[0] + 9.5, 14), 'varie')
text(ax, cx[1], 36, r'$(2,5)$', 'autre', 'm'); text(ax, cx[1], 26, r'$\neq$', 'limite', 'm'); text(ax, cx[1], 16, r'$(5,2)$', 'autre', 'm')
for (x, y), t in zip([(70, 37), (77, 28), (71, 19)], ['gourde', 'carte', 'lampe']):
    text(ax, x, y, t, 'sujet', 's')
text(ax, cx[2], 10, 'pas d’ordre', 'sujet', 's')
save(fig, '42-019')
