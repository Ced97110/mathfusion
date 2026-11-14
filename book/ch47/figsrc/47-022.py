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

fig, ax = canvas(66)
cx, cy, s = 22, 36, 17
sq(ax, cx, cy, s)
disc(ax, cx, cy, 2.2, 'varie'); text(ax, cx+4.2, cy-3.5, r'$O$', 'varie', 's')
text(ax, cx, cy+s+5, 'le centre', 'fixe', 's')
ys = [52, 36, 20]; steps = ['quart de tour', 'demi-tour', 'trois quarts']
for k in range(3):
    text(ax, 58, ys[k]+3.5, steps[k], 'varie', 's')
    arrow(ax, (47, ys[k]), (68, ys[k]), 'varie')
    disc(ax, 74, ys[k], 3.4, 'varie', label=r'$O$', size='s')
text(ax, 62, 8, r'orbite de $O$ : $\{O\}$, 1 point', 'varie', 's')
save(fig, '47-022')
