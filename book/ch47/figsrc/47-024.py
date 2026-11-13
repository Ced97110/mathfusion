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

fig, ax = canvas(80)
text(ax, 22, 74, 'carré', 'sujet', 'm', weight='bold'); text(ax, 66, 74, 'horloge', 'autre', 'm', weight='bold')
box(ax, 6, 56, 32, 10, 'sujet', label='4 rotations', size='s')
box(ax, 50, 56, 32, 10, 'autre', label='+0, +3, +6, +9', size='s')
arrow(ax, (22, 55), (22, 47), 'varie'); arrow(ax, (66, 55), (66, 47), 'varie')
text(ax, 31, 51, 'déplacent', 'varie', 's'); text(ax, 75, 51, 'déplacent', 'varie', 's')
cx, cy, s = 22, 29, 12
sq(ax, cx, cy, s)
for k in range(4):
    x, y = pt(cx, cy, 0.9*s*0.85, 55+90*k); disc(ax, x, y, 1.5, 'sujet')
for k, n in enumerate(['1', '4', '7', '10']):
    box(ax, 51+k*8, 24, 7, 10, 'autre', label=n, size='s', r=0.5)
text(ax, 22, 11, 'les 4 points', 'sujet', 's'); text(ax, 66, 11, 'les heures', 'autre', 's')
text(ax, 44, 3.5, 'groupe de 4 mouvements + ensemble déplacé', 'encre', 's')
save(fig, '47-024')
