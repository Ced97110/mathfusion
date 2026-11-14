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
fig, ax = canvas(58)
xc, yc = table(ax, 14, 46, 8, 7, bg=lambda r, c: 'varie' if (r, c) == (1, 2) else 'fixe', xr=lambda r, c: 'varie' if (r, c) == (1, 2) else 'sujet')
for i in range(5): text(ax, xc(i), 49.5, str(i + 1), 'encre', 's')
for r, l in enumerate(['$e$', '$a$', '$b$', '$c$']): text(ax, 10, yc(r), l, 'encre', 's')
text(ax, 34, 55, r'nombre $x$', 'fixe', 's')
text(ax, 10, 55, r'$g$', 'fixe', 's')
text(ax, 71, 40, 'case orange :', 'varie', 'm')
text(ax, 71, 34, 'une croix', 'varie', 'm')
text(ax, 71, 28, '= un couple', 'varie', 'm')
text(ax, 34, 10, '12 croix = 12 couples', 'sujet', 'm')
save(fig, '49-214')
