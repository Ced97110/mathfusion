import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(68)
x0 = 22
rows = [(38, 4, 8, ['sujet'] * 3 + [None], 'sujet', frac(3, 4), '45 min'),
        (23, 6, 8, ['limite'] * 6, 'limite', frac(6, 4), '90 min'),
        (8, 8, 4, ['resultat'] * 6 + [None] * 2, 'resultat', frac(6, 8), '45 min')]
for y, n, cw, roles, role, f, lab in rows:
    bar(ax, x0, y, n * cw, 9, n, roles)
    text(ax, 12, y + 4.5, f, role, 'l')
    text(ax, 79, y + 4.5, lab, role, 'm')
ux = x0 + 32
line(ax, [(ux, 6), (ux, 52)], 'fixe', dash=True)
text(ax, ux, 56, '1 heure', 'fixe', 's')
text(ax, 12, 62, 'fraction', 'fixe', 's')
save(fig, '06-042')
