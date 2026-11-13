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
text(ax, 20, 46, 'par lignes', 'sujet', 'm')
xc, yc = table(ax, 4, 42, 5, 5)
for r, n in enumerate([5, 3, 1, 3]):
    text(ax, 33, yc(r), str(n), 'sujet', 'm')
box(ax, 10, 8, 20, 8, 'resultat', label='12', size='l')
text(ax, 66, 46, 'par colonnes', 'autre', 'm')
xc2, yc2 = table(ax, 52, 42, 5, 5, bg=lambda r, c: 'limite' if c == 3 else 'fixe', xr=lambda r, c: 'limite' if c == 3 else 'autre')
for i, n in enumerate([2, 2, 2, None, 2]):
    if n is not None: text(ax, xc2(i), 18, str(n), 'autre', 'm')
text(ax, xc2(3), 18, '?', 'limite', 'm', weight='bold')
text(ax, xc2(3), 13.5, 'colonne oubliée', 'limite', 's')
box(ax, 57, 3, 20, 8, 'limite', label='8', size='l')
text(ax, 44, 8, r'$\neq$', 'limite', 'l')
save(fig, '49-210')
