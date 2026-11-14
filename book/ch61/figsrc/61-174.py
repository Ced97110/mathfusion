import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
ox, oy, k = 8, 8, 7
arrow(ax, (ox, oy), (ox + 4.4 * k, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy), (ox, oy + 7.4 * k), 'fixe', lw=0.7)
line(ax, [(ox, oy), (ox + 3.4 * k, oy + 6.8 * k)], 'sujet', lw=1.4)
for p in ((1, 2), (3, 6)): disc(ax, ox + p[0] * k, oy + p[1] * k, 1.1, 'varie')
text(ax, 24, 20, '(1 ; 2)', 'varie', 's'); text(ax, 36, 46, '(3 ; 6)', 'varie', 's')
steps = ['points (1 ; 2) et (3 ; 6)', '6 − 2 = 4 ; 1 − 3 = −2', '÷ 2 : $a=2$, $b=-1$', r'$c=0$ avec un point', r'$2x-y=0$']
for i, t in enumerate(steps):
    y = 48 - 11 * i
    box(ax, 46, y, 40, 8, 'resultat' if i == 4 else 'varie' if i in (1, 2, 3) else 'sujet', label=t, size='s')
    if i < 4: arrow(ax, (66, y), (66, y - 3), 'fixe')
save(fig, '61-174')
