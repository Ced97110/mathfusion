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
fig, ax = canvas(56)
cw = 8
xc, yc = table(ax, 8, 40, cw, 6, cols=(0,2,1,4,3), gaps=[0,0,6,0,6], bg=lambda r, c: 'varie' if c in (0, 2) else ('autre' if c in (1, 4) else 'resultat'), xr=lambda r, c: 'sujet')
for i, c in enumerate((0,2,1,4,3)): text(ax, xc(i), 44, str(c + 1), 'encre', 's')
for a, b, lab in [(0, 1, 'orbite {1, 3}'), (2, 3, 'orbite {2, 5}'), (4, 4, 'orbite {4}')]:
    pass
groups = [(0, 1, 'varie'), (2, 3, 'autre'), (4, 4, 'resultat')]
for a, b, role in groups:
    brace(ax, xc(a) - cw / 2 + 0.3, xc(b) + cw / 2 - 0.3, 15, role, depth=1.4)
    text(ax, (xc(a) + xc(b)) / 2, 8, '4 croix', role, 'm')
text(ax, 44, 51, 'colonnes regroupées par orbite', 'fixe', 's')
save(fig, '49-217')
