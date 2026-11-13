import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def sq(ax, cx, cy, s, role='fixe'):
    poly(ax, [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)], role)
def grid(ax, x0, y0, cw, ch, gap, rows, cols, roles):
    cells = []
    for i in range(rows):
        for j in range(cols):
            x = x0 + j*(cw+gap); y = y0 + (rows-1-i)*(ch+gap)
            box(ax, x, y, cw, ch, roles[i], r=0.6)
            cells.append((x, y))
    return cells

fig, ax = canvas(60)
xs = [12, 44, 76]
for x, t in zip(xs, ['X', 'Y', 'Z']): disc(ax, x, 22, 3.5, 'sujet', label=r'$%s$' % t, size='s')
arrow(ax, (16, 22), (40, 22), 'varie'); arrow(ax, (48, 22), (72, 22), 'varie')
text(ax, 28, 17, r'$\alpha$ : quart de tour', 'varie', 's'); text(ax, 60, 17, r'$\beta$ : demi-tour', 'varie', 's')
arrow(ax, (13, 27), (75, 27), 'resultat', lw=1.3, curve=-0.4)
text(ax, 44, 44, r'trois quarts de tour : $\beta\alpha$', 'resultat', 's')
text(ax, 44, 6, r'$X\to Z$ par $\beta\alpha$ : dans $G$', 'resultat', 's')
save(fig, '47-032')
