import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(58)
text(ax, 44, 52, 'diviseurs communs de 18 et 24', 'fixe', 's')
for i, v in enumerate([1, 2, 3, 6]):
    role = 'resultat' if v == 6 else 'fixe'
    box(ax, 18 + i * 14, 38, 10, 8, role, label=str(v))
text(ax, 18 + 3 * 14 + 5, 33, 'le plus grand', 'resultat', 's')
text(ax, 44, 12, r'$\frac{18}{24}=\frac{18\div6}{24\div6}=\frac{3}{4}$', 'resultat', 'l')
save(fig, '06-046')
