import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
FS = ' '
def mat(ax, cx, cy, rows, role='encre', size='m', pitch=4.6, gap=3):
    """Matrix as one text per row; returns (xs, ys) of cell centres and cell pitch."""
    cw = 0.636 * SIZE[size] * 25.4 / 72
    n = len(rows[0]); cell = (2 + gap) * cw; width = n * cell - gap * cw; left = cx - width / 2
    pad = lambda v: str(v).replace('-', '−').rjust(2, FS)
    ys = [cy + (len(rows) - 1) / 2 * pitch - i * pitch for i in range(len(rows))]
    xs = [left + j * cell + 1.3 * cw for j in range(n)]
    for y, r in zip(ys, rows): text(ax, cx, y, (FS * gap).join(pad(v) for v in r), role, size)
    xl, xr, yt, yb = left - 3.2, left + width + 3.2, ys[0] + pitch / 2, ys[-1] - pitch / 2
    line(ax, [(xl + 1, yt), (xl, yt), (xl, yb), (xl + 1, yb)], 'encre'); line(ax, [(xr - 1, yt), (xr, yt), (xr, yb), (xr - 1, yb)], 'encre')
    return xs, ys, cell
fig, ax = canvas(52)
text(ax, 18, 45, r'$R(\theta)$', 'sujet', 'l')
cells = [[r'$\cos\theta$', r'$-\sin\theta$'], [r'$\sin\theta$', r'$\cos\theta$']]
for i in range(2):
    for j in range(2):
        box(ax, 2 + j * 17, 28 - i * 11, 17, 10.5, 'sujet', label=cells[i][j], size='s')
text(ax, 18, 13, r'$\theta=90°$ :', 'varie', 's')
text(ax, 18, 8.5, r'$\cos 90°=0$', 'varie', 's')
text(ax, 18, 4, r'$\sin 90°=1$', 'varie', 's')
ox, oy, u = 62, 10, 4.2
line(ax, [(40, oy), (86, oy)], 'fixe'); line(ax, [(ox, 4), (ox, 36)], 'fixe')
P = (ox + 3 * u, oy + 4 * u); Q = (ox - 4 * u, oy + 3 * u)
line(ax, [(ox, oy), P], 'fixe', dash=True); line(ax, [(ox, oy), Q], 'fixe', dash=True)
arrow(ax, P, Q, 'varie', curve=0.35)
disc(ax, P[0], P[1], 1.2, 'sujet'); disc(ax, Q[0], Q[1], 1.2, 'resultat')
text(ax, P[0] + 1, P[1] + 3.5, '(3, 4)', 'sujet', 's')
text(ax, Q[0] - 1, Q[1] - 3.5, r'$(-4,\,3)$', 'resultat', 's')
text(ax, ox, 36, '90°', 'varie', 's')
save(fig, '73-067')
