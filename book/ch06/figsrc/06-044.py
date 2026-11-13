import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(64)
x0, w = 22, 60
bar(ax, x0, 46, w, 9, 8, ['sujet'] * 6 + [None] * 2)
for i in range(4):
    box(ax, x0 + i * 15 + 0.6, 44.2, 13.8, 12.6, 'varie', fill=False, dash=True)
bar(ax, x0, 14, w, 9, 4, ['resultat'] * 3 + [None])
text(ax, 11, 50.5, frac(6, 8), 'sujet', 'l')
text(ax, 11, 18.5, frac(3, 4), 'resultat', 'l')
arrow(ax, (x0 + 30, 42), (x0 + 30, 26), 'varie')
text(ax, x0 + 33, 34, 'regrouper 2 par 2', 'varie', 's', ha='left')
text(ax, x0 + 30, 60, '4 groupes, 3 pris', 'varie', 's')
save(fig, '06-044')
