import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$A_4$ : 3 éléments d’ordre 2 en tout', 'varie', 's')
def row(x0, filled, role):
    box(ax, x0, 28, 38, 22, role)
    for k in range(4):
        x = x0 + 6 + k * 8.7
        if k == 0: disc(ax, x, 39, 3.2, 'fixe', label=r'$e$', size='s')
        elif filled: disc(ax, x, 39, 3.2, 'varie')
        else: ax.add_patch(Circle((x, 39), 3.2, ec=COL['limite'], fc='none', lw=0.8, ls='--', zorder=2))
row(4, True, 'sujet'); row(46, False, 'limite')
text(ax, 23, 22, 'un 2-Sylow : 4 éléments', 'sujet', 's')
text(ax, 65, 22, 'un autre : rien pour le remplir', 'limite', 's')
text(ax, 44, 8, r'un seul 2-Sylow : $n_2 = 1$', 'resultat', 'm', weight='bold')
save(fig, '50-160')
