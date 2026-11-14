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
pts = [pt(cx, cy, R, 55+90*k) for k in range(4)]
for k in range(4): disc(ax, *pts[k], 1.9, 'sujet')
text(ax, pts[0][0]+4, pts[0][1]+3, r'$P$', 'sujet', 's'); text(ax, pts[1][0]-4, pts[1][1]+3, r'$Q$', 'sujet', 's')
arrow(ax, pt(cx, cy, R, 55+14), pt(cx, cy, R, 145-14), 'varie', curve=-0.2)
text(ax, 44, 70, r'une rotation envoie $P$ sur $Q$', 'varie', 's')
disc(ax, cx, cy, 1.9, 'fixe'); text(ax, cx, cy-4.5, r'$O$', 'fixe', 's')
text(ax, 44, 14, r'$P$ et $Q$ sont liés', 'sujet', 'm')
text(ax, 44, 5, r'$O$ : lié à aucun autre', 'fixe', 's')
save(fig, '47-028')
