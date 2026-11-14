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
fig, ax = canvas(54)
xc, yc = table(ax, 11, 42, 12, 6)
for i in range(5):
    text(ax, xc(i), 46.5, str(i + 1), 'encre', 's')
ns = [2, 2, 2, 4, 2]
for i in range(5):
    arrow(ax, (xc(i), 17.8), (xc(i), 15.5), 'varie', lw=0.7)
    text(ax, xc(i), 12, str(ns[i]), 'varie', 'm')
text(ax, 44, 49, 'une colonne par nombre', 'fixe', 's')
text(ax, 44, 4, r'$N$ = 2 + 2 + 2 + 4 + 2 = 12', 'resultat', 'm')
save(fig, '49-216')
