import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# deux images rangées en colonnes : un tableau, la matrice
cw, ch = 9, 8
text(ax, 17, 47, 'images des sacs', 'encre', 's')
cols = [('2', '1', 'sujet'), ('1', '3', 'varie')]
for k, (a, b, role) in enumerate(cols):
    x = 6 + k * 12
    box(ax, x, 30, cw, ch, role, label=a, size='m', r=0.5)
    box(ax, x, 21, cw, ch, role, label=b, size='m', r=0.5)
arrow(ax, (31, 29), (44, 29), 'resultat', lw=1.4)
# tableau
mx, my = 55, 21
for k, (a, b, role) in enumerate(cols):
    x = mx + k * 11
    box(ax, x, my + 9, cw, ch, role, label=a, size='m', r=0.5)
    box(ax, x, my, cw, ch, role, label=b, size='m', r=0.5)
    text(ax, x + cw / 2, 42, [r'$e_1$', r'$e_2$'][k], role, 's')
for j, lab in enumerate([r'$f_1$', r'$f_2$']):
    text(ax, 49.5, my + 13 - j * 9, lab, 'encre', 's')
for xx, d in [(mx - 2.2, 1), (mx + 21.2, -1)]:
    line(ax, [(xx + d * 1.6, my - 1.2), (xx, my - 1.2), (xx, my + 18.2), (xx + d * 1.6, my + 18.2)], 'encre', lw=1.0)
text(ax, mx + 10, 12, 'la matrice', 'resultat', 'm', weight='bold')
save(fig, '58-197')
