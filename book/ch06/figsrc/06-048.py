import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(66)
x0, cw, pitch = 22, 9, 12
num = [(2, 'varie'), (3, 'varie'), (3, 'resultat')]
den = [(2, 'varie'), (2, 'resultat'), (2, 'resultat'), (3, 'varie')]
yn, yd = 46, 22
for i, (v, r) in enumerate(num):
    box(ax, x0 + i * pitch, yn, cw, 8, r, label=str(v))
for i, (v, r) in enumerate(den):
    box(ax, x0 + i * pitch, yd, cw, 8, r, label=str(v))
line(ax, [(x0 - 2, 38), (x0 + 4 * pitch, 38)], 'encre', lw=1.2)
line(ax, [(x0 + cw / 2, yn), (x0 + cw / 2, yd + 8)], 'varie', dash=True)
line(ax, [(x0 + pitch + cw / 2, yn), (x0 + 3 * pitch + cw / 2, yd + 8)], 'varie', dash=True)
text(ax, 3, yn + 4, '18 =', 'sujet', 'm', ha='left')
text(ax, 3, yd + 4, '24 =', 'autre', 'm', ha='left')
text(ax, 78, 38, 'barrés', 'varie', 's')
text(ax, 44, 9, r'$\frac{3}{2\times2}=\frac{3}{4}$', 'resultat', 'l')
save(fig, '06-048')
