import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for k in range(2):
    ox = 8 + k * 42; oy = 10; s = 20
    box(ax, ox - 4, oy - 5, 38, 40, 'fixe', fill=False, dash=True)
    poly(ax, [(ox, oy), (ox + s, oy), (ox + s, oy + s), (ox, oy + s)], 'resultat')
    arrow(ax, (ox, oy), (ox + s, oy), 'sujet', lw=1.4)
    arrow(ax, (ox, oy), (ox, oy + s), 'autre', lw=1.4)
    text(ax, ox + s + 4, oy + 1, rf'$e_{k+1}$', 'sujet', 'm')
    text(ax, ox - 1, oy + s + 4, rf'$f_{k+1}$', 'autre', 'm')
    text(ax, ox + s / 2, oy + s / 2, 'aire 1', 'resultat', 's')
    text(ax, ox + 15, oy + 33 - 3, rf'$(e_{k+1},\ f_{k+1})$', 'encre', 'm')
save(fig, '75-051')
