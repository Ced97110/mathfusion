import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for n, x0 in [(2, 8), (3, 30), (4, 56)]:
    for i in range(n):
        for j in range(n):
            ax.add_patch(Rectangle((x0 + 5 * i, 30 + 5 * j), 5, 5, ec=COL['sujet'], fc=FILL['sujet'], lw=0.6, zorder=2))
    text(ax, x0 + 2.5 * n, 25, r'$M_%d(R)$' % n, 'sujet', 'm')
    text(ax, x0 + 2.5 * n, 20, f'{n} × {n}', 'fixe', 's')
text(ax, 82, 40, r'$\cdots$', 'fixe', 'l')
box(ax, 4, 3, 80, 9, 'sujet', label=r'$M_n(R)$ : $n$ lignes, $n$ colonnes')
save(fig, '51-142')
