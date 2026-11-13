import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(66)
text(ax, 44, 58, r'$2\,\frac{3}{4}=\frac{2\times4+3}{4}=\frac{11}{4}$', 'sujet', 'l')
bw, gap, y0 = 24, 3, 36
bar(ax, 5, y0, bw, 8, 4, ['sujet'] * 4)
bar(ax, 5 + bw + gap, y0, bw, 8, 4, ['sujet'] * 4)
bar(ax, 5 + 2 * (bw + gap), y0, bw, 8, 4, ['autre', 'autre', 'autre', None])
brace(ax, 5, 5 + 2 * bw + gap, y0 - 1, 'sujet', label='2 × 4 = 8 quarts')
brace(ax, 5 + 2 * (bw + gap), 5 + 2 * (bw + gap) + bw, y0 - 1, 'autre', label='3 quarts')
text(ax, 44, 12, '8 + 3 = 11 quarts', 'resultat', 'm')
save(fig, '06-036')
