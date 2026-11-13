import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [r'$2^3\times2^2=2^5$', r'$2^3/2^2=2^1$', r'$2^0=1$',
        r'$(2^3)^2=2^6$', r'$(2\times3)^2=2^2\times3^2$', r'$(2/3)^2=2^2/3^2$']
rh, gap = 11, 2
for g, role in enumerate(('sujet', 'autre')):
    ytop = 82 - g * (3 * rh + 2 * gap + 6)
    for k in range(3):
        y = ytop - (k + 1) * rh - k * gap
        box(ax, 2, y, 54, rh, role, label=rows[3 * g + k], size='m')
    y0 = ytop - 3 * rh - 2 * gap
    box(ax, 59, y0, 27, 3 * rh + 2 * gap, role, label=('on compte\nles facteurs', 'on répète\nl’objet entier')[g], size='s', fill=False)
save(fig, '14-051')
