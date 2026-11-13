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

fig, ax = canvas(64)
steps = ['ne rien faire', 'quart de tour', 'demi-tour', 'trois quarts de tour']
res = [r'$P$', r'$P_1$', r'$P_2$', r'$P_3$']
ys = [52, 38, 24, 10]
for k in range(4):
    disc(ax, 10, ys[k], 3.2, 'sujet', label=r'$P$', size='s')
    arrow(ax, (14.2, ys[k]), (51.8, ys[k]), 'varie')
    text(ax, 33, ys[k]+3, steps[k], 'varie', 's')
    disc(ax, 55, ys[k], 3.2, 'sujet', label=res[k], size='s')
box(ax, 49.5, 3.5, 11, 56.5, 'sujet', fill=False, dash=True, lw=0.8)
text(ax, 74, 31, 'orbite :\n4 points', 'sujet', 's')
save(fig, '47-021')
