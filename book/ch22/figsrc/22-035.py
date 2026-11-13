import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(62)
text(ax, 44, 57, r'$x=4$', 'fixe', 'l')
line(ax, [(44, 8), (44, 50)], 'fixe', dash=True)
h = 10
y = 34; xr = rad(ax, 6, y, 18, h, 'sujet')
text(ax, xr + 9, y + 4.2, r'$x+5$', 'encre', 'l')
text(ax, 22, 22, r'$=\sqrt{9}=3$', 'sujet', 'l')
text(ax, 22, 8, 'trait long', 'sujet', 'm')
xr = rad(ax, 50, y, 8, h, 'autre')
text(ax, xr + 4, y + 4.2, r'$x$', 'encre', 'l')
text(ax, xr + 8 + 6, y + 4.2, r'$+5$', 'encre', 'l')
text(ax, 66, 22, r'$=2+5=7$', 'autre', 'l')
text(ax, 66, 8, 'trait court', 'autre', 'm')
save(fig, '22-035')
