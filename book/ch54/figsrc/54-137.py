import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
w, u = 8, 1.2
X = lambda i: 56 + 18 * i
text(ax, 44, 83, r'ℤ/10 n’est pas intègre : $2\times5=0$', 'varie', 's')
rows = [(66, 'sujet', r'$p=2+4x$', {0: 2, 1: 4}, False),
        (46, 'autre', 'constante 5', {0: 5}, False),
        (12, 'fixe', r'$5p=10+20x$', {0: 10, 1: 20}, True)]
for yb, role, lab, co, ghost in rows:
    line(ax, [(48, yb), (84, yb)], 'fixe')
    text(ax, 2, yb + 6, lab, role if not ghost else 'sujet', 'm', ha='left')
    for i in range(2):
        a = co.get(i, 0)
        if ghost:
            line(ax, [(X(i) - w / 2, yb), (X(i) + w / 2, yb)], 'varie', lw=1.4)
            ax.add_patch(Rectangle((X(i) - w / 2, yb), w, a * u, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=2))
            text(ax, X(i), yb + a * u + 3, f'{a} = 0', 'varie', 's')
        else:
            ax.add_patch(Rectangle((X(i) - w / 2, yb), w, a * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
            text(ax, X(i), yb + a * u + 3, str(a), role, 's')
for i in range(2):
    text(ax, X(i), 5, str(i), 'fixe', 's')
text(ax, 2, 5, 'position :', 'fixe', 's', ha='left')
text(ax, 2, 25, 'polynôme nul', 'varie', 's', ha='left')
save(fig, '54-137')
