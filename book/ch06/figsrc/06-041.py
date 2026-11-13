import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(62)
text(ax, 10, 52, frac(3, 4), 'sujet', 'l')
text(ax, 21, 52, '=', 'encre', 'l')
text(ax, 44, 52, r'$\frac{3\times2}{4\times2}$', 'varie', 'l')
text(ax, 67, 52, '=', 'encre', 'l')
text(ax, 78, 52, frac(6, 8), 'autre', 'l')
bar(ax, 4, 24, 38, 8, 4, ['sujet'] * 3 + [None])
bar(ax, 46, 24, 38, 8, 8, ['autre'] * 6 + [None] * 2)
text(ax, 23, 18, '45 min sur 60', 'sujet', 's')
text(ax, 65, 18, '45 min sur 60', 'autre', 's')
text(ax, 44, 8, 'haut et bas × 2', 'varie', 's')
save(fig, '06-041')
