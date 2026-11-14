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

fig, ax = canvas(52)
cells = grid(ax, 6, 10, 13, 9, 1.5, 3, 4, ['sujet']*3)
brace(ax, 6, 62.5, 42, 'fixe', '4 cases par ligne', down=False)
yb = 10; yt = 10 + 3*9 + 2*1.5
line(ax, [(65, yb), (66.6, yb), (66.6, yt), (65, yt)], 'fixe')
text(ax, 77, (yb+yt)/2, '3 lignes', 'fixe', 's')
text(ax, 44, 4, r'$12 = 4 \times 3$', 'resultat', 'l')
save(fig, '47-017')
