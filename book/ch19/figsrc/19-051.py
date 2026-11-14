import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def plane(ax, ox, oy, sx, sy, xr, yr):
    P = lambda x, y: (ox + x * sx, oy + y * sy)
    arrow(ax, P(xr[0], 0), P(xr[1], 0), "fixe", lw=0.8)
    arrow(ax, P(0, yr[0]), P(0, yr[1]), "fixe", lw=0.8)
    return P
fig, ax = canvas(66)
cols = [22, 36, 50, 64, 78]
for c, s in zip((22, 50, 78), 'abc'): box(ax, c - 5, 52, 10, 9, 'varie', label=f'${s}$', size='l')
text(ax, 36, 56.5, r'$x+$', 'sujet', 'l'); text(ax, 64, 56.5, r'$y=$', 'sujet', 'l')
for y, vals, name in ((36, (2, 3, 12), 'cas 1'), (16, (5, 1, 4), 'cas 2')):
    text(ax, 8, y + 4.5, name, 'fixe', 's')
    for c, v in zip((22, 50, 78), vals):
        box(ax, c - 5, y, 10, 9, 'varie', fill=False, label=str(v), size='m')
        line(ax, [(c, y + 9.8), (c, y + 14.5)], 'fixe', lw=0.6, dash=True)
for c in (22, 50, 78): line(ax, [(c, 51.2), (c, 46)], 'fixe', lw=0.6, dash=True)
save(fig, '19-051')
