import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
digits = ['1', '0', '0', '0', '7']
pitch, bw, x0 = 13, 9, 20
xs = [x0 + i * pitch for i in range(5)]
gap = lambda g: x0 + g * pitch + bw + (pitch - bw) / 2   # centre of the gap after box g
yt, yb = 46, 12
for row, y, lab in ((0, yt, 'cm'), (1, yb, 'm')):
    text(ax, 8, y + 4, lab, 'sujet', 'l', weight='bold')
    for i, d in enumerate(digits):
        box(ax, xs[i], y, bw, 9, 'fixe', label=d, size='l')
ax.add_patch(Circle((gap(2), yt + 1.2), 1.1, ec=COL['varie'], fc=COL['varie'], zorder=4))
ax.add_patch(Circle((gap(0), yb + 1.2), 1.1, ec=COL['varie'], fc=COL['varie'], zorder=4))
arrow(ax, (gap(2) - 1, yt - 2), (gap(0) + 1, yb + 12), 'varie', lw=1.2)
text(ax, 60, 29, 'la virgule recule de 2 rangs', 'varie', 's')
text(ax, 44, 59, 'les chiffres ne changent pas', 'fixe', 's')
save(fig, '11-049')
