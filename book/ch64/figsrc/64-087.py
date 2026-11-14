import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def panel(x, head, radical):
    text(ax, x + 20, 59, head, 'sujet' if not radical else 'resultat', 's', weight='bold')
    box(ax, x, 12, 40, 40, 'sujet')
    box(ax, x + 4, 16, 22, 22, 'fixe')
    text(ax, x + 3, 48.5, r'$F_{i+1}$', 'sujet', 's', ha='left')
    text(ax, x + 6, 34.5, r'$F_i$', 'fixe', 's', ha='left')
    disc(ax, x + 34, 25, 3.4, 'varie', label=r'$d_i$', size='s')
    if radical:
        disc(ax, x + 15, 25, 3.4, 'fixe', label=r'$a_i$', size='s')
        arrow(ax, (x + 18.8, 25), (x + 30, 25), 'varie')
        text(ax, x + 20, 6, r'$d_i^{\,n_i}=a_i\in F_i$', 'resultat', 's')
    else:
        text(ax, x + 20, 6, r'$d_i$ : aucune condition', 'fixe', 's')
panel(2, 'tour quelconque', False)
panel(46, 'tour de radicaux', True)
save(fig, '64-087')
