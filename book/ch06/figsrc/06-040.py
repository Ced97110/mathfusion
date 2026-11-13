import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(66)
rows = [(44, 'resultat', r'$\frac{3}{4}=\frac{3\times2}{4\times2}=\frac{6}{8}$', 'vrai'),
        (24, 'resultat', r'$\frac{3}{4}=\frac{3\times3}{4\times3}=\frac{9}{12}$', 'vrai'),
        (4, 'limite', r'$\frac{3}{4}\to\frac{3\times0}{4\times0}=\frac{0}{0}$', 'bas = 0 : impossible')]
for y, role, s, lab in rows:
    box(ax, 3, y, 82, 17, role)
    text(ax, 33, y + 8.5, s, role, 'l')
    text(ax, 71, y + 8.5, lab, role, 's')
text(ax, 44, 64, 'même entier en haut et en bas', 'fixe', 's')
save(fig, '06-040')
