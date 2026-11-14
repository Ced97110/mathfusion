import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
cs, x0, y0 = 3.6, 10.0, 24.0
text(ax, 44, 72, r'$99=9\times 11$', 'encre', 'l')
for i in range(9):
    for j in range(11):
        role = 'sujet' if j == 0 else ('autre' if i == 0 else 'fixe')
        ax.add_patch(Rectangle((x0 + i * cs, y0 + j * cs), cs, cs, ec=COL['fixe'] if role == 'fixe' else COL[role], fc=FILL[role], lw=0.4, zorder=2))
brace(ax, x0, x0 + 9 * cs, y0, 'sujet', r'$H$ : 9 éléments', down=True)
text(ax, 5, y0 + 5.5 * cs, r'$K$ : 11', 'autre', 's', rot=90)
text(ax, 48, 62, r'$n_p$ divise l’autre facteur', 'fixe', 's', ha='left')
text(ax, 48, 56, r'$n_p$ laisse le reste 1', 'fixe', 's', ha='left')
text(ax, 48, 46, r'$n_3=1$ : un seul $H$', 'sujet', 'm', ha='left')
text(ax, 48, 38, r'$n_{11}=1$ : un seul $K$', 'autre', 'm', ha='left')
text(ax, 48, 26, r'$G\cong H\times K$', 'resultat', 'l', ha='left', weight='bold')
save(fig, '50-203')
