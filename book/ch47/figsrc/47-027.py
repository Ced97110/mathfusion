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

fig, ax = canvas(72)
cx, cy, s = 44, 38, 20
sq(ax, cx, cy, s)
R = 0.9*s
ax.add_patch(Circle((cx, cy), R+3.5, ec=COL['sujet'], fc='none', lw=0.9, ls='--', zorder=1))
for k in range(4):
    x, y = pt(cx, cy, R, 55+90*k); disc(ax, x, y, 1.9, 'sujet')
ax.add_patch(Circle((cx, cy), 4, ec=COL['varie'], fc='none', lw=0.9, ls='--', zorder=1))
disc(ax, cx, cy, 1.6, 'varie')
text(ax, 66, 66, r'orbite de $P$ : 4', 'sujet', 's')
text(ax, 44, 29, r'orbite de $O$ : 1', 'varie', 's')
text(ax, 44, 4.5, 'deux orbites différentes : on les compte', 'encre', 's')
save(fig, '47-027')
