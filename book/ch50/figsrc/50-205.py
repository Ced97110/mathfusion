import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, x0 = 4.2, 20.0
text(ax, 44, 58, r'$n_{11}$ divise 9 : 1, 3 ou 9', 'encre', 'm')
text(ax, x0 + 5.5 * cw, 50, 'reste de la division par 11', 'fixe', 's')
for yb, n, role in [(36, 1, 'resultat'), (24, 3, 'limite'), (12, 9, 'limite')]:
    for i in range(11):
        full = i < n
        ax.add_patch(Rectangle((x0 + i * cw, yb), cw, 6, ec=COL[role] if full else COL['fixe'], fc=FILL[role] if full else 'white', lw=0.7, zorder=2))
    text(ax, 11, yb + 3, rf'$n_{{11}}={n}$', 'encre', 'm'); text(ax, 78, yb + 3, f'reste {n}', role, 's', weight='bold')
text(ax, 44, 5, r'seul $n_{11}=1$ reste possible', 'resultat', 'm')
save(fig, '50-205')
