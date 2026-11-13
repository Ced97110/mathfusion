import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(66)
cw, gap, x0, y0 = 4.2, 2.0, 5.3, 36
x = x0
for g in range(3):
    bar(ax, x, y0, 5 * cw, 7, 5, ['sujet'] * 5, lw=0.6)
    brace(ax, x, x + 5 * cw, y0 - 1, 'sujet', label='5')
    x += 5 * cw + gap
bar(ax, x, y0, 2 * cw, 7, 2, ['varie'] * 2, lw=0.6)
text(ax, x0 + 5 * cw * 1.5 + gap, y0 + 12, '3 groupes de 5', 'sujet', 's')
text(ax, x + cw, y0 + 12, 'reste 2', 'varie', 's')
text(ax, 44, 20, r'$17 = 3\times5 + 2$', 'encre', 'm')
text(ax, 44, 7, r'$\frac{17}{5}=3\,\frac{2}{5}$', 'resultat', 'l')
save(fig, '06-035')
