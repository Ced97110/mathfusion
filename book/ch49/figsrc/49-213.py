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
fig, ax = canvas(50)
cw = 4.4
labs = ['une ligne : 3', 'une colonne : 2', r'tout : $N$ = 12']
for k, x0 in enumerate([2, 32, 62]):
    if k == 0: bg = lambda r, c: 'autre' if r == 1 else 'fixe'; xr = lambda r, c: 'autre' if r == 1 else 'fixe'
    elif k == 1: bg = lambda r, c: 'autre' if c == 0 else 'fixe'; xr = lambda r, c: 'autre' if c == 0 else 'fixe'
    else: bg = lambda r, c: 'sujet'; xr = lambda r, c: 'sujet'
    table(ax, x0 + 2, 36, cw, cw, bg=bg, xr=xr)
    text(ax, x0 + 2 + 2.5 * cw, 14, labs[k], 'sujet' if k == 2 else 'autre', 's')
text(ax, 44, 44, 'compter des croix', 'fixe', 'm')
save(fig, '49-213')
