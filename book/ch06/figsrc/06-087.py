import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def bar(y, n, k, role, rest='fixe', lab=None, h=8, x0=8, wd=72):
    for i in range(n):
        ax.add_patch(Rectangle((x0 + i * wd / n, y), wd / n, h, ec=COL[role if i < k else rest],
                     fc=FILL[role if i < k else rest], lw=0.6, zorder=2))
    if lab: text(ax, x0 + wd * k / n / 2, y + h / 2, lab, role, 's')
fig, ax = canvas(100)
bar(86, 4, 1, 'sujet', lab=r'$1/4$')
bar(72, 12, 3, 'sujet', lab=r'$3/12$')
arrow(ax, (14, 85), (14, 81), 'varie'); text(ax, 22, 83, r'$\times 3$', 'varie', 's')
bar(56, 6, 1, 'autre', lab=r'$1/6$')
bar(42, 12, 2, 'autre', lab=r'$2/12$')
arrow(ax, (14, 55), (14, 51), 'varie'); text(ax, 22, 53, r'$\times 2$', 'varie', 's')
bar(24, 12, 5, 'resultat', lab=r'$5/12$')
text(ax, 44, 68, '+', 'encre', 'l')
text(ax, 44, 12, 'parts de même nom : douzièmes', 'resultat', 's')
save(fig, '06-087')
