import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(58)
bar(ax, 6, 36, 34, 10, 3, ['sujet'] * 3)
bar(ax, 48, 36, 34, 10, 3, ['autre', 'autre', None])
text(ax, 23, 50, '1 pizza entière', 'sujet', 's')
text(ax, 65, 50, '2 parts sur 3', 'autre', 's')
arrow(ax, (23, 34), (23, 26), 'sujet')
arrow(ax, (65, 34), (65, 26), 'autre')
text(ax, 23, 18, '1', 'sujet', 'xl')
text(ax, 65, 18, frac(2, 3), 'autre', 'xl')
arrow(ax, (31, 18), (57, 18), 'fixe')
text(ax, 44, 21.5, 'suivi de', 'fixe', 's')
text(ax, 23, 6, 'un entier', 'sujet', 's')
text(ax, 65, 6, 'une fraction propre', 'autre', 's')
save(fig, '06-033')
