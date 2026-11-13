import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(72)
x0, x1 = 10, 78
ya, yb = 50, 24
fa = numberline(ax, x0, x1, ya, 0, 4, 1, labels=False, arrow_right=False)
fb = numberline(ax, x0, x1, yb, 0, 8, 1, labels=False, arrow_right=False)
for f, y in ((fa, ya), (fb, yb)):
    text(ax, f(0) if False else x0, y - 4, '0', 'fixe', 's')
    text(ax, x1, y - 4, '1', 'fixe', 's')
px = fa(3)
line(ax, [(px, ya), (px, yb)], 'resultat', dash=True)
disc(ax, px, ya, 1.8, 'sujet')
disc(ax, px, yb, 1.8, 'autre')
text(ax, px, ya + 6, r'$P=\frac{3}{4}$', 'sujet', 'm')
text(ax, px, yb - 8, r'$\frac{6}{8}$', 'autre', 'm')
text(ax, x0, ya + 6, '4 parts', 'sujet', 's', ha='left')
text(ax, x0, yb + 6, '8 parts', 'autre', 's', ha='left')
text(ax, px - 1.5, (ya + yb) / 2, 'même point', 'resultat', 's', ha='right')
save(fig, '06-037')
