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
text(ax, 14, 48, r'$G$', 'fixe', 'xl'); text(ax, 19.5, 48, r'$x$', 'varie', 'xl')
text(ax, 22, 56, 'orbite de x sous G', 'sujet', 's')
text(ax, 17, 41, r'$\neq$ un produit', 'limite', 's')
text(ax, 22, 30, r'$G$ : les 4 rotations', 'fixe', 's')
text(ax, 22, 25, r'$x$ : le point $P$', 'varie', 's')
arrow(ax, (31, 48), (46, 48), 'sujet'); text(ax, 38.5, 52, 'images', 'sujet', 's')
cx, cy, s = 66, 40, 15
sq(ax, cx, cy, s)
for k in range(4):
    x, y = pt(cx, cy, 0.9*s, 55+90*k); disc(ax, x, y, 1.9, 'sujet')
box(ax, 51, 12, 30, 8, 'sujet', label=r'$GP$ = les 4 images', size='s')
save(fig, '47-026')
