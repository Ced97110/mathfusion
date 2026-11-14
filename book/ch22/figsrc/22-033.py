import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(56)
sx, y, h, w = 26, 14, 16, 18
xr = rad(ax, sx, y, w, h, 'fixe', 1.6)
text(ax, xr + w / 2, y + .42 * h, '16', 'varie', 'l')
box(ax, sx - 3, y - 3, xr - sx + w + 6, h + 6, 'sujet', fill=False, dash=True)
text(ax, 20, 48, 'signe radical', 'fixe', 'm')
arrow(ax, (22, 45), (sx + 2.5, y + .62 * h), 'fixe')
text(ax, 66, 48, 'radicande', 'varie', 'm')
arrow(ax, (62, 45), (xr + w / 2 + 1, y + .42 * h + 3.5), 'varie')
brace(ax, sx - 3, xr + w + 3, 10, 'sujet', 'le radical : le tout', True, 'm')
save(fig, '22-033')
