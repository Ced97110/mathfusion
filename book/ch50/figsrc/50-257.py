import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 42, r'$|G| = 12$ : tailles possibles', 'encre', 'm', weight='bold')
for n in range(1, 12):
    r = 'resultat' if n in (1, 2, 3, 4) else ('fixe' if n == 6 else 'limite')
    box(ax, 4.5 + 7.2 * (n - 1), 24, 6.4, 7, r, label=('6 ?' if n == 6 else str(n)), size='s', r=0.3, lw=0.6)
box(ax, 4, 11.5, 4, 4, 'resultat', r=0.3); text(ax, 10, 13.5, 'garanti (Sylow)', 'resultat', 's', ha='left')
box(ax, 44, 11.5, 4, 4, 'limite', r=0.3); text(ax, 50, 13.5, 'interdit (Lagrange)', 'limite', 's', ha='left')
save(fig, '50-257')
