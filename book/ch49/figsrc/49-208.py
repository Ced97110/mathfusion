import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
T = [[1,1,1,1,1],[1,0,1,1,0],[0,0,0,1,0],[0,1,0,1,1]]
def table(ax, x0, ytop, cw, ch, cols=(0,1,2,3,4), gaps=None, bg=None, xr=None, rows=(0,1,2,3)):
    gaps = gaps or [0]*len(cols)
    xs = []
    cur = x0
    for i in range(len(cols)):
        cur += gaps[i]; xs.append(cur); cur += cw
    for ri, r in enumerate(rows):
        for i, c in enumerate(cols):
            role = bg(r, c) if bg else 'fixe'
            y = ytop - (ri + 1) * ch
            ax.add_patch(Rectangle((xs[i], y), cw, ch, ec=COL['fixe'], fc='white' if role == 'fixe' else FILL[role], lw=0.5, zorder=1))
            if T[r][c]:
                rr = xr(r, c) if xr else 'sujet'
                if rr:
                    s = min(cw, ch) * 0.28; cx, cy = xs[i] + cw / 2, y + ch / 2
                    ax.plot([cx - s, cx + s], [cy - s, cy + s], color=COL[rr], lw=1.0, zorder=3, solid_capstyle='round')
                    ax.plot([cx - s, cx + s], [cy + s, cy - s], color=COL[rr], lw=1.0, zorder=3, solid_capstyle='round')
    return (lambda i: xs[i] + cw / 2), (lambda ri: ytop - (ri + 0.5) * ch)
fig, ax = canvas(52)
xc, yc = table(ax, 3, 36, 5, 5)
text(ax, 15.5, 42, '1. compter', 'varie', 'm')
for r, n in enumerate([5, 3, 1, 3]):
    text(ax, 33, yc(r), str(n), 'sujet', 'm')
    arrow(ax, (29, yc(r)), (31, yc(r)), 'varie', lw=0.7)
text(ax, 33, 42, 'points fixes', 'sujet', 's')
arrow(ax, (37, 26), (46, 26), 'varie')
text(ax, 54, 42, '2. additionner', 'varie', 'm')
box(ax, 47, 20, 14, 12, 'sujet', label='12', size='l')
arrow(ax, (62, 26), (69, 26), 'varie')
text(ax, 77, 42, '3. diviser par 4', 'varie', 'm', ha='center')
box(ax, 70, 20, 14, 12, 'resultat', label='3', size='l')
text(ax, 44, 8, 'de l\u2019intérieur vers l\u2019extérieur', 'fixe', 's')
save(fig, '49-208')
