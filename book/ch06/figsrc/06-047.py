import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(58)
x0, pitch = 33, 13
text(ax, 3, 50, 'diviseurs de 3', 'sujet', 's', ha='left')
text(ax, 3, 36, 'diviseurs de 4', 'autre', 's', ha='left')
for v in (1, 3):
    box(ax, x0 + (v - 1) * pitch, 46, 9, 8, 'resultat' if v == 1 else 'sujet', label=str(v))
for v in (1, 2, 4):
    box(ax, x0 + (v - 1) * pitch, 32, 9, 8, 'resultat' if v == 1 else 'autre', label=str(v))
line(ax, [(x0 + 4.5, 45.4), (x0 + 4.5, 40.6)], 'resultat', dash=True)
text(ax, x0 + 4.5, 25, 'seul diviseur commun', 'resultat', 's', ha='left')
text(ax, 44, 9, r'$\frac{3}{4}\div1=\frac{3}{4}$', 'resultat', 'l')
save(fig, '06-047')
