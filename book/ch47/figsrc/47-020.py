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

fig, ax = canvas(70)
cx, cy, s = 44, 36, 20
sq(ax, cx, cy, s, 'sujet')
for (x, y, t, dx, dy) in [(cx-s, cy-s, 'A', -3.5, -3), (cx+s, cy-s, r'$B$', 3.5, -3), (cx+s, cy+s, r'$C$', 3.5, 3), (cx-s, cy+s, r'$D$', -3.5, 3)]:
    text(ax, x+dx, y+dy, t, 'sujet', 'm')
disc(ax, cx, cy, 1.5, 'fixe'); text(ax, cx+3.5, cy-3, r'$O$', 'fixe', 's')
x, y = pt(cx, cy, 0.9*s, 55); disc(ax, x, y, 1.9, 'sujet'); text(ax, x+4, y-3.5, r'$P$', 'sujet', 's')
x2, y2 = pt(cx, cy, 0.9*s, 145)
line(ax, [(cx, cy), (x, y)], 'fixe', dash=True); line(ax, [(cx, cy), (x2, y2)], 'fixe', dash=True)
arrow(ax, (x + 0.2, y + 2.2), (x2 + 2.2, y2 + 0.8), 'varie', lw=1.2, curve=0.35)
disc(ax, x2, y2, 1.9, 'varie'); text(ax, x2 + 1, y2 - 4, r'$r(P)$', 'varie', 's')
arrow(ax, pt(cx, cy, 8, 10), pt(cx, cy, 8, 100), 'varie', lw=1.2, curve=0.35)
text(ax, cx-9, cy+9, r'$r$', 'varie', 'm')
text(ax, 44, 4.5, r'$r$ : quart de tour autour de $O$, $P \to r(P)$', 'varie', 's')
save(fig, '47-020')
