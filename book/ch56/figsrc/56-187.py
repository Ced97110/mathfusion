import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$7\div3$ : reste $r=0$, diviseur $b=3$', 'sujet', 's')
# two columns with a vertical size scale
for x0, title, role, ok in [(8, 'taille constante', 'limite', False), (50, '0 pour le reste', 'resultat', True)]:
    text(ax, x0 + 15, 52, title, role, 's')
    line(ax, [(x0, 14), (x0, 44)], 'fixe')
    for y, v in [(16, '0'), (40, '1')]:
        ax.plot([x0 - 1.2, x0 + 1.2], [y, y], color=COL['fixe'], lw=0.8)
        text(ax, x0 - 3.5, y, v, 'fixe', 's')
    yr = 40 if not ok else 16
    disc(ax, x0 + 10, yr, 3, 'resultat' if ok else 'varie', label='r', size='s')
    disc(ax, x0 + 24, 40, 3, 'sujet', label='b', size='s')
    box(ax, x0 + 7, 2, 24, 8, role, label=('1 < 1 faux' if not ok else '0 < 1 vrai'), size='s')
save(fig, '56-187')
