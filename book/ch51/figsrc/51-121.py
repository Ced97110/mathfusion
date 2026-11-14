import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$\mathbb{Z}/7$ : on retire les 7', 'encre', 'm')
cw = 2.0
def bar(y, n, label):
    text(ax, 44, y + 5.5, label, 'sujet', 'm')
    x = 4.0
    for i in range(n):
        last = i == n - 1
        ax.add_patch(Rectangle((x, y), cw, 3.5, ec=COL['resultat' if last else 'fixe'], fc=FILL['resultat' if last else 'fixe'], lw=0.5, zorder=2))
        x += cw
        if (i + 1) % 7 == 0 and not last: x += 1.5
bar(42, 15, r'$3\times 5=15=2\times 7+1$')
bar(24, 8, r'$2\times 4=8=1\times 7+1$')
bar(6, 36, r'$6\times 6=36=5\times 7+1$')
save(fig, '51-121')
