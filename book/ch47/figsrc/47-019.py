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
cx, cy, s = 44, 40, 20
sq(ax, cx, cy, s)
R = 0.9*s
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.7, ls='--', zorder=1))
names = [r'$P$', r'$r(P)$', r'$r^2(P)$', r'$r^3(P)$']
offs = [(7, 3), (-8, 3), (-8, -3.5), (8, -3.5)]
for k in range(4):
    x, y = pt(cx, cy, R, 55 + 90*k)
    disc(ax, x, y, 1.9, 'sujet')
    text(ax, x+offs[k][0], y+offs[k][1], names[k], 'sujet', 's')
    x2, y2 = pt(cx, cy, R, 55 + 90*(k+1))
    a0 = pt(cx, cy, R, 55 + 90*k + 14); a1 = pt(cx, cy, R, 55 + 90*(k+1) - 14)
    arrow(ax, a0, a1, 'varie', curve=-0.2)
disc(ax, cx, cy, 1.9, 'varie')
text(ax, cx, cy-4.5, r'$O$', 'varie', 's')
text(ax, 44, 74, 'orbite de P : 4 points', 'sujet', 'm')
text(ax, 44, 5, 'O reste seul à sa place', 'varie', 's')
save(fig, '47-019')
