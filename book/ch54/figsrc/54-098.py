import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
cw, x0 = 11, 30
text(ax, 12, 72, 'position', 'fixe', 's')
for r in range(4):
    text(ax, x0 + (r + 0.5) * cw, 72, str(r), 'fixe', 's')
labs = [r'$x^0=1$', r'$x$', r'$x^2$', r'$x^3$']
ys = [56, 40, 24, 8]
for k in range(4):
    text(ax, 14, ys[k] + 4, labs[k], 'sujet', 'm')
    for r in range(4):
        if r == k:
            box(ax, x0 + r * cw + 0.3, ys[k], cw - 0.6, 8, 'sujet', label='1', size='m', weight='bold')
        else:
            box(ax, x0 + r * cw + 0.3, ys[k], cw - 0.6, 8, 'fixe', fill=False, dash=True)
    if k < 3:
        c = x0 + (k + 0.5) * cw
        arrow(ax, (c, ys[k] - 0.5), (c + cw, ys[k] - 7.5 + 0.0), 'varie')
        text(ax, c + cw / 2 + 8.5, ys[k] - 4, r'$\times\,x$', 'varie', 's')
save(fig, '54-098')
