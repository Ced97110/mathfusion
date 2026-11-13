import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def bar(ax, x, y, w, h, n, roles, lw=0.8):
    for i in range(n):
        r = roles[i]
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[r or 'fixe'], fc=FILL[r] if r else 'white', lw=lw, zorder=2))

def frac(a, b):
    return r'$\frac{%s}{%s}$' % (a, b)

fig, ax = canvas(72)
def groups(y, k, role):
    for g in range(k):
        gx = 6 + g * 15
        box(ax, gx, y, 14, 10, 'varie', fill=False, dash=True)
        for i in range(6):
            disc(ax, gx + 3 + (i % 3) * 4, y + 2.5 + (i // 3) * 5, 1.4, role)
groups(50, 2, 'sujet')
groups(30, 5, 'autre')
text(ax, 6, 65, '12 = 2 groupes de 6', 'sujet', 's', ha='left')
text(ax, 6, 45, '30 = 5 groupes de 6', 'autre', 's', ha='left')
text(ax, 44, 22, 'PGCD = 6 : la taille des groupes', 'varie', 's')
text(ax, 44, 9, r'$\frac{12}{30}=\frac{12\div6}{30\div6}=\frac{2}{5}$', 'resultat', 'l')
save(fig, '06-045')
