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
cw = 4.2
text(ax, 14, 50, 'les couples', 'sujet', 'm')
table(ax, 3, 45, cw, cw)
text(ax, 14, 22, '12 croix', 'sujet', 'm')
arrow(ax, (26, 36), (31, 36), 'varie')
text(ax, 46, 50, 'regrouper par orbite', 'varie', 'm')
xc, yc = table(ax, 33, 45, cw, cw, cols=(0,2,1,4,3), gaps=[0,0,2.5,0,2.5], bg=lambda r, c: 'varie')
for a, b in [(0, 1), (2, 3), (4, 4)]:
    brace(ax, xc(a) - cw / 2 + 0.3, xc(b) + cw / 2 - 0.3, 27, 'varie', label=None, depth=1.2)
for a, b in [(0, 1), (2, 3), (4, 4)]:
    text(ax, (xc(a) + xc(b)) / 2, 21, '4', 'varie', 'm')
arrow(ax, (60, 36), (65, 36), 'varie')
text(ax, 76, 50, 'résultat', 'resultat', 'm')
box(ax, 66, 28, 20, 14, 'resultat', label=r'$N = 3 \times 4$', size='m')
text(ax, 76, 22, '= 12', 'resultat', 'm')
save(fig, '49-211')
