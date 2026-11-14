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
labs = [[0,3,6,9],[1,4,7,10],[2,5,8,11]]
cw, ch, gap, x0, y0 = 14, 9, 1.5, 15, 12
cells = grid(ax, x0, y0, cw, ch, gap, 3, 4, ['sujet']*3)
for i in range(3):
    for j in range(4):
        x, y = cells[i*4+j]
        text(ax, x+cw/2, y+ch/2, str(labs[i][j]), 'sujet', 'm')
text(ax, 44, 52, 'chaque nombre une seule fois', 'resultat', 's')
text(ax, 44, 5.5, '3 lignes de 4 : total 12', 'encre', 's')
save(fig, '47-018')
