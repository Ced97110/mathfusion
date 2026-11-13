import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(70)
x0, w = 8, 72
bar(ax, x0, 50, w, 9, 4, ['sujet'] * 3 + [None])
bar(ax, x0, 18, w, 9, 8, ['sujet'] * 6 + [None] * 2)
text(ax, 44, 63, '4 parts, 3 coloriées', 'sujet', 's')
text(ax, 44, 12, '8 parts, 6 coloriées', 'sujet', 's')
arrow(ax, (20, 47), (20, 30), 'varie')
text(ax, 23, 38.5, 'chaque part en 2', 'varie', 's', ha='left')
px = x0 + 0.75 * w
line(ax, [(px, 60), (px, 17)], 'resultat', dash=True)
text(ax, px + 1.5, 44.5, 'même', 'resultat', 's', ha='left')
text(ax, px + 1.5, 41, 'longueur', 'resultat', 's', ha='left')
save(fig, '06-039')
