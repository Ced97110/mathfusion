import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
bx, bw, bh = 4, 34, 10
ys = [64, 37, 10]
cx = bx + bw / 2
box(ax, bx, ys[0], bw, bh, 'sujet', label=r'$x_1^2+x_2^2$')
box(ax, bx, ys[1], bw, bh, 'varie', label=r'$-2x_1x_2$')
box(ax, bx, ys[2], bw, bh, 'resultat', label=r'$0$')
steps = [(r'on retire $e_1^2$', r'$e_1^2=x_1^2+2x_1x_2+x_2^2$'),
         (r'on retire $-2e_2$', r'$-2e_2=-2x_1x_2$')]
for i, (a, b) in enumerate(steps):
    y0, y1 = ys[i], ys[i + 1] + bh
    arrow(ax, (cx, y0), (cx, y1), 'varie')
    ym = (y0 + y1) / 2
    text(ax, cx + 3, ym + 2.2, a, 'varie', 'm', ha='left')
    text(ax, cx + 3, ym - 2.2, b, 'fixe', 's', ha='left')
text(ax, bx + bw + 4, ys[0] + bh / 2, r'plus haut : $x_1^2$', 'sujet', 'm', ha='left')
text(ax, bx + bw + 4, ys[1] + bh / 2, r'plus haut : $x_1x_2$', 'varie', 'm', ha='left')
text(ax, bx + bw + 4, ys[2] + bh / 2, 'plus rien à retirer', 'resultat', 'm', ha='left')
save(fig, '55-088')
