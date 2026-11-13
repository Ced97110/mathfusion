import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(78)
text(ax, 10, 64, frac(3, 4), 'sujet', 'xl')
text(ax, 21, 64, r'$\times$', 'encre', 'l')
text(ax, 32, 64, frac(2, 2), 'varie', 'xl')
text(ax, 43, 64, '=', 'encre', 'l')
text(ax, 58, 64, frac(6, 8), 'autre', 'xl')
arrow(ax, (38, 53), (38, 45), 'fixe')
text(ax, 20, 38, r'$\frac{2}{2}=1$', 'varie', 'l')
bar(ax, 48, 34, 24, 8, 2, ['varie'] * 2)
text(ax, 76, 38, 'une unité', 'varie', 's', ha='left')
arrow(ax, (38, 31), (38, 23), 'fixe')
text(ax, 44, 14, r'$\frac{6}{8}=\frac{3}{4}\times1=\frac{3}{4}$', 'resultat', 'l')
save(fig, '06-043')
