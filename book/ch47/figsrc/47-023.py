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
xs = [14, 34, 54, 74]; nums = ['1 (+0)', '4 (+3)', '7 (+6)', '10 (+9)']
disc(ax, 44, 63, 3.2, 'sujet', label='1', size='s')
for k in range(4):
    box(ax, xs[k]-7, 44, 14, 9, 'sujet', label=nums[k], size='s', r=0.6)
    dx = xs[k]-44
    arrow(ax, (44+dx*0.1, 59.8), (xs[k], 53.8), 'varie')
text(ax, 44, 38, "orbite de 1 : où 1 peut aller", 'sujet', 's')
roles = ['fixe', 'sujet', 'fixe']
cells = grid(ax, 5, 10, 18, 7, 2, 3, 4, roles)
for k in range(4):
    # grid x of column k : 7 + k*(15.5)
    gx = 5 + k*20 + 9
    line(ax, [(xs[k], 42), (gx, 27.5)], 'sujet', lw=0.6, dash=True) if False else None
text(ax, 44, 5, 'la ligne 1 + H de la grille', 'sujet', 's')
save(fig, '47-023')
