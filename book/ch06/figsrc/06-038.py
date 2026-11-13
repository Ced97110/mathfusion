import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(72)
x0, x1 = 8, 62
rows = [(52, 2, 1, 2), (36, 4, 2, 4), (20, 8, 4, 8)]
fs = []
for y, n, a, b in rows:
    f = numberline(ax, x0, x1, y, 0, n, 1, labels=False, arrow_right=False)
    fs.append(f)
    text(ax, 75, y, frac(a, b), 'sujet', 'l')
    text(ax, x0, y - 4, '0', 'fixe', 's')
    text(ax, x1, y - 4, '1', 'fixe', 's')
px = x0 + 0.5 * (x1 - x0)
line(ax, [(px, 58), (px, 18)], 'resultat', dash=True)
for y, n, a, b in rows:
    disc(ax, px, y, 1.8, 'sujet')
text(ax, px, 65, 'même point', 'resultat', 's')
save(fig, '06-038')
