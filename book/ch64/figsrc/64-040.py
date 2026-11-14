import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [1.5 + i * 12.4 for i in range(7)]; w = 10.6; h = 10
y1, y2 = 38, 16
row1 = {0: r'$\mathbb{Z}$', 2: r'$9\mathbb{Z}$', 3: r'$45\mathbb{Z}$', 5: r'$180\mathbb{Z}$', 6: r'$\{0\}$'}
row2 = [r'$\mathbb{Z}$', r'$3\mathbb{Z}$', r'$9\mathbb{Z}$', r'$45\mathbb{Z}$', r'$90\mathbb{Z}$', r'$180\mathbb{Z}$', r'$\{0\}$']
for i in range(7):
    new = i in (1, 4)
    if i in row1:
        box(ax, xs[i], y1, w, h, 'sujet', label=row1[i], size='s')
    box(ax, xs[i], y2, w, h, 'varie' if new else 'sujet', label=row2[i], size='s')
    cx = xs[i] + w / 2
    if new:
        arrow(ax, (cx, y1 + 4), (cx, y2 + h + 0.5), 'varie')
    else:
        line(ax, [(cx, y1 - 0.5), (cx, y2 + h + 0.5)], 'fixe', lw=0.5, dash=True)
c = lambda i: xs[i] + w / 2
brace(ax, c(0), c(2), y2 - 0.5, 'varie', label=r'$9$ → $3\times3$')
brace(ax, c(3), c(5), y2 - 0.5, 'varie', label=r'$4$ → $2\times2$')
save(fig, '64-040')
