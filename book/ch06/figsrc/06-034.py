import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(80)
# row 1 : true reading, 1 + 2/3
text(ax, 22, 62, r'$1\,\frac{2}{3}$', 'resultat', 'xl')
text(ax, 22, 50, r'$=1+\frac{2}{3}$', 'resultat', 'l')
bar(ax, 46, 56, 17, 8, 3, ['sujet'] * 3)
bar(ax, 66, 56, 17, 8, 3, ['autre', 'autre', None])
text(ax, 54.5, 68, '1 gâteau', 'sujet', 's')
text(ax, 74.5, 68, '2 tiers', 'autre', 's')
text(ax, 64.5, 51, '3 + 2 = 5 tiers', 'resultat', 's')
line(ax, [(3, 40), (85, 40)], 'fixe', dash=True)
# row 2 : false reading, 1 x 2/3
text(ax, 22, 26, r'$1\times\frac{2}{3}$', 'limite', 'xl')
text(ax, 22, 12, 'jamais', 'limite', 's')
bar(ax, 66, 22, 17, 8, 3, ['limite', 'limite', None])
text(ax, 74.5, 34, '2 tiers seulement', 'limite', 's')
text(ax, 74.5, 16, 'le gâteau a disparu', 'limite', 's')
save(fig, '06-034')
